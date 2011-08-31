# coding: utf-8
import time
from django.db import models
from model_utils import Choices
from model_utils.managers import InheritanceManager
from markdown2 import markdown
from south.modelsinspector import add_introspection_rules

add_introspection_rules([], ["^tagging\.fields\.TagField"])


class Attivita(models.Model):
  '''
  Classe base per tutte le attivita
  '''
  titolo = models.CharField(max_length=255)
  slug = models.SlugField(unique=True)
  data_inizio = models.DateField(null=True, help_text="La data di inizio del progetto")
  data_fine = models.DateField(blank=True, help_text="La data di fine del progetto")
  descrizione = models.TextField(blank=True)
  descrizione_html = models.TextField(editable=False, blank=True)
  collaborazioni = models.CharField(max_length=255, blank=True)

  objects = InheritanceManager()

  # override save per generare l'html dal markdown
  def save(self, force_insert=False, force_update=False):
    self.descrizione_html = markdown(self.descrizione)
    super(Attivita, self).save(force_insert, force_update)

  def periodo(self):
    if self.data_fine:
      return "%s - %s" % (self.data_inizio.year, self.data_fine.year)
    else:
      return "%s" % (self.data_inizio.year,)
      
  class Meta:
    verbose_name = 'attività'
    verbose_name_plural = 'attività'

  def __unicode__(self):
    return self.titolo
    
  def get_absolute_url(self):
      return "/scheda/%s/" % (self.slug,)


class Immagine(models.Model):
  didascalia = models.CharField(max_length=200)
  attivita = models.ForeignKey('Attivita')
  attach_file = models.FileField(upload_to="schede/", blank=True)

  def __unicode__(self):
    return u'%s' % self.didascalia

  class Meta:
    verbose_name_plural = 'immagini'
      

class Progetto(models.Model):
  '''
  Rappresenta un progetto (astratto)
  '''
  STATUS = Choices(
    ('si', 'Sì'),    
    ('no', 'No'))
  
  luogo = models.CharField(blank=True, max_length=255)
  ruolo = models.CharField(blank=True, max_length=255)
  committenza = models.CharField(blank=True, max_length=255)
  realizzato = models.CharField(max_length=3, choices=STATUS)

  class Meta:
    abstract = True


class Concorsuale(Attivita, Progetto):
  '''
  Rappresenta un'attivita progettuale di tipo concorsuale
  '''
  TIPO = Choices(
    ('idee', 'Concorsi di idee'),    
    ('gara', 'Bandi di gara'))
  tipologia = models.CharField(max_length=4, choices=TIPO)
  def extended_tipologia(self):
    for t in self.TIPO._choices:
      if self.tipologia == t[0]:
        return t[1]

  class Meta(Progetto.Meta):
    verbose_name = 'attività concorsuale'
    verbose_name_plural = 'attività concorsuali'


class Servizi(Attivita, Progetto):
  '''
  Rappresenta un'attivita progettuale servizio di architettura
  '''
  TIPO = Choices(
    ('sport', 'Attrezzature sportive'),    
    ('scola', 'Attrezzature scolastiche'),
    ('ricer', 'Attività di ricerca nei programmi sperimentali per interventi di ERP'),
    ('liber', 'Edifici di civile abitazione di iniziativa privata (Edilizia libera)'),
    ('conve', 'Edifici di civile abitazione di iniziativa pubblica (Edilizia convenzionata)'),
    ('sovve', 'Edilizia sovvenzionata'),
    ('agevo', 'Edilizia agevolata'),
    )
  tipologia = models.CharField(max_length=5, choices=TIPO)
  def extended_tipologia(self):
    for t in self.TIPO._choices:
      if self.tipologia == t[0]:
        return t[1]

  class Meta(Progetto.Meta):
    verbose_name = 'attività (servizi di architettura)'
    verbose_name_plural = 'attività servizi di architettura'


class Urbanistica(Attivita, Progetto):
  '''
  Rappresenta un'attivita progettuale servizio di architettura
  '''
  class Meta(Progetto.Meta):
    verbose_name = 'attività (urbanistica)'
    verbose_name_plural = 'attività urbanistica'
    
    
class Esperto(Attivita):
  '''
  Rappresenta un'attivita in quanto esperto
  '''
  luogo = models.CharField(blank=True, max_length=255)

  class Meta:
    verbose_name = 'attività (esperto)'
    verbose_name_plural = 'attività di esperto'


class Consulenza(Attivita):
  '''
  Rappresenta un'attivita di consulenza
  '''
  TIPO = Choices(
    ('pedil', 'Programmi edilizi'),    
    ('pcomp', 'Programmi complessi'),
    )
  tipologia = models.CharField(max_length=5, choices=TIPO)
  def extended_tipologia(self):
    for t in self.TIPO._choices:
      if self.tipologia == t[0]:
        return t[1]
        
  class Meta:
    verbose_name = 'attività (consulenza)'
    verbose_name_plural = 'attività di consulenza'


class Pubblicista(Attivita):
  '''
  Rappresenta un'attivita di pubblicista
  '''
  pubblicazione = models.CharField(max_length=255)
  ruolo = models.CharField(blank=True, max_length=255)
  editore = models.CharField(blank=True, max_length=255)

  class Meta:
    verbose_name = 'attività (pubblicista)'
    verbose_name_plural = 'attività di pubblicista'
  