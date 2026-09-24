from django.shortcuts import render

# Create your views here.
def about(request):
    return render(request, 'bio/about.html')\

def details(request):
    return render(request, 'bio/about_detail.html')