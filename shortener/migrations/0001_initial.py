# Generated by Django 2.1.7 on 2019-04-05 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Links',
            fields=[
                ('short_link', models.SlugField(max_length=6, primary_key=True, serialize=False)),
                ('httpurl', models.URLField(max_length=264)),
            ],
        ),
    ]
