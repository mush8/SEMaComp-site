from django.contrib import admin
from .models import Post, Session, Speaker, Sponsor

# Register your models here.
admin.site.register(Post)
admin.site.register(Session)
admin.site.register(Speaker)
admin.site.register(Sponsor)
