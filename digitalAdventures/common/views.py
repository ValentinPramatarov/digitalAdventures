from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from digitalAdventures.common.forms import PostCommentForm, SearchGamesForm
from digitalAdventures.posts.models import ImagePost
from core.utils import get_post_url


def index(request):
    search_form = SearchGamesForm(request.GET)
    search_pattern = None
    if search_form.is_valid():
        search_pattern = search_form.cleaned_data['game_name']

    posts = ImagePost.objects.all()
    if search_pattern:
        posts = posts.filter(game__name__icontains=search_pattern)

    for post in posts:
        if request.user.is_authenticated:
            post.has_user_like_photo = request.user in post.liked_by.all()
        else:
            post.has_user_like_photo = False

    context = {
        'posts': posts,
        'comment_form': PostCommentForm(),
        'search_form': search_form,
    }

    return render(request, 'common/index.html', context)


@login_required
def like_post(request, pk):
    post = ImagePost.objects.get(pk=pk)

    user_liked_photo = request.user in post.liked_by.all()

    if user_liked_photo:
        post.liked_by.remove(request.user)
        post.likes -= 1
        post.save()

    else:
        post.liked_by.add(request.user)
        post.likes += 1
        post.save()

    return redirect(get_post_url(request, pk))


def comment_post(request, pk):
    post = ImagePost.objects.get(pk=pk)

    form = PostCommentForm(request.POST)

    if form.is_valid():
        comment = form.save(commit=False)
        comment.posted_by = request.user
        comment.related_post = post
        comment.save()

    return redirect(get_post_url(request, pk))
