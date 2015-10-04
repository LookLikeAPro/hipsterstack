from django.http import HttpResponse
from django.views.generic import View
from django.template import RequestContext, loader
from django.shortcuts import render

# from services.generator import randomize

class questionnaire(View):
	def get(self, request, *args, **kwargs):
		request.session['answers'] = [1,2,3]
		template = loader.get_template('questionnaire.html')
		context = RequestContext(request, {'question': "WHAT TE FUCK"})
		return HttpResponse(template.render(context))
	def post(self, request, *args, **kwargs):
		template = loader.get_template('questionnaire.html')
		context = RequestContext(request, {"result": request.session['answers']})
		return HttpResponse(template.render(context))
		# def get(self, request, *args, **kwargs):
		#     return HttpResponse("Hello, World")