from django.shortcuts import render

# Create your views here.
def ev3(request):
	return render(request, 'ev3.html')