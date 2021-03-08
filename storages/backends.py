from django.core.files.storage import Storage
from django.utils.deconstruct import deconstructible
from UpStorageApiClient.api import UpStorageBucket


@deconstructible
class U3Storage(Storage):
    """
    Custom Backend Storage.That Upload Files To UpStorage.
    """

    def __init__(self):
        self.key = 'setdstings.KEY'

    def _open(self, name, mode='rb'):
        pass

    def _save(self, name, content):
        client = UpStorageBucket(auth_token='testtoken', api_key='testkey1')
        req = client.upload(file=content)
        return str(req['file']).split('/')[-2]

    def url(self, name):
        return f'http://127.0.0.1:8000/api/storage/file/sakib/PMS/{name}/'

    def exists(self, name):
        return False


