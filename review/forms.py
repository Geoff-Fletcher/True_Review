from django import forms
from .models import MovieReview

class MovieReviewForm(forms.ModelForm):
    class Meta:
        model = MovieReview
        fields = ['featured_image', 'title', 'rating', 'slug', 'review_text', 'release_date', 'runtime', 'director']