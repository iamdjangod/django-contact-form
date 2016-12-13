from __future__ import unicode_literals

from django.db import models

# Create your models here.



class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=128)

    def __unicode__(self):
        return "{0} {1} {2}".format(
            self, self.name, self.email)