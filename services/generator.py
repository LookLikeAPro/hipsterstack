nodes = [
	{
		"name": "",
		"language": "NodeJS",
		"description": "NodeJS is the only real dev language",
		"type": "Backend",
	}, {
		"name": "Express",
		"language": "NodeJS",
		"description": "",
		"type": "Backend",
	}, {
		"name": "Sails",
		"language": "NodeJS",
		"description": "",
		"type": "Backend",
	}, {
		"name": "Strongloop",
		"language": "NodeJS",
		"description": "",
		"type": "Backend",
	}, {
		"name": "Backbone",
		"language": "Javascript",
		"description": "NodeJS is the only real dev language",
		"type": "Backend+Frontend",
	}, {
		"name": "Ember.js",
		"language": "Javascript",
		"description": "NodeJS is the only real dev language",
		"type": "Backend+Frontend",
	}, {
		"name": "AngularJS",
		"language": "Javascript",
		"description": "NodeJS is the only real dev language",
		"type": "Frontend",
	}, {
		"name": "ReactJS",
		"language": "Javascript",
		"description": "NodeJS is the only real dev language",
		"type": "Frontend",
	}]

paths = [
	{
		"source": "NodeJS",
		"target": "ReactJS",
		"distance": 56,
		"description": "ReactJS isomorphism!!"
	}
]

def randomize():
	return nodes[0]["description"];