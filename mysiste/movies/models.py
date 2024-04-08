from django.db import models

class Moviedata(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=100)
    duration = models.FloatField()
    rating = models.IntegerField()
    typ = models.CharField(max_length=100, default='scifi')
    image = models.ImageField(upload_to='images/', default='images/None/no-img.jpg')