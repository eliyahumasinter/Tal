from django.db import models
from django.utils import timezone
from PIL import Image
# Create your models here.


class Email(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email


class Card(models.Model):
    title = models.CharField(max_length=60)
    subtitle = models.CharField(max_length=120)
    button_text = models.CharField(max_length=25)
    link = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='images')
    date_posted = models.DateTimeField(default=timezone.now)

    def save(self):
        super().save()
        img = Image.open(self.image.path)
        if img.height > 400 or img.width > 400:
            output_size = (400, 400)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def __str__(self):
        return self.title


class Event(models.Model):
    title = models.CharField(max_length=80)
    subtitle = models.CharField(max_length=120)
    date = models.DateTimeField()
    address = models.CharField(max_length=500)

    def __str__(self):
        return self.title
