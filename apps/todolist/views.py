from django.shortcuts import render

# Create your views here.

def TodolistView(request):
	return render(request, "todolist.html")