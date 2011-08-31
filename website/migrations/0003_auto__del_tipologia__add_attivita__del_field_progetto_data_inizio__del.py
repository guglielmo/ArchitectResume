# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting model 'Tipologia'
        db.delete_table('website_tipologia')

        # Adding model 'Attivita'
        db.create_table('website_attivita', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titolo', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('data_inizio', self.gf('django.db.models.fields.DateField')(null=True)),
            ('data_fine', self.gf('django.db.models.fields.DateField')(null=True)),
            ('descrizione', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('website', ['Attivita'])

        # Deleting field 'Progetto.data_inizio'
        db.delete_column('website_progetto', 'data_inizio')

        # Deleting field 'Progetto.tipologia'
        db.delete_column('website_progetto', 'tipologia_id')

        # Deleting field 'Progetto.titolo'
        db.delete_column('website_progetto', 'titolo')

        # Deleting field 'Progetto.id'
        db.delete_column('website_progetto', 'id')

        # Deleting field 'Progetto.descrizione'
        db.delete_column('website_progetto', 'descrizione')

        # Adding field 'Progetto.attivita_ptr'
        db.add_column('website_progetto', 'attivita_ptr', self.gf('django.db.models.fields.related.OneToOneField')(default=0, to=orm['website.Attivita'], unique=True, primary_key=True), keep_default=False)


    def backwards(self, orm):
        
        # Adding model 'Tipologia'
        db.create_table('website_tipologia', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('website', ['Tipologia'])

        # Deleting model 'Attivita'
        db.delete_table('website_attivita')

        # Adding field 'Progetto.data_inizio'
        db.add_column('website_progetto', 'data_inizio', self.gf('django.db.models.fields.DateField')(null=True), keep_default=False)

        # Adding field 'Progetto.tipologia'
        db.add_column('website_progetto', 'tipologia', self.gf('django.db.models.fields.related.ForeignKey')(default=0, related_name='progetti_set', to=orm['website.Tipologia']), keep_default=False)

        # Adding field 'Progetto.titolo'
        db.add_column('website_progetto', 'titolo', self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True), keep_default=False)

        # Adding field 'Progetto.id'
        db.add_column('website_progetto', 'id', self.gf('django.db.models.fields.AutoField')(default=0, primary_key=True), keep_default=False)

        # Adding field 'Progetto.descrizione'
        db.add_column('website_progetto', 'descrizione', self.gf('django.db.models.fields.TextField')(default='', blank=True), keep_default=False)

        # Deleting field 'Progetto.attivita_ptr'
        db.delete_column('website_progetto', 'attivita_ptr_id')


    models = {
        'website.attivita': {
            'Meta': {'object_name': 'Attivita'},
            'data_fine': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'data_inizio': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'descrizione': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'titolo': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
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
