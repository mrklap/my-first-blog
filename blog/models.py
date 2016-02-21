from django.db import models

from django.utils import timezone


class Post(models.Model):   #definiujemy tu model.
    #poni¿ej definiujemy w³aœciwoœci
    author = models.ForeignKey('auth.User') #to jest link do innego modelu
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
        default = timezone.now)
    published_date = models.DateTimeField(
        blank = True, null = True)

    #definiujemy metody
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

