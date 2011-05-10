#encoding: utf-8

from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    user = models.OneToOneField(User)

    def __unicode__(self):
        return 'Conta: %s' % self.name
