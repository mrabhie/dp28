from django.contrib import admin

# Register your models here.from django.contrib import admin
from dp28app import models

class TopicAdminView(admin.ModelAdmin):
    list_display=('topic_name',)
    search_fields=('topic_name',)
    
class WebPageAdminView(admin.ModelAdmin):
    list_display=('topic','name','url')
    search_fields=('name',)
    list_editable=('name',)
    list_filter=('topic',)

class AccessDetailsAdminView(admin.ModelAdmin):
    list_display=('webpage','datetime')

admin.site.register(models.Topic,TopicAdminView)
admin.site.register(models.WebPage,WebPageAdminView)
admin.site.register(models.AccessDetails,AccessDetailsAdminView)