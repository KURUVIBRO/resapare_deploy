from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ['id' ,'title','description','image','wide_image']
    list_editable = ['title','description','image','wide_image']

@admin.register(models.Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display=['id','topic','option_no','option','count']
    list_editable=['option_no','option']

@admin.register(models.Reaction)
class ReactionAdmin(admin.ModelAdmin):
    list_display=['time','user','choice']

@admin.register(models.Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display=['user','uname']

@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display=['id','user','topic','body']
