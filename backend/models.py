from enum import unique
from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from django.forms import CharField
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
class Topic(models.Model):
    id=models.IntegerField(primary_key=True)
    title=models.CharField(max_length=255)
    description=models.CharField(max_length=500)
    image=models.URLField(max_length=200,default=None)
    wide_image=models.URLField(max_length=200,default=None)
    def __str__(self)->str:
        return str(self.id)+'.  '+self.title

class Choice(models.Model):
    class Meta:
        unique_together=(('topic','option_no'))
    id=models.IntegerField(primary_key=True)
    topic=models.ForeignKey(Topic,on_delete=models.CASCADE)
    option_no=models.IntegerField(default=0)
    option=models.CharField(max_length=55)
    count=models.IntegerField(default=0)
    def __str__(self)->str:
        return str(self.id)+'.  '+self.option+'  '+str(self.topic)

class Reaction(models.Model):
    class Meta:
        unique_together=(('user','choice','topic'))
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    choice=models.ForeignKey(Choice,on_delete=models.CASCADE)
    topic=models.ForeignKey(Topic,on_delete=models.CASCADE)
    time=models.DateTimeField()

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    uname=models.CharField(max_length=30,primary_key=True)
    
class Comment(models.Model):
   id=models.AutoField(primary_key=True)
   user=models.ForeignKey(Profile,on_delete=models.CASCADE,unique=False)
   topic=models.ForeignKey(Topic,on_delete=models.CASCADE,unique=False)
   body=models.CharField(max_length=255)

'''
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
'''

