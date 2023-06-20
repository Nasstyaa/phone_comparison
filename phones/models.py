from django.db import models

# Create your models here.
class Phone(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=50, verbose_name="Наименование модели")
  price = models.IntegerField(verbose_name="Стоимость")
  image = models.ImageField()
  release_date = models.DateField()
  lte_exists = models.BooleanField()
  slug = models.SlugField(max_length=50, unique=True, verbose_name="URL")
