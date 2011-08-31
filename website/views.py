# coding: utf-8

from django.shortcuts import render_to_response
from django.http import Http404
from datetime import datetime
from website.models import *

def activities_index(request):
  return render_to_response("index.html", { 
    'menutab': request.GET.get('menutab', 0),
    'tipi_concorsuale': Concorsuale.TIPO._choices,
    'concorsuale_idee_list': Concorsuale.objects.filter(tipologia='idee'),
    'concorsuale_gara_list': Concorsuale.objects.filter(tipologia='gara'),
    'servizi_sport_list': Servizi.objects.filter(tipologia='sport'), 
    'servizi_scola_list': Servizi.objects.filter(tipologia='scola'), 
    'servizi_ricer_list': Servizi.objects.filter(tipologia='ricer'), 
    'servizi_liber_list': Servizi.objects.filter(tipologia='liber'), 
    'servizi_conve_list': Servizi.objects.filter(tipologia='conve'), 
    'servizi_sovve_list': Servizi.objects.filter(tipologia='sovve'), 
    'servizi_agevo_list': Servizi.objects.filter(tipologia='agevo'), 
    'urbanistica_list': Urbanistica.objects.all(),
    'consulenza_pedil_list': Consulenza.objects.filter(tipologia='pedil'),
    'consulenza_pcomp_list': Consulenza.objects.filter(tipologia='pcomp'),
    'esperto_list': Esperto.objects.all(),
    'pubblicista_list': Pubblicista.objects.all(),
  } )
  
def activity_detail(request, slug):
  activity = Attivita.objects.select_subclasses().get(slug=slug)
  return render_to_response("detail.html", { 'activity': activity, 'type': type(activity).__name__ } )
