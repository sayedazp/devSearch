from django.contrib import admin
from .models import Skill, Profile
# Register your models here.
admin.site.register([Profile, Skill])