from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        # model指定了表单要显示的字段
        model = Comment
        fields = ['name','email','url','text']