# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting model 'Progetto'
        db.delete_table('website_progetto')

        # Deleting field 'Servizi.progetto_ptr'
        db.delete_column('website_servizi', 'progetto_ptr_id')

        # Adding field 'Servizi.attivita_ptr'
        db.add_column('website_servizi', 'attivita_ptr', self.gf('django.db.models.fields.related.OneToOneField')(default=0, to=orm['website.Attivita'], unique=True, primary_key=True), keep_default=False)

        # Adding field 'Servizi.luogo'
        db.add_column('website_servizi', 'luogo', self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True), keep_default=False)

        # Adding field 'Servizi.ruolo'
        db.add_column('website_servizi', 'ruolo', self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True), keep_default=False)

        # Adding field 'Servizi.committenza'
        db.add_column('website_servizi', 'committenza', self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True), keep_default=False)

        # Adding field 'Servizi.realizzato'
        db.add_column('website_servizi', 'realizzato', self.gf('django.db.models.fields.CharField')(default='no', max_length=3), keep_default=False)

        # Deleting field 'Concorsuale.progetto_ptr'
        db.delete_column('website_concorsuale', 'progetto_ptr_id')

        # Adding field 'Concorsuale.attivita_ptr'
        db.add_column('website_concorsuale', 'attivita_ptr', self.gf('django.db.models.fields.related.OneToOneField')(default=0, to=orm['website.Attivita'], unique=True, primary_key=True), keep_default=False)

        # Adding field 'Concorsuale.luogo'
        db.add_column('website_concorsuale', 'luogo', self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True), keep_default=False)

        # Adding field 'Concorsuale.ruolo'
        db.add_column('website_concorsuale', 'ruolo', self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True), keep_default=False)

        # Adding field 'Concorsuale.committenza'
        db.add_column('website_concorsuale', 'committenza', self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True), keep_default=False)

        # Adding field 'Concorsuale.realizzato'
        db.add_column('website_concorsuale', 'realizzato', self.gf('django.db.models.fields.CharField')(default='no', max_length=3), keep_default=False)

        # Deleting field 'Urbanistica.progetto_ptr'
        db.delete_column('website_urbanistica', 'progetto_ptr_id')

        # Adding field 'Urbanistica.attivita_ptr'
        db.add_column('website_urbanistica', 'attivita_ptr', self.gf('django.db.models.fields.related.OneToOneField')(default=0, to=orm['website.Attivita'], unique=True, primary_key=True), keep_default=False)

        # Adding field 'Urbanistica.luogo'
        db.add_column('website_urbanistica', 'luogo', self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True), keep_default=False)

        # Adding field 'Urbanistica.ruolo'
        db.add_column('website_urbanistica', 'ruolo', self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True), keep_default=False)

        # Adding field 'Urbanistica.committenza'
        db.add_column('website_urbanistica', 'committenza', self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True), keep_default=False)

        # Adding field 'Urbanistica.realizzato'
        db.add_column('website_urbanistica', 'realizzato', self.gf('django.db.models.fields.CharField')(default='no', max_length=3), keep_default=False)


    def backwards(self, orm):
        
        # Adding model 'Progetto'
        db.create_table('website_progetto', (
            ('attivita_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['website.Attivita'], unique=True, primary_key=True)),
            ('ruolo', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('luogo', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('committenza', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('realizzato', self.gf('django.db.models.fields.CharField')(max_length=3)),
        ))
        db.send_create_signal('website', ['Progetto'])

        # Adding field 'Servizi.progetto_ptr'
        db.add_column('website_servizi', 'progetto_ptr', self.gf('django.db.models.fields.related.OneToOneField')(default=0, to=orm['website.Progetto'], unique=True, primary_key=True), keep_default=False)

        # Deleting field 'Servizi.attivita_ptr'
        db.delete_column('website_servizi', 'attivita_ptr_id')

        # Deleting field 'Servizi.luogo'
        db.delete_column('website_servizi', 'luogo')

        # Deleting field 'Servizi.ruolo'
        db.delete_column('website_servizi', 'ruolo')

        # Deleting field 'Servizi.committenza'
        db.delete_column('website_servizi', 'committenza')

        # Deleting field 'Servizi.realizzato'
        db.delete_column('website_servizi', 'realizzato')

        # Adding field 'Concorsuale.progetto_ptr'
        db.add_column('website_concorsuale', 'progetto_ptr', self.gf('django.db.models.fields.related.OneToOneField')(default=0, to=orm['website.Progetto'], unique=True, primary_key=True), keep_default=False)

        # Deleting field 'Concorsuale.attivita_ptr'
        db.delete_column('website_concorsuale', 'attivita_ptr_id')

        # Deleting field 'Concorsuale.luogo'
        db.delete_column('website_concorsuale', 'luogo')

        # Deleting field 'Concorsuale.ruolo'
        db.delete_column('website_concorsuale', 'ruolo')

        # Deleting field 'Concorsuale.committenza'
        db.delete_column('website_concorsuale', 'committenza')

        # Deleting field 'Concorsuale.realizzato'
        db.delete_column('website_concorsuale', 'realizzato')

        # Adding field 'Urbanistica.progetto_ptr'
        db.add_column('website_urbanistica', 'progetto_ptr', self.gf('django.db.models.fields.related.OneToOneField')(default=0, to=orm['website.Progetto'], unique=True, primary_key=True), keep_default=False)

        # Deleting field 'Urbanistica.attivita_ptr'
        db.delete_column('website_urbanistica', 'attivita_ptr_id')

        # Deleting field 'Urbanistica.luogo'
        db.delete_column('website_urbanistica', 'luogo')

        # Deleting field 'Urbanistica.ruolo'
        db.delete_column('website_urbanistica', 'ruolo')

        # Deleting field 'Urbanistica.committenza'
        db.delete_column('website_urbanistica', 'committenza')

        # Deleting field 'Urbanistica.realizzato'
        db.delete_column('website_urbanistica', 'realizzato')


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
            'Meta': {'object_name': 'Concorsuale', '_ormbases': ['website.Attivita']},
            'attivita_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['website.Attivita']", 'unique': 'True', 'primary_key': 'True'}),
            'committenza': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'luogo': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'realizzato': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'ruolo': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
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
        'website.pubblicista': {
            'Meta': {'object_name': 'Pubblicista', '_ormbases': ['website.Attivita']},
            'attivita_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['website.Attivita']", 'unique': 'True', 'primary_key': 'True'}),
            'editore': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'pubblicazione': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'ruolo': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        'website.servizi': {
            'Meta': {'object_name': 'Servizi', '_ormbases': ['website.Attivita']},
            'attivita_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['website.Attivita']", 'unique': 'True', 'primary_key': 'True'}),
            'committenza': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'luogo': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'realizzato': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'ruolo': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'tipologia': ('django.db.models.fields.CharField', [], {'max_length': '5'})
        },
        'website.urbanistica': {
            'Meta': {'object_name': 'Urbanistica', '_ormbases': ['website.Attivita']},
            'attivita_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['website.Attivita']", 'unique': 'True', 'primary_key': 'True'}),
            'committenza': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'luogo': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'realizzato': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'ruolo': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        }
    }

    complete_apps = ['website']
