from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'blog/index.html', {})

#def about(request):
    #return render(request, 'blog/about.html', {})

def about(request):
    return render(request, 'blog/about.html', {})
