from django.contrib import admin

# Register your models here.
from .models import AudioFile, AudioAlteration

admin.site.register( AudioFile )
admin.site.register( AudioAlteration )
