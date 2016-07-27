from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class Post(models.Model):

    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Sponsor(models.Model):

    SPONSOR_LEVEL_PRATA = 1
    SPONSOR_LEVEL_OURO = 2
    SPONSOR_LEVEL_DIAMANTE = 3
    SPONSOR_LEVELS = [
        (0, _(u"")),
        (SPONSOR_LEVEL_PRATA, _(u"Prata")),
        (SPONSOR_LEVEL_OURO, _(u"Ouro")),
        (SPONSOR_LEVEL_DIAMANTE, _(u"Diamante")),
    ]

    title = models.CharField(max_length=200, default="", blank=False)
    sponsor_level = models.IntegerField(default=0,
        choices=SPONSOR_LEVELS)
    institution_url = models.URLField(max_length=500, default="", blank=False)
    text = models.TextField()
    image = models.ImageField(upload_to = 'semacomp2016/static/img/sponsor/', )
    image_url = '../../static/img/sponsor/'

class Speaker(models.Model):

    title = models.CharField(max_length=200, default="", blank=False)
    institution = models.CharField(max_length=200, default="", blank=False)
    text = models.TextField()
    image_url = models.URLField(max_length=500, default="", blank=False)
    email = models.CharField(max_length=100, default="", blank=False)

    def __str__(self):
        return self.name

class Session(models.Model):

    AUDIENCE_LEVEL_NOVICE = 1
    AUDIENCE_LEVEL_INTERMEDIATE = 2
    AUDIENCE_LEVEL_EXPERIENCED = 3
    AUDIENCE_LEVELS = [
        (AUDIENCE_LEVEL_NOVICE, _(u"Novato")),
        (AUDIENCE_LEVEL_INTERMEDIATE, _(u"Intermediário")),
        (AUDIENCE_LEVEL_EXPERIENCED, _(u"Experiente")),
    ]
    audience_level = models.IntegerField(default=1,
        choices=AUDIENCE_LEVELS)

    SESSION_CATEGORY_TRAINING = 1
    SESSION_CATEGORY_TALK = 2
    SESSION_CATEGORY_COMPETITION = 3
    SESSION_CATEGORIES = [
        (SESSION_CATEGORY_TRAINING, _(u"Workshop")),
        (SESSION_CATEGORY_TALK, _(u"Palestra")),
        (SESSION_CATEGORY_COMPETITION, _(u"Competição")),
    ]
    session_category = models.IntegerField(default=1,
        choices=SESSION_CATEGORIES)

    speaker = models.ForeignKey(Speaker, on_delete=models.CASCADE)
    title = models.CharField(max_length=400, default="", blank=True)
    text = models.TextField()

    start = models.DateTimeField()
    end = models.DateTimeField()

    def __str__(self):
        return self.name
