from django.db import models
import datetime
#date = models.DateField(_("Date"), default=datetime.date.today)
class GitCours(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    date = models.DateField(default=datetime.date.today)
    author = models.CharField(max_length=120,default=None)
    link = models.URLField(max_length=120,default=None)
    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

class LinuxCours(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    date = models.DateField(default=datetime.date.today)
    author = models.CharField(max_length=120,default=None)
    link = models.URLField(max_length=120,default=None)
    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title



class PyCours(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    date = models.DateField(default=datetime.date.today)
    author = models.CharField(max_length=120,default=None)
    link = models.URLField(max_length=120,default=None)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title


class JsCours(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    date = models.DateField(default=datetime.date.today)
    author = models.CharField(max_length=120,default=None)
    link = models.URLField(max_length=120,default=None)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title


class JqCours(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    date = models.DateField(default=datetime.date.today)
    author = models.CharField(max_length=120,default=None)
    link = models.URLField(max_length=120,default=None)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title


class MyCours(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    date = models.DateField( default=datetime.date.today)
    author = models.CharField(max_length=120,default=None)
    link = models.URLField(max_length=120,default=None)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title
