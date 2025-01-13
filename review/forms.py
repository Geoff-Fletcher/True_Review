from django import forms
from .models import MovieReview, Comment, CommonReviewData


class MovieReviewForm(forms.ModelForm):
    class Meta:
        model = MovieReview
        fields = ['featured_image', 'title', 'rating', 'review_text',
                  'release_date', 'runtime', 'director']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body', 'rating')
