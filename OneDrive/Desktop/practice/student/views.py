from django.shortcuts import render, HttpResponse
# Create your views here.

def Student_name(request):
    return render(request, 'hello.html')