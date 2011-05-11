#encoding: utf-8
from django.db import models
from django.contrib.auth.models import User

class Video(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name="Nome")
    owner = models.ForeignKey(User, verbose_name="Proprietário")
    description = models.TextField(u"Descrição", blank=True)
    screenshot = models.FileField(upload_to="videos/screenshots/")
    video_path = models.CharField(max_length=400, blank=True)

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)

    def link(self):
        return "/media/videos" + self.video_path[self.video_path.rindex("/"):]
    def __unicode__(self):
        return "Video: %s" % (self.name)
