# Generated by Django 5.0.2 on 2024-02-15 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teams',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('designation', models.CharField(max_length=50)),
                ('photo', models.ImageField(upload_to='photos/%y/%m/%d')),
                ('facebook_link', models.URLField(max_length=255)),
                ('twitter_link', models.URLField(max_length=255)),
                ('google_plus_link', models.URLField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
