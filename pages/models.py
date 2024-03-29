from django.db import models

# Create your models here.
class Team(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    designation = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='photos/%y/%m/%d')
    facebook_link = models.URLField(max_length=255)
    twitter_link = models.URLField(max_length=255)
    linkedin_link = models.URLField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name