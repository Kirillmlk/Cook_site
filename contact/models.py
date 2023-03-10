from django.db import models


class ContactModel(models.Model):
    """ класс модели обратной связи"""
    name = models.CharField(max_length=50)
    email = models.EmailField()
    website = models.URLField(blank=True, null=True)
    message = models.TextField(max_length=5000)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.email}'


class ContactLink(models.Model):
    icon = models.FileField(upload_to="icons/")
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name