from django.contrib import admin
from .models import Category
from .models import CommonReviewData
from .models import TVReview
from .models import MovieReview
from .models import GameReview

admin.site.register(Category)
admin.site.register(CommonReviewData)
admin.site.register(TVReview)
admin.site.register(MovieReview)
admin.site.register(GameReview)

# Register your models here.
