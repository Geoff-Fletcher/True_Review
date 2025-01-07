from django.core.paginator import Paginator
from django.shortcuts import render
from .models import MovieReview, TVReview, GameReview

def index(request):
    # Combine all reviews into a single queryset
    reviews = (
        MovieReview.objects.filter(status=1)
        .union(TVReview.objects.filter(status=1))
        .union(GameReview.objects.filter(status=1))
        .order_by('-created_on')  # Sort by creation date (newest first)
    )

    # Paginate the combined queryset
    paginator = Paginator(reviews, 9)  # Show 9 reviews per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Pass the paginated reviews to the template
    context = {
        'post_list': page_obj,
        'page_obj': page_obj,
        'is_paginated': page_obj.has_other_pages(),
    }
    return render(request, 'index.html', context)


"""def comment_edit(request, slug, comment_id):
    
    if request.method == "POST":

        queryset = CommonReviewData.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

    if comment_form.is_valid() and comment.author == request.user:
        comment = comment_form.save(commit=False)
        comment.post = post
        comment.approved = False
        comment.save()
        messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
    else:
        messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))

def comment_delete(request, slug, comment_id):
    
    view to delete comment
    
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))

# Create your views here."""
