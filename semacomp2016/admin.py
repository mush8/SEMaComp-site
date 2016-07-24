from django.contrib import admin
from .models import (Post, SessionCategory, Session,
                    Speaker, Sponsor, Attendee)

# Register your models here.
admin.site.register(Post)
admin.site.register(SessionCategory)
admin.site.register(Session)
admin.site.register(Speaker)
admin.site.register(Sponsor)
admin.site.register(Attendee)
