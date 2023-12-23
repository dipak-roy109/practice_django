from django.shortcuts import render, HttpResponse

# Create your views here.

def Teacher_name(request):
    return HttpResponse('<h2> This is Teacher object </h2> <p> hi, my name is Dipak Roy. I am from Bangladesh </p>')
