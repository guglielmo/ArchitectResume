# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Attivita.real_type'
        db.delete_column('website_attivita', 'real_type_id')


    def backwards(self, orm):
        
        # Adding field 'Attivita.real_type'
        db.add_column('website_attivita', 'real_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'], null=True), keep_default=False)


    models = {
        'website.attivita': {
            'Meta': {'object_name': 'Attivita'},
            'data_fine': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'data_inizio': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'descrizione': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'titolo': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'website.concorsuale': {
            'Meta': {'object_name': 'Concorsuale', '_ormbases': ['website.Progetto']},
            'progetto_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['website.Progetto']", 'unique': 'True', 'primary_key': 'True'}),
            'tipologia': ('django.db.models.fields.CharField', [], {'max_length': '4'})
        },
        'website.consulenza': {
            'Meta': {'object_name': 'Consulenza', '_ormbases': ['website.Attivita']},
            'attivita_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['website.Attivita']", 'unique': 'True', 'primary_key': 'True'}),
            'tipologia': ('django.db.models.fields.CharField', [], {'max_length': '5'})
        },
        'website.esperto': {
            'Meta': {'object_name': 'Esperto', '_ormbases': ['website.Attivita']},
            'attivita_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['website.Attivita']", 'unique': 'True', 'primary_key': 'True'}),
            'luogo': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        'website.immagine': {
            'Meta': {'object_name': 'Immagine'},
            'attach_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'attivita': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['website.Attivita']"}),
            'didascalia': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'website.progetto': {
            'Meta': {'object_name': 'Progetto', '_ormbases': ['website.Attivita']},
            'attivita_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['website.Attivita']", 'unique': 'True', 'primary_key': 'True'}),
            'committenza': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'luogo': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'realizzato': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'ruolo': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        'website.pubblicista': {
            'Meta': {'object_name': 'Pubblicista', '_ormbases': ['website.Attivita']},
            'attivita_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['website.Attivita']", 'unique': 'True', 'primary_key': 'True'}),
            'editore': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'pubblicazione': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'ruolo': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        'website.servizi': {
            'Meta': {'object_name': 'Servizi', '_ormbases': ['website.Progetto']},
            'progetto_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['website.Progetto']", 'unique': 'True', 'primary_key': 'True'}),
            'tipologia': ('django.db.models.fields.CharField', [], {'max_length': '5'})
        },
        'website.urbanistica': {
            'Meta': {'object_name': 'Urbanistica', '_ormbases': ['website.Progetto']},
            'progetto_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['website.Progetto']", 'unique': 'True', 'primary_key': 'True'})
        }
    }

    complete_apps = ['website']
