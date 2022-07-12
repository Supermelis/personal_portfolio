from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=200)
    blogDate = models.DateField()
    description = models.CharField(max_length=250)
