from django.urls import path
from review import views

urlpatterns = [
    path('', views.index, name='index'),
    path('review/create/', views.create_movie_review,
         name="create_moviereview"),
    path('review/edit/<int:movie_review_id>',
         views.edit_movie_review, name="edit_moviereview"),
    path('review/delete/<int:movie_review_id>',
         views.delete_movie_review, name="delete_moviereview"),
    path('reviews/<review_id>/', views.review_detail, name="review_detail"),
    path('reviews/<int:review_id>/edit_comment/<int:comment_id>/', views.comment_edit, name='comment_edit'),
    path('reviews/<int:review_id>/delete_comment/<int:comment_id>/', views.comment_delete, name='comment_delete'),
]
