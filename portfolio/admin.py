from django.contrib import admin

from .models import *

class MediaInline(admin.StackedInline):
    fieldsets = [
        (None, {'fields':['media', 'alttext', 'order']})
    ]
    model = Media
    extra = 1

class EmbedInline(admin.StackedInline):
        fieldsets = [
            (None, {'fields':['src']})
        ]
        model = Embed
        extra = 1

class BulletInline(admin.StackedInline):
    fieldsets = [
        (None, {'fields':['text']})
    ]
    model = Bullet
    extra = 1

class ResumeItemAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields':['title', 'company', 'start_date', 'end_date']})
    ]
    inlines = [BulletInline]

class CodingProjectAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields':['order','title', 'tagline', 'text','technologies','project_link','project_link_display_text']})
    ]
    inlines = [MediaInline]

class GalleryAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields':['title']})
    ]
    inlines = [EmbedInline, MediaInline]

admin.site.register(ResumeItem, ResumeItemAdmin)
admin.site.register(CodingProject, CodingProjectAdmin)
admin.site.register(Gallery, GalleryAdmin)
