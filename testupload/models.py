from django.db import models


class TestModel(models.Model):
    image = models.ImageField()

    def __str__(self):
        return str(self.id)

