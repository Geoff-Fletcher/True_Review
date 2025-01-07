from django.contrib import admin
from .models import MovieReview, TVReview, GameReview, Comment

# Full admin setup for MovieReview
@admin.register(MovieReview)
class MovieReviewAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'rating', 'status', 'created_on', 'release_date', 'director', 'runtime')
    list_filter = ('status', 'created_on', 'release_date', 'rating')
    search_fields = ('title', 'author__username', 'director')
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = (
        ('Basic Info', {
            'fields': ('title', 'slug', 'author', 'category', 'status', 'featured_image')
        }),
        ('Review Details', {
            'fields': ('review_text', 'rating', 'release_date')
        }),
        ('Movie-Specific Details', {
            'fields': ('director', 'runtime')
        }),
    )

# Full admin setup for TVReview
@admin.register(TVReview)
class TVReviewAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'rating', 'status', 'created_on', 'release_date', 'showrunner', 'number_of_episodes', 'average_episode_length')
    list_filter = ('status', 'created_on', 'release_date', 'rating')
    search_fields = ('title', 'author__username', 'showrunner')
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = (
        ('Basic Info', {
            'fields': ('title', 'slug', 'author', 'category', 'status', 'featured_image')
        }),
        ('Review Details', {
            'fields': ('review_text', 'rating', 'release_date')
        }),
        ('TV-Specific Details', {
            'fields': ('showrunner', 'number_of_episodes', 'average_episode_length')
        }),
    )

# Full admin setup for GameReview
@admin.register(GameReview)
class GameReviewAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'rating', 'status', 'created_on', 'release_date', 'studio', 'time_to_beat', 'number_of_players')
    list_filter = ('status', 'created_on', 'release_date', 'rating')
    search_fields = ('title', 'author__username', 'studio')
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = (
        ('Basic Info', {
            'fields': ('title', 'slug', 'author', 'category', 'status', 'featured_image')
        }),
        ('Review Details', {
            'fields': ('review_text', 'rating', 'release_date')
        }),
        ('Game-Specific Details', {
            'fields': ('studio', 'time_to_beat', 'number_of_players')
        }),
    )

# Admin setup for Comment
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'rating', 'approved', 'created_on')
    list_filter = ('approved', 'created_on', 'rating')
    search_fields = ('author__username', 'post__title', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
    approve_comments.short_description = "Mark selected comments as approved"


