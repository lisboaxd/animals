from django.shortcuts import render
from django.views.generic import View
from django.http import Http404


from .forms import CadastroPet

class Dashboard(View):

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
        return Http404