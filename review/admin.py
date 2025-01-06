from django.contrib import admin
from .models import Category, MovieReview, TVReview, GameReview

# Base class for common review fields
class CommonReviewAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "rating", "status", "created_on")
    search_fields = ("title", "author__username", "slug")
    list_filter = ("status", "created_on", "release_date")
    ordering = ["-created_on"]
    readonly_fields = ("created_on",)  # Make created_on read-only

# MovieReview admin
@admin.register(MovieReview)
class MovieReviewAdmin(CommonReviewAdmin):
    fieldsets = (
        (None, {
            'fields': (
                'author', 'featured_image', 'title', 'slug', 'review_text',
                'release_date', 'rating', 'status', 'created_on',  # Read-only
                'runtime', 'director', 'category'
            )
        }),
    )

# TVReview admin
@admin.register(TVReview)
class TVReviewAdmin(CommonReviewAdmin):
    fieldsets = (
        (None, {
            'fields': (
                'author', 'featured_image', 'title', 'slug', 'review_text',
                'release_date', 'rating', 'status', 'created_on',  # Read-only
                'number_of_episodes', 'showrunner', 'average_episode_length', 
                'category'
            )
        }),
    )

# GameReview admin
@admin.register(GameReview)
class GameReviewAdmin(CommonReviewAdmin):
    fieldsets = (
        (None, {
            'fields': (
                'author', 'featured_image', 'title', 'slug', 'review_text',
                'release_date', 'rating', 'status', 'created_on',  # Read-only
                'studio', 'time_to_beat', 'number_of_players', 'category'
            )
        }),
    )

# Register Category separately
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
