#Add models to view. The '.' before models works because it's in the same directory as the views file.
from django.shortcuts import render
from django.utils import timezone
from .models import Post

#Making a view...something

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
    



