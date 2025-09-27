from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'sport_category']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter post title...'}),
            'content': forms.Textarea(attrs={'placeholder': 'Share your thoughts...', 'rows': 5}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'placeholder': 'Write your comment...', 
                'rows': 3,
                'style': 'width: 100%;'
            }),
        }
        labels = {
            'content': 'Your Comment',
        }