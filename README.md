## django-upstorage-backend

This is a custom django storage backend for `UpStorage`

## Installation
1. Install Library Using `pip`
````shell script
>> pip install django-upstorage-backend
````

## Starting Guide

1. Set The Custom Storage Backend.open settings.py of your project.
````python
DEFAULT_FILE_STORAGE = 'django-upstorage-backend.storages.backends.U3Storage'
````

2.Set some required KEYS to `settings.py`
````python
AUTH_TOKEN = 'auth token from your account'
API_KEY = 'api key of your project'
USERNAME = 'username of your account'
PROJECT_NAME = 'Created Project name'
````

Thats it.We are done.Now all of your files will be handeled by the custom UpStorage Backend Storage

## Some More Info

* `You dont need to set 'upload_to' in model Fields (until custom folder selection update comes)`

* `File Link Will Be Stored On Your Model.You Can call them as you do usally.`


## Upcoming Updates

* `Delete File for UpStorage When Django Deletes it from its database.You can easily enable or disable this feature`

* `Save Files On Custom Folders In Your Project.You can set specific folder location by adding the folder name on 'upload_to='my_folder' on ModelFields.By using this you can organize your files into specific folders.`


