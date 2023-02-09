from django.db import models


class Category(models.Model):
    category = models.CharField(max_length=200, null=True, unique=True, default='')
    slug = models.SlugField(max_length=200, null=True, unique=True, allow_unicode=True)

    def __str__(self):
        return self.category

    class Meta:
        ordering = ('category',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class Product(models.Model):
    name = models.CharField(max_length=200, null=True, unique=True, default='')
    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE)
    description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to="static/images", blank=True)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'product'
        verbose_name_plural = 'products'
