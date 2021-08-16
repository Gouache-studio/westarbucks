from django.db import models

# Create your models here.

class Menu(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        db_table = 'menus' #테이블 이름을 만듦

class Category(models.Model):
    name = models.CharField(max_length=20)
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE)

    class Meta:
        db_table = 'categories'

class Product(models.Model):
    name = models.CharField(max_length=20)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    class Meta:
        db_table = 'products'

class Image(models.Model):
    image_url = models.CharField(max_length=500)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)

    class Meta:
        db_table = 'image_urls'

class Allergy(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        db_table = 'allergies'

class Products_allergy(models.Model):
    allergy_id  = models.ForeignKey('Allergy', on_delete=models.CASCADE)
    product_id  = models.ForeignKey('Product', on_delete=models.CASCADE)

    class Meta:
        db_table = 'products_allergies'
