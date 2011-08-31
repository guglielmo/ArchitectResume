# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Progetto'
        db.create_table('website_progetto', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titolo', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('data_inizio', self.gf('django.db.models.fields.DateField')(null=True)),
            ('descrizione', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('ruolo', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('luogo', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('committenza', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('realizzato', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('tipologia', self.gf('django.db.models.fields.related.ForeignKey')(related_name='progetti_set', to=orm['website.Tipologia'])),
        ))
        db.send_create_signal('website', ['Progetto'])

        # Adding model 'Tipologia'
        db.create_table('website_tipologia', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('website', ['Tipologia'])


    def backwards(self, orm):
        
        # Deleting model 'Progetto'
        db.delete_table('website_progetto')

        # Deleting model 'Tipologia'
        db.delete_table('website_tipologia')


    models = {
        'website.progetto': {
            'Meta': {'object_name': 'Progetto'},
            'committenza': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'data_inizio': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'descrizione': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'luogo': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'realizzato': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'ruolo': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'tipologia': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'progetti_set'", 'to': "orm['website.Tipologia']"}),
            'titolo': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        'website.tipologia': {
            'Meta': {'object_name': 'Tipologia'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['website']
