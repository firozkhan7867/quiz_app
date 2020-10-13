from django.contrib import admin

# Register your models here.

from .models import Participants


class ParticipantsAdmin(admin.ModelAdmin):
    list_display = ('f_name', 'l_name', 'email','score')
    list_display_links = ('f_name', 'email')
    list_filter = ('score',)

admin.site.register(Participants,ParticipantsAdmin)
