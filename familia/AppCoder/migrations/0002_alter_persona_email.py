# Generated by Django 4.1.2 on 2022-10-25 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='email',
            field=models.EmailField(max_length=50),
        ),
    ]