# Generated by Django 4.2.1 on 2023-07-15 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0010_i_b_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='i_b_data',
            name='exp_date',
            field=models.CharField(max_length=25, null=True),
        ),
    ]