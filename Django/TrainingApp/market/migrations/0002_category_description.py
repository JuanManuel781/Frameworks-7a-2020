# Generated by Django 3.1.1 on 2020-10-29 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='description',
            field=models.TextField(default=''),
        ),
    ]