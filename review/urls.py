from django.urls import path
from review import views

urlpatterns = [
    path('', views.index, name='index'),
    path('review/create/', views.create_movie_review, name="create_moviereview"),
    path('review/edit/<movie_review_id>', views.edit_movie_review, name="edit_moviereview"),
    path('reviews/<review_id>/', views.review_detail, name="review_detail"),
]
