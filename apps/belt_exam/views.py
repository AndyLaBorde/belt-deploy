from django.shortcuts import render, redirect
from .models import *
# Create your views here.
def index(request):

	if request.session.get('errors') == None:
		request.session['errors'] = []
	return render(request, 'belt_exam/index.html')

def register(request):

	if request.method == 'POST':
		errors = User.objects.register_validation(request.POST)
		print errors
	if len(errors) != 0:
		request.session['errors'] = errors
		return redirect('/')
	else: 
		user = User.objects.register(request.POST)
		request.session['user_id'] = user.id
		request.session['name'] = user.name
		return redirect('/dashboard')	
		print User.objects.all()

def login(request):

	errors = User.objects.login_validation(request.POST)
	if len(errors) != 0:
		request.session['errors'] = errors
		
		for error in errors:
			print error
		return redirect('/dashboard')
	else:
		user= User.objects.login(request.POST)
		request.session['user_id'] = user.id
		request.session['name'] = user.name
		return redirect('/dashboard')

def logout(request):
	request.session.clear()
	return redirect('/')

def dashboard(request):
	user = User.objects.get(id =request.session['user_id'])
	context = {
	"user" : user,
	"favQuotes": user.quotes.all(),
	"otherQuotes" : Quote.objects.exclude(added_by = user),

	}
	return render(request, 'belt_exam/dashboard.html', context)

def add_quote(request):

	Quote.objects.addQuote(request.POST, request.session['user_id'])
	return redirect('/dashboard')

def add_fav(request, quote_id):
	# user_id = request.session['user_id']
	user  = User.objects.get(id= request.session['user_id'])
	quote = Quote.objects.get(id= quote_id)

	quote.added_by.add(user)
	return redirect('/dashboard')


def remove_quote(request, quote_id):
	user_id = request.session['user_id']
	Quote.objects.get(id=quote_id).added_by.remove(user_id)
	return redirect('/dashboard')

def user_quotes(request, user_id):
	user = User.objects.get(id= user_id)
	context={
		'quote': Quote.objects.filter(added_by = user).all(),
		'user' : user,
	}
	return render(request, 'belt_exam/quote.html', context)



