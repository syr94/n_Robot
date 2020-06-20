from django.shortcuts import render

# Create your views here.
def programming(request):
	return render(request, 'programming.html')