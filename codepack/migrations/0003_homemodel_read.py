# Generated by Django 3.0.7 on 2021-08-07 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codepack', '0002_author_category_homemodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='homemodel',
            name='read',
            field=models.IntegerField(default=0),
        ),
    ]
