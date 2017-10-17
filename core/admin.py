from django.contrib import admin
from .models import Pet, Especie, Raca




class PetModelAdmin(admin.ModelAdmin):
	list_display = ['nome','idade','cor','raca','sexo','castrado']
	list_display_links = ['nome']
	list_editable = ['raca','castrado']
	list_filter = ['nome','castrado','cor','idade','sexo']
	search_fields = ['nome']
	class Meta:
		model = Pet




# Register your models here.
admin.site.register(Pet,PetModelAdmin)
admin.site.register(Especie)
admin.site.register(Raca)