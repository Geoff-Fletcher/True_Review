from . import views
from django.urls import path

urlpatterns = [
    path("", include("review.urls"), name="review-urls"),
  
]