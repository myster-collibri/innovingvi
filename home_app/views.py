from django.shortcuts import render

# Create your views here.

def home(request):

    return render(request,'index.html')

def about(request):

    return render(request,'about.html')

def formation(request):

    return render(request,'formation.html')

def service(request):

	return render(request,"services.html")

def blog_fx(request):

    return render(request,'blog.html')

def gallery(request):

    return render(request,'gallery.html')

def videos(request):

    return render(request,'videos.html')

def document(request):

    return render(request,'document.html')

def project(request):

    return render(request,'project.html')
