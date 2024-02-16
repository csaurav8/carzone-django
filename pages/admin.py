from django.contrib import admin
from .models import Team
from django.utils.html import format_html

class TeamAdmin(admin.ModelAdmin):

    list_display = ('id', 'photo_thumbnail', 'first_name', 'designation', 'created_at')
    list_display_links = ('id', 'first_name')
    list_filter = ('designation',)
    search_fields = ('first_name', 'last_name', 'designation')

    def photo_thumbnail(self, obj):
        if obj.photo:
            return format_html('<img src="{}" style="border-radius: 50%; width: 50px; height: 50px;" />'.format(obj.photo.url))
        else:
            return format_html('<p>No photo</p>')

    photo_thumbnail.short_description = 'Photo'

# Register your models here.
admin.site.register(Team, TeamAdmin)
