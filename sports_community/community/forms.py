from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'sport_category']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter post title...'}),
            'content': forms.Textarea(attrs={'placeholder': 'Share your thoughts...', 'rows': 5}),
        }