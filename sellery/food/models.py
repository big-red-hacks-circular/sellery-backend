from django.db import models

class Food(models.Model):
    name = models.CharField(max_length=200)
    labels = models.CharField(max_length=600, blank=True)
    img_url = models.CharField(max_length=200)

    def __str__(self):
        return self.name