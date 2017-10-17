from django import forms
from .models import Pet

class CadastroPet(forms.ModelForm):
    """
    Formulario de Cadastro de um Pet
    @Author: Mateus Lisboa
    @Since: 10/2017
    """
    class Meta:
        model = Pet
        fields = [
            'nome',
            'idade',
            'especie',
            'raca',
            'castrado',
            'sexo',
            'cor',
        ]




