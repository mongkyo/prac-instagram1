from django.shortcuts import render, redirect

from .models import Post, User


def post_list(request):
    if request.method == 'POST':
        post = Post(
            author=User.objects.first(),
            photo=request.FILES['photo'],
        )
        post.save()
        return redirect('posts:post-list')