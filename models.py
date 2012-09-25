from django.db import models

# Create your models here.
from cms.models import CMSPlugin

class AlohaFieldPlugin(CMSPlugin):
    body = models.TextField('body')

    def __unicode__(self):
        return u'%s' % (self.body,)
