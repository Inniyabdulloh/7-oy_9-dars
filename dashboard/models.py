from django.db import models

# Create your models here.
class Services(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.ImageField(upload_to='services/')

    def __str__(self):
        return self.name


class Portfolio(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='portfolio/')

    def __str__(self):
        return self.name


class Staff(models.Model):
    full_name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    bio = models.TextField()

    image = models.ImageField(upload_to='staff/')

    twitter = models.URLField(max_length=255)
    facebook = models.URLField(max_length=255)
    instagram = models.URLField(max_length=255)
    linkedin = models.URLField(max_length=255)

    def __str__(self):
        return self.full_name




