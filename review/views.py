from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from.models import MovieReview, TVReview, GameReview, CommonReviewData
from.forms import MovieReviewForm, CommentForm


def review_detail(request, review_id):
    # allow user to see an individual reviews contents when they click on it
    requested_review = get_object_or_404(CommonReviewData, id = review_id)
    print('review == ', requested_review)

    context = {
        "review": requested_review,
    }

    return render(request, 'review/review_detail.html', context)

def index(request):
    # Combine reviews using only the common fields
    movie_reviews = MovieReview.objects.filter(status = 1).values(
    'id', 'title', 'author', 'slug', 'featured_image', 'rating',
    'release_date', 'created_on', 'category'
    )
    tv_reviews = TVReview.objects.filter(status = 1).values(
    'id', 'title', 'author', 'slug', 'featured_image', 'rating', 'release_date', 'created_on', 'category'
    )
    game_reviews = GameReview.objects.filter(status = 1).values(
    'id', 'title', 'author', 'slug', 'featured_image', 'rating', 'release_date', 'created_on', 'category'
    )

# Combine all reviews and sort by creation date
    reviews = sorted(
    list(movie_reviews) + list(tv_reviews) + list(game_reviews),
    key = lambda x: x['created_on'], reverse = True
    )

# Paginate the combined reviews
    paginator = Paginator(reviews, 6) # Show 6 reviews per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

# Pass the paginated reviews to the template
    context = {
        'post_list': page_obj,
        'page_obj': page_obj,
        'is_paginated': page_obj.has_other_pages(),
    }
    return render(request, 'review/index.html', context)

def create_movie_review(request):
    # creates template for viewer to add their own editable movie review to the site
    if request.method == "POST":
        movie_review_form = MovieReviewForm(request.POST)
        if movie_review_form.is_valid():
            movie_review = movie_review_form.save(commit=False)
            movie_review.author = request.user
            movie_review_form.save()
            messages.success(request, "Review created successfully!")
        else:
            print(movie_review_form.errors)
        return redirect('index')
    else: 
         movie_review_form = MovieReviewForm()

    context = {
    "form": movie_review_form,
    }

    return render(request, 'review/create_moviereview.html', context)


def edit_movie_review(request, movie_review_id):
    movie_review = get_object_or_404(MovieReview, id=movie_review_id)
    # creates template for viewer to add their own editable movie review to the site
    if request.method == "POST":
        movie_review_form = MovieReviewForm(request.POST, instance=movie_review)
        if movie_review_form.is_valid():
            movie_review = movie_review_form.save(commit=False)
            movie_review.author = request.user
            movie_review_form.save()
            messages.success(request, "Review updated successfully!")
        else:
            print(movie_review_form.errors)
        return redirect('index')
    else: 
         movie_review_form = MovieReviewForm(instance=movie_review)

    context = {
    "form": movie_review_form,
    }
    return render(request, 'review/edit_moviereview.html', context)




def comment_edit(request, slug, comment_id):
  
      # Fetch the corresponding CommonReviewData post
    queryset = CommonReviewData.objects.filter(status=1)  # Only published reviews
    post = get_object_or_404(queryset, slug=slug)

    # Fetch the comment by ID
    comment = get_object_or_404(Comment, pk=comment_id)

    # Check if the request is a POST
    if request.method == "POST":
        # Bind the comment form with data
        comment_form = CommentForm(data=request.POST, instance=comment)

        # Check if the form is valid and the author is the logged-in user
        if comment_form.is_valid() and comment.author == request.user:
            # Save the comment
            updated_comment = comment_form.save(commit=False)
            updated_comment.post = post
            updated_comment.approved = False  # Mark as unapproved until reviewed
            updated_comment.save()

            # Add a success message
            messages.add_message(request, messages.SUCCESS, 'Comment updated!')
        else:
            # Add an error message if validation fails
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

        # Redirect back to the same page or slug URL
        return HttpResponseRedirect(reverse('some_view_name', args=[slug]))

    # If not a POST request, render the page as usual (optional)
    return redirect('some_view_name', slug=slug)


def comment_delete(request, slug, comment_id):
    
    # Fetch the corresponding CommonReviewData post
    queryset = CommonReviewData.objects.filter(status=1)  # Only published reviews
    post = get_object_or_404(queryset, slug=slug)

    # Fetch the comment by ID
    comment = get_object_or_404(Comment, pk=comment_id)

    # Ensure the comment can only be deleted by the author
    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    # Redirect back to the same page or slug URL
    return HttpResponseRedirect(reverse('some_view_name', args=[slug]))

# Create your views here.

