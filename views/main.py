from django.http import HttpResponse
from django.views.generic import View
from django.template import RequestContext, loader
from django.shortcuts import render

from services.generator import generator

class main(View):
	def get(self, request, *args, **kwargs):
		template = loader.get_template('main.html')
		context = RequestContext(request, {})
		return HttpResponse(template.render(context))
	def post(self, request, *args, **kwargs):
		template = loader.get_template('main.html')
		context = RequestContext(request, {"result": generator.randomize()})
		return HttpResponse(template.render(context))
		# def get(self, request, *args, **kwargs):
		#     return HttpResponse("Hello, World")

# def welcome(request):
#     return HttpResponse("Hello, World")