from django.shortcuts import render

# Create your views here.
def show_main(request):
    return render(request, "appcoolshop/main.html")

def show_catalog(request):
    return render(request, "appcoolshop/catalog.html")

def show_feedback(request):
    return render(request, "appcoolshop/feedback.html")    

def show_about(request):
    return render(request, "appcoolshop/about.html")    