from __future__ import unicode_literals

from django.db import models


class Blogs(models.Model):
    title = models.CharField(max_length=100, unique=True)
    body = models.TextField()
    posted = models.DateField(db_index=True, auto_now_add=True)
    postedby=models.CharField(max_length=100, unique=True)
    category = models.ForeignKey('blog.Categories')

    def __unicode__(self):
        return '%s' % self.title

class Categories(models.Model):
    title = models.CharField(max_length=100, db_index=True)
