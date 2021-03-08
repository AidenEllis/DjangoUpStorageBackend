from django.core.files.storage import Storage
from django.utils.deconstruct import deconstructible
from UpStorageApiClient.api import UpStorageBucket
from .utils import get_setting


@deconstructible
class U3Storage(Storage):
    """
    Custom Backend Storage.That Upload Files To UpStorage.
    """

    def __init__(self):
        self.storage_host = 'http://127.0.0.1:8000/api/storage/file'
        self.AUTH_TOKEN = get_setting('AUTH_TOKEN')
        self.API_KEY = get_setting('API_KEY')
        self.USERNAME = get_setting('USERNAME')
        self.PROJECT_NAME = get_setting('PROJECT_NAME')

    def _open(self, name, mode='rb'):
        pass

    def _save(self, name, content):
        client = UpStorageBucket(auth_token=self.AUTH_TOKEN, api_key=self.API_KEY)
        req = client.upload(file=content)
        return str(req['file']).split('/')[-2]

    def url(self, name):
        return f'http://127.0.0.1:8000/api/storage/file/{self.USERNAME}/{self.PROJECT_NAME}/{name}/'

    def exists(self, name):
        return False
