## django-upstorage-backend

This is a custom django storage backend for `UpStorage`

## Installation
1. Install Library Using `pip`
````shell script
>> pip install django-upstorage-backend
````

## Starting Guide

1. Set The Custom Storage Backend. Now Open settings.py of your project.
````python
DEFAULT_FILE_STORAGE = 'django-upstorage-backend.storages.backends.U3Storage'
````

2. Set some required KEYS to `settings.py`
````python
AUTH_TOKEN = 'auth token from your account'
API_KEY = 'api key of your project'
USERNAME = 'username of your account'
PROJECT_NAME = 'Created Project name'
````

Thats it, We are all done. Now all of your files will be handeled by the custom UpStorage's Backend Storage.


## Advanced Guide

* `You don't need to set 'upload_to' in model Fields (Defaultly it files will be saved on the root of your project.)`

* `File Link Will Be Stored On Your Model As Expected.You Can call them as you do usally.`

* `You Can also set 'upload_to='specific/folder' in your model like:`
   ````python
  Class TestModel(model.Model):
      image = models.ImageField(upload_to='to/my/folder')
  
  # this will save the file to that folder.if there's no folder it will create it.
  ````

* `If you want to delete the image from the UpStorage Bucket when you delete it from django, you have to do it a bit differently.Lemme show you`
   ````python
  Class TestModel(model.Model):
      image = models.ImageField()
  
  # To delete the image you have to delete that by writing:
  
  obj = TestModel.objects.get(id=pk)
  obj.image.delete()
  
  # You can't directly delete it like this:
  
  obj.delete() # this won't delete the file from UpStorage
  
  # You have to delete the file field first to delete it.
  ````
  To make it simple you can override `delete` Method on your Model
  
  ````python
  Class TestModel(model.Model):
      image = models.ImageField()
  
      def delete(self):
          self.image.delete()
          super(TestModel, self).delete()
  ````

