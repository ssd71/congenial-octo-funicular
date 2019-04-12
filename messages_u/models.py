from django.db import models
from django.forms import ModelForm

# Create your models here.

class Message(models.Model):
    by_username = models.TextField(blank = False)
    sentence = models.TextField(blank = False)
    verb = models.TextField(blank = False)

class MessageForm(ModelForm):
    class Meta:
        model = Message
        exclude = ['by_username']
