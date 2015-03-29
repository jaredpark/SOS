from django.shortcuts import render
from utilities import ContactFormProcessor

def homepage(request):
	context_dictionary = {}
	ContactFormProcessor(request, context_dictionary)
	return(render(request, 'homepage/index.html', context_dictionary))