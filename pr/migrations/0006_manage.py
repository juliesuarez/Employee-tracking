# Generated by Django 4.2.7 on 2023-11-28 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pr', '0005_educationdetail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_car', models.CharField(max_length=100)),
                ('number_plate', models.CharField(max_length=50)),
                ('color_of_car', models.CharField(max_length=50)),
                ('ownership', models.CharField(max_length=100)),
                ('name_of_driver', models.CharField(max_length=50)),
            ],
        ),
    ]