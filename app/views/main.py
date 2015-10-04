from django.http import HttpResponse
from django.views.generic import View
from django.template import RequestContext, loader
from django.shortcuts import render

# from services.generator import randomize

class main(View):
	def get(self, request, *args, **kwargs):
		template = loader.get_template('main.html')
		context = RequestContext(request, {})
		request.session[0] = 'bar'
		return HttpResponse(template.render(context))
	def post(self, request, *args, **kwargs):
		template = loader.get_template('main.html')
		context = RequestContext(request, {"result": request.session['0']})
		return HttpResponse(template.render(context))
		# def get(self, request, *args, **kwargs):
		#     return HttpResponse("Hello, World")

# def welcome(request):
#     return HttpResponse("Hello, World")


# nodes = [
# 	{
# 		"name": "",
# 		"language": "NodeJS",
# 		"description": "NodeJS is the only real dev language",
# 		"type": "Backend",
# 	}, {
# 		"name": "Express",
# 		"language": "NodeJS",
# 		"description": "",
# 		"type": "Backend",
# 	}, {
# 		"name": "Sails",
# 		"language": "NodeJS",
# 		"description": "",
# 		"type": "Backend",
# 	}, {
# 		"name": "Strongloop",
# 		"language": "NodeJS",
# 		"description": "",
# 		"type": "Backend",
# 	}, {
# 		"name": "Backbone",
# 		"language": "Javascript",
# 		"description": "NodeJS is the only real dev language",
# 		"type": "Backend+Frontend",
# 	}, {
# 		"name": "Ember.js",
# 		"language": "Javascript",
# 		"description": "NodeJS is the only real dev language",
# 		"type": "Backend+Frontend",
# 	}, {
# 		"name": "AngularJS",
# 		"language": "Javascript",
# 		"description": "NodeJS is the only real dev language",
# 		"type": "Frontend",
# 	}, {
# 		"name": "ReactJS",
# 		"language": "Javascript",
# 		"description": "NodeJS is the only real dev language",
# 		"type": "Frontend",
# 	}]

# paths = [
# 	{
# 		"source": "NodeJS",
# 		"target": "ReactJS",
# 		"distance": 56,
# 		"description": "ReactJS isomorphism!!"
# 	}
# ]

# def randomize():
# 	return nodes[0]["description"];