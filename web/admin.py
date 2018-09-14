from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Data, Tag, Report

admin.site.site_header = 'مدیریت لام'
admin.site.site_title = 'مدیریت لام'
admin.site.index_title = 'مدیریت لام'

admin.site.unregister(Group)


@admin.register(Data)
class DataAdmin(admin.ModelAdmin):
    readonly_fields = ('pid', 'jalali_updated_on', 'jalali_created_on')
    fieldsets = [
        ('اطلاعات اصلی', {'fields': ['pid', 'title', 'subtitle', 'content', 'event', 'image', 'image_caption']}),
        ('اطلاعات تکمیلی', {'fields': ['tag', 'reference', 'author', 'is_active']}),
        ('تاریخ‌ها', {'fields': ['jalali_updated_on', 'jalali_created_on']}),
    ]
    list_display = ('title', 'author', 'is_active', 'jalali_updated_on', 'jalali_created_on')
    list_filter = ['author', 'is_active', 'updated_on', 'created_on']
    search_fields = ['title', 'content', 'event', 'image_caption', 'tag']


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    readonly_fields = ('data', 'jalali_updated_on', 'jalali_created_on')
    fieldsets = [
        ('اطلاعات اصلی', {'fields': ['body', 'reporter', 'status']}),
        ('تاریخ‌ها', {'fields': ['jalali_updated_on', 'jalali_created_on']}),
    ]
    list_display = ('data', 'reporter', 'status', 'jalali_updated_on', 'jalali_created_on')
    list_filter = ['reporter', 'status', 'updated_on', 'created_on']
    search_fields = ['data', 'body', 'reporter']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    readonly_fields = ('keyword', 'jalali_updated_on', 'jalali_created_on')
    fieldsets = [
        ('اطلاعات اصلی', {'fields': ['name', 'keyword', 'is_active']}),
        ('تاریخ‌ها', {'fields': ['jalali_updated_on', 'jalali_created_on']}),
    ]
    list_display = ('name', 'keyword', 'is_active', 'jalali_updated_on', 'jalali_created_on')
    list_filter = ['is_active', 'updated_on', 'created_on']
    search_fields = ['name', 'keyword']