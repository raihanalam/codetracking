from django import forms
from django.forms import fields
from .models import Blog, Comment

class CommentForm(forms.ModelForm):
     class Meta:
          model = Comment
          fields = ('comment',) 