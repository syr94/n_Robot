from django.shortcuts import render


def index(request):
	return render(request, 'mainApp/homePage.html')
# Create your views here.
def contact(request):
	contacts = ['Если у вас стались вопросы, можете связаться со мной', '+7 (929)-150-947', 'syr94@mail.ru']
	return render(request, 'mainApp/contact.html',{'values':contacts})