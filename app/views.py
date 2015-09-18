from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import View
from django.template import RequestContext, loader

class welcome(View):
	def get(self, request, *args, **kwargs):
		template = loader.get_template('index.html')
		context = RequestContext(request, {})
		return HttpResponse(template.render(context))
		# def get(self, request, *args, **kwargs):
		#     return HttpResponse("Hello, World")

# def welcome(request):
#     return HttpResponse("Hello, World")