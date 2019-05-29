from django.shortcuts import render, redirect, get_object_or_404
from .forms import BlogPost, CommentForm
from .models import Blog

from datetime import datetime

# Create your views here.
def new(req):
  return render(req, 'blogcrud/new.html')

def create(req):
	if req.method == 'POST':
		form = BlogPost(req.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.save()
			return redirect('home')
			
	else:
		form = BlogPost()
		return render(req, 'blogcrud/new.html', {'form':form})

# 삭제
def delete(req, blog_id):
  post = get_object_or_404(Blog, pk = blog_id)
  post.delete()
  return redirect('home')

# 업데이트
def update(req, blog_id):
	post = get_object_or_404(Blog, pk = blog_id)
	if req.method == "POST":
		form = BlogPost(req.POST, instance = post)
		if form.is_valid():
			post = form.save(commit=False)
			post.update_date = datetime.now()
			post.save()
			return redirect('home')
	else:
			form = BlogPost(instance = post)
			return render(req, 'blogcrud/edit.html', {'form':form})

# 댓글생성
def commentcreate(req, blog_id):
	post = get_object_or_404(Blog, pk = blog_id)
	if req.method == "POST":
		form = CommentForm(req.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.post = post
			comment.save()
			return redirect('detail', blog_id = post.pk)
	else:
	  form = CommentForm()
	  return render(req, 'blogapp/detail.html', {'form': form, 'blog': post})