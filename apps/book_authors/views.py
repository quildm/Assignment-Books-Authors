from django.shortcuts import render, HttpResponse, redirect

def index(request):
	response = "Hello, This is book_authors"
	return HttpResponse(response)