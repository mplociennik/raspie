from django.http import HttpResponse, HttpRequest
from django.views.generic import View
from django.conf import settings
from django.shortcuts import render

import pyvona

class Speech(View):
    template_name = 'speech/test.html'

    def get(self, request, *args, **kwargs):
        if request.GET.get('text'):
            print request.GET['text']
            v = pyvona.create_voice(settings.IVONA_ACCESS_KEY, 
                                    settings.IVONA_SECRET_KEY)
            v.voice_name = 'Jacek'
            v.speak(request.GET['text'])
        return render(request, self.template_name)
