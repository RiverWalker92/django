from django.db import models
from datetime import datetime
from tinymce.models import HTMLField


class Layout(models.Model):
    title_id = models.CharField(max_length=255, null=False, blank=True, unique=True)
    main_title = models.CharField(max_length=255, null=True, blank=True)
    sub_title = models.CharField(max_length=255, null=True, blank=True)
    icon = models.CharField(max_length=255, null=True, blank=True, default="fa fa-play")
    url = models.URLField(max_length=255, null=True, blank=True)
    text_block = HTMLField(max_length=5000, null=True, blank=True)

class Content(models.Model):
    title_id = models.CharField(max_length=255, null=True, blank=True)
    main_title = models.CharField(max_length=255, null=True, blank=True)
    sub_title = models.CharField(max_length=255, null=True, blank=True)

class SmallContent(models.Model):
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, null=False, blank=True, unique=True)
    text_block = models.TextField(max_length=5000, null=True, blank=True)
    icon = models.CharField(max_length=255, null=True, blank=True)
    #price = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True )
    #photo = models.ImageField(upload_to='team', null=True, blank=True)
    def fade_in_time(self):
        return self.pk * 0.3

class TeamMember(models.Model):
    main_title = models.CharField(max_length=255, null=False, blank=False, unique=True)
    sub_title = models.CharField(max_length=255, null=True, blank=True)
    icon1 = models.CharField(max_length=255, null=True, blank=True, default="fa fa-facebook")
    url1 = models.URLField(max_length=255, null=True, blank=True)
    icon2 = models.CharField(max_length=255, null=True, blank=True, default="fa fa-twitter")
    url2 = models.URLField(max_length=255, null=True, blank=True)
    icon3 = models.CharField(max_length=255, null=True, blank=True, default="fa fa-linkedin")
    url3 = models.URLField(max_length=255, null=True, blank=True)
    #price = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True )
    photo = models.ImageField(upload_to='team', null=True, blank=True)
    def fade_in_time(self):
        return self.pk * 0.3
