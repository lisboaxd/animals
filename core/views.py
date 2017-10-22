from django.shortcuts import render
from django.views.generic import View
from django.http import Http404,HttpResponse


from .forms import CadastroPet

class Dashboard(View):

    http_method_names = ['get','post']

    def get(self,request, *args, **kwargs):
        return render(request,
                      'core/formulario.html',
                      context={
                          'title': 'ola mundo',
                          'cabecalho': 'Titulo do cabecalho',
                          'form': CadastroPet()
                      }
                      )

    def post(self,request):
        request

    def http_method_not_allowed(sel,request):
        return HttpResponse(u'Sinto muito, voce nao pode fazer request com o metodo usado')

