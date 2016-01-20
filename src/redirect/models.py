from __future__ import unicode_literals

from django.db import models
import md5

# Create your models here.


def _md5(text):
    m = md5.new()
    m.update(text)
    return m.hexdigest()



class Redirect(models.Model):
    name = models.CharField(max_length=255)
    short = models.CharField(unique=True, max_length=255, blank=True)
    url = models.URLField()

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.short:
            self.short = _md5(self.url)[:6]

        super(Redirect, self).save(*args, **kwargs)


class ClickLog(models.Model):
    url = models.ForeignKey(Redirect, null=True)
    ip = models.GenericIPAddressField()

    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.created
