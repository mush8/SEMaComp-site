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

    institution = models.CharField(max_length=200)
    text = models.TextField()
    image_url = models.URLField(max_length=500, blank=False)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.institution

class Attendee(models.Model):

    name = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    text = models.CharField(
        max_length=60, blank=True,
        help_text=_('descreva-se em uma linha!'))
    paid = models.BooleanField(default=False)
    image_gravatar = models.BooleanField(default=False)
    image_url = models.URLField(max_length=500, blank=False)
    spam_recruiting = models.BooleanField(default=False)

    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name

class Speaker(Attendee):

    # session = models.ForeignKey(Session, on_delete=models.CASCADE)
    pass

class SessionCategory(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = "Categoria de sessão da SEMaComp"
        verbose_name_plural = "Categorias de sessões da SEMaComp"

class Session(models.Model):

    AUDIENCE_LEVEL_NOVICE = 1
    AUDIENCE_LEVEL_INTERMEDIATE = 2
    AUDIENCE_LEVEL_EXPERIENCED = 3
    AUDIENCE_LEVELS = [
        (0, _(u"")),
        (AUDIENCE_LEVEL_NOVICE, _(u"Novato")),
        (AUDIENCE_LEVEL_INTERMEDIATE, _(u"Intermediário")),
        (AUDIENCE_LEVEL_EXPERIENCED, _(u"Experiente")),
    ]

    category = models.ForeignKey(SessionCategory)
    speaker = models.ForeignKey(Speaker)
    text = models.TextField()
    audience_level = models.IntegerField(default=0,
        choices=AUDIENCE_LEVELS)

    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name
