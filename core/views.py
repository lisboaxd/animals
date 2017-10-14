from django.shortcuts import render
from django.views.generic import View
from django.http import Http404


from .forms import CadastroPet

class Dashboard(View):

    def get(self,request, *args, **kwargs):
        return render(request,
                      'core/index.html',
                      context={
                          'title': 'ola mundo',
                          'cabecalho': 'Titulo do cabecalho',
                          'form': CadastroPet()
                      },
                      status=201
                      )

    def post(self,request):
        return Http404