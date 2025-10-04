# blog/forms.py

from django import forms
from .models import Post, Comment, Tag


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content", "tags"]

        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "content": forms.Textarea(attrs={"class": "form-control"}),
            # Added TagWidget
            "tags": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter tags separated by commas",
                }
            ),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]

        widgets = {
            "content": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                    "placeholder": "Write your comment here...",
                }
            ),
        }


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ["name"]

        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Tag name"}
            ),
        }
