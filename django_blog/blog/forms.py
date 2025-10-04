from django import forms
from .models import Post, Comment, Tag

class PostForm(forms.ModelForm):
    tags = forms.CharField(
        required=False,
        help_text="Enter tags separated by commas",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def save(self, commit=True, *args, **kwargs):
        post = super().save(commit=False)
        if commit:
            post.save()
            tags_list = [t.strip() for t in self.cleaned_data['tags'].split(",") if t.strip()]
            post.tags.clear()
            for tag_name in tags_list:
                tag, created = Tag.objects.get_or_create(name=tag_name)
                post.tags.add(tag)
        return post


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']
