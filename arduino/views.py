from django.shortcuts import render

# Create your views here.
def arduino(request):
	return render(request, 'arduino.html')