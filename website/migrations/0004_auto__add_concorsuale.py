# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Concorsuale'
        db.create_table('website_concorsuale', (
            ('progetto_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['website.Progetto'], unique=True, primary_key=True)),
            ('tipologia', self.gf('django.db.models.fields.CharField')(max_length=4)),
        ))
        db.send_create_signal('website', ['Concorsuale'])


    def backwards(self, orm):
        
        # Deleting model 'Concorsuale'
        db.delete_table('website_concorsuale')


    models = {
        'website.attivita': {
            'Meta': {'object_name': 'Attivita'},
            'data_fine': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'data_inizio': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'descrizione': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'titolo': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'website.concorsuale': {
            'Meta': {'object_name': 'Concorsuale', '_ormbases': ['website.Progetto']},
            'progetto_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['website.Progetto']", 'unique': 'True', 'primary_key': 'True'}),
            'tipologia': ('django.db.models.fields.CharField', [], {'max_length': '4'})
        },
        'website.progetto': {
            'Meta': {'object_name': 'Progetto', '_ormbases': ['website.Attivita']},
            'attivita_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['website.Attivita']", 'unique': 'True', 'primary_key': 'True'}),
            'committenza': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'luogo': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'realizzato': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'ruolo': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        }
    }

    complete_apps = ['website']
