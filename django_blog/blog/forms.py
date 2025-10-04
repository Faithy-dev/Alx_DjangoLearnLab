# blog/forms.py

from django import forms
from .models import Post, Comment, Tag


# Custom TagWidget class
class TagWidget(forms.TextInput):
    def __init__(self, attrs=None):
        default_attrs = {"class": "form-control", "placeholder": "Enter tags separated by commas"}
        if attrs:
            default_attrs.update(attrs)
        super().__init__(attrs=default_attrs)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content", "tags"]

        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "content": forms.Textarea(attrs={"class": "form-control"}),
            "tags": TagWidget(),   # ✅ Using TagWidget here
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
