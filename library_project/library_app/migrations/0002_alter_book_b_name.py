# Generated by Django 4.2.1 on 2023-05-09 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='B_name',
            field=models.CharField(max_length=60),
        ),
    ]
