from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    @staticmethod
    def film_category():
        return Category.objects.get(name="Film")

    @staticmethod
    def tv_category():
        return Category.objects.get(name="TV Series")

    @staticmethod
    def game_category():
        return Category.objects.get(name="Video Game")


class CommonReviewData(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    featured_image = CloudinaryField('image', default='placeholder')
    title = models.CharField(max_length=100)
    rating = models.IntegerField(validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ])
    slug = models.SlugField(max_length=200, unique=True)   
    review_text = models.TextField()
    release_date = models.DateField()
    status = models.IntegerField(choices=STATUS, default=0)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"{self.title} | written by {self.author}, {self.created_on}"


class MovieReview(CommonReviewData):
    runtime = models.DurationField()
    director = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, default=Category.film_category)

class TVReview(CommonReviewData):
    number_of_episodes = models.IntegerField()
    showrunner = models.CharField(max_length=100)
    average_episode_length = models.DurationField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, default=Category.tv_category)

class GameReview(CommonReviewData):
    studio = models.CharField(max_length=100)
    time_to_beat = models.DurationField()
    number_of_players = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, default=Category.game_category)


class Comment(models.Model):
    post = models.ForeignKey(
    CommonReviewData, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    rating = models.IntegerField(validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ])
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
            return f"{self.body} | written by {self.author}"