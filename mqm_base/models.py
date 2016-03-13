from __future__ import unicode_literals

from django.db import models
from django.conf import settings


class Locale(models.Model):
    code = models.CharField(max_length=30, unique=True)
    name = models.CharField(max_length=100, blank=True, null=True)

    def __unicode__(self):
        if self.name:
            return '%s (%s)' % (self.name, self.code)
        else:
            return self.code


class Issue(models.Model):
    locale = models.ForeignKey(Locale, related_name='issues')
    file = models.TextField()
    identifier = models.TextField()
    original = models.TextField()
    before = models.TextField()
    after = models.TextField()


class MQMType(models.Model):
    mqmid = models.CharField(max_length=50, db_index=True)
    classification = models.CharField(max_length=50)

class Rating(models.Model):
    issue = models.ForeignKey(Issue, related_name='ratings')
    mqm_type = models.ForeignKey(MQMType)
    rater = models.ForeignKey(settings.AUTH_USER_MODEL)
