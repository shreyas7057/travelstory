from django.db import models

from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model

User = get_user_model()

class Story(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    story_title = models.CharField(max_length=200)
    place_name = models.CharField(max_length=200)
    city_name = models.CharField(max_length=250)
    thumbnail = models.ImageField(upload_to='thumbnails/',blank=True,null=True)
    photos = models.ImageField(upload_to='photos/',blank=True,null=True)
    # questions
    nearby_places = models.CharField(max_length=200)
    food_to_try = models.CharField(max_length=200)
    precautions = models.CharField(max_length=200)
    things_to_try = models.CharField(max_length=200)
    visit_season = models.CharField(max_length=200)
    trip_highlights = models.TextField()
    brief_summary = RichTextField()