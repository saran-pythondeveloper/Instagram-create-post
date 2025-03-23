from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image', 'video']
        image = forms.ImageField(label="Upload Image", required=False, widget=forms.ClearableFileInput(attrs={'class': 'form-control'}))
        video = forms.FileField(label="Upload Video", required=False, widget=forms.ClearableFileInput(attrs={'class': 'form-control'}))
        caption = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write a caption...', 'rows': 4}), required=False)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
