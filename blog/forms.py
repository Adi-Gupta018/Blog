from django import forms

from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        exclude = ["post"]
        labels={
            "user_name":"Name",
            "user_email":"Email",
            "text":"Comment"
        }
        error_messages = {
            "user_name":{
                "required":"Your name can't be blank",
                "max_length":"Please enter a shoter name"
            }
        }