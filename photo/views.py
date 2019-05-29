from django.shortcuts import render, redirect
from .models import Photo
from .forms import PhotoForm

# Create your views here.
def photo(request):
    photos = Photo.objects
    return render(request, 'photo/photo.html', {'photos':photos})
    
# 생성

def new(req):
    return render(req, 'photo/new.html')

def create(req):
    if req.method == 'POST':
        form = PhotoForm(req.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('photo')

    else:
        form = PhotoForm()
        return render(req, 'photo/new.html' , {'form':form})