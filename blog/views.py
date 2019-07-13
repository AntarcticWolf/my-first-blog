from django.shortcuts import render

#Making a view...something

def post_list(request):
    return render(request, 'blog/post_list.html', {})
