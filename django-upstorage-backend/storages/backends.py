from django.core.files.storage import Storage
from django.utils.deconstruct import deconstructible
from UpStorageApiClient.api import UpStorageBucket
from .utils import get_setting
from django.core.files import File


@deconstructible
class U3Storage(Storage):
    """
    Custom Backend Storage.That Upload Files To UpStorage.
    """

    def __init__(self):
        self.host = 'https://upstorage.pythonanywhere.com'
        self.storage_host = f'{self.host}/api/storage/file'
        self.AUTH_TOKEN = get_setting('AUTH_TOKEN')
        self.API_KEY = get_setting('API_KEY')
        self.USERNAME = get_setting('USERNAME')
        self.PROJECT_NAME = get_setting('PROJECT_NAME')
        self.bucket = UpStorageBucket(auth_token=self.AUTH_TOKEN, api_key=self.API_KEY)

    def _open(self, name, mode='rb'):
        pass

    def _save(self, name, content):
        """
        Unfortunately you can't send the filename with the folder name it will convert to just the file name.
        so we add special charecter to split those '/'. we do it by '____set_dir_name____' this special
        word.
        """
        name = name.replace(" ", "_")
        upload_to_list = name.split('\\')
        upload_to = "".join(str(x + '____set_dir_name____') for x in upload_to_list[:-1])

        content_name = f"{upload_to}{content.name}"

        content = File(content, content_name)

        response = self.bucket.upload(file=content)

        return str(response['file']).split(f"/{self.PROJECT_NAME}")[-1]

    def url(self, name):
        return f'{self.storage_host}/{self.USERNAME}/{self.PROJECT_NAME}/{name}'

    def exists(self, name):
        return False

    def delete(self, name):
        self.bucket.delete(name)
