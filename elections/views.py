from django.http import HttpResponse
from django.template import loader

def home(request):
	template = loader.get_template('elections/home.html')
	return HttpResponse (template.render(request))

def hashtags(request):
	template=loader.get_template('elections/hashtags.html')
	return HttpResponse(template.render(request))

def retweets(request):
	template=loader.get_template('elections/retweets.html')
	return HttpResponse(template.render(request))

def popularity(request):
	template=loader.get_template('elections/popularity.html')
	return HttpResponse(template.render(request))

def location(request):
	template=loader.get_template('elections/location.html')
	return HttpResponse(template.render(request))

def analysis(request):
	template=loader.get_template('elections/analysis.html')
	return HttpResponse(template.render(request))









