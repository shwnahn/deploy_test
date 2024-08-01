from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
import json

# Create your views here.
def posts(request):
  posts = Post.objects.all()
  ctx = {
    'posts': posts
  }
  return render(request, 'pirostagram/list.html', ctx)

def login(request):
  return render(request, 'user/login.html')

@login_required
def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        image_form = PostImageForm(request.POST, request.FILES)

        if form.is_valid() and image_form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            
            images = image_form.cleaned_data.get('images')
            if images:
                for img in images:
                    Image.objects.create(post=post, image=img)
            
            messages.success(request, 'Post created successfully!')
            return redirect('pirostagram:posts')
        else:
            messages.error(request, 'There was an error with your submission. Please check the form.')
    else:
        form = PostForm()
        image_form = PostImageForm()
    
    ctx = {
        'form': form,
        'image_form': image_form
    }
    return render(request, 'pirostagram/new_post.html', ctx)

@login_required
def like_post(request):
  post_id = request.POST.get('id')
  button_type = request.POST.get('type')

  post = Post.objects.get(id=post_id)

  if button_type == 'like':
      if request.user not in post.likes.all():
          post.likes.add(request.user)
  else:
      if request.user in post.likes.all():
          post.likes.remove(request.user)

  return JsonResponse({'id': post.id, 'type': button_type, 'likes': post.likes.count()})

@login_required
def leave_comment(request):
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        text = request.POST.get('text')
        post = Post.objects.get(id=post_id)
        comment = Comment.objects.create(post=post, user=request.user, text=text)
        return JsonResponse({'id': comment.id, 'user': comment.user.username, 'text': comment.text})

@login_required
def delete_comment(request):
    comment_id = request.POST.get('comment_id')
    comment = Comment.objects.get(id=comment_id)
    if comment.user == request.user:
        comment.delete()
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error'}, status=403)