#encoding: utf-8
from django.db import models
from flavyoutube.apps.account import models as account_models

class Video(models.Model):
    id = models.AutoField(primary_key=True)
    owner = models.ForeignKey(account_models.User, verbose_name="Proprietário")
    description = models.TextField(u"Descrição", blank=True)
    screenshot = models.FileField(upload_to="videos/screenshots/")
    video = models.FileField(upload_to="videos/")

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)
