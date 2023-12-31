# Generated by Django 3.1.2 on 2023-06-04 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, verbose_name='Наименование модели')),
                ('price', models.IntegerField(verbose_name='Стоимость')),
                ('image', models.ImageField(upload_to='')),
                ('release_date', models.DateField()),
                ('lte_exists', models.BooleanField()),
                ('slug', models.SlugField(unique=True, verbose_name='URL')),
            ],
        ),
    ]
