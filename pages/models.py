from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to="static/images", blank=True)
    pub_date = models.DateTimeField('date published')

