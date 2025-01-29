from django.contrib import admin
from .models import  Profile, Memorial, Tag, Photo, Message


admin.site.register(Profile)
admin.site.register(Memorial)
admin.site.register(Tag)
admin.site.register(Photo)
admin.site.register(Message)

