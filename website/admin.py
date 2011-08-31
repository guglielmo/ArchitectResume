from django.contrib import admin 
from website.models import *

class ImmagineInline(admin.StackedInline): 
  model = Immagine
  extra = 0

class AttivitaAdmin(admin.ModelAdmin):
  prepopulated_fields = { 'slug': ['titolo'] }
  search_fields = ['^titolo', '^descrizione']
  inlines = [ImmagineInline]


admin.site.register(Concorsuale, AttivitaAdmin)
admin.site.register(Servizi, AttivitaAdmin)
admin.site.register(Urbanistica, AttivitaAdmin)
admin.site.register(Esperto, AttivitaAdmin)
admin.site.register(Consulenza, AttivitaAdmin)
admin.site.register(Pubblicista, AttivitaAdmin)