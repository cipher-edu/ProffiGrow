from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.template import loader

# Create your views here.
class IndexView(View):
    def get(self, request):
        template = loader.get_template('index-saas.html')
        return HttpResponse(template.render({}, request))