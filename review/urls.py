from django.urls import path
from review import views

urlpatterns = [
    path('', views.index, name='index'),
    ##path('review/create/', review_views.create_moviereview, name="create_moviereview"),
    path('reviews/<review_id>/', views.review_detail, name="review_detail"),
]
