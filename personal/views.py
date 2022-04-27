from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request, 'index.html')

def Nimadir(request):
    return render(request, 'blog-single.html')