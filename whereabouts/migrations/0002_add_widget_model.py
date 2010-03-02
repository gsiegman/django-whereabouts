
from south.db import db
from django.db import models
from whereabouts.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'SocialNetworkWidget'
        db.create_table('whereabouts_socialnetworkwidget', (
            ('id', orm['whereabouts.socialnetworkwidget:id']),
            ('network', orm['whereabouts.socialnetworkwidget:network']),
            ('name', orm['whereabouts.socialnetworkwidget:name']),
            ('slug', orm['whereabouts.socialnetworkwidget:slug']),
            ('description', orm['whereabouts.socialnetworkwidget:description']),
            ('widget_template', orm['whereabouts.socialnetworkwidget:widget_template']),
        ))
        db.send_create_signal('whereabouts', ['SocialNetworkWidget'])
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'SocialNetworkWidget'
        db.delete_table('whereabouts_socialnetworkwidget')
        
    
    
    models = {
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'whereabouts.socialnetwork': {
            'icon': ('django.db.models.fields.files.ImageField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'profile_template': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'site_url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'whereabouts.socialnetworkprofile': {
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'network': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['whereabouts.SocialNetwork']"}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'profile_id': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'whereabouts.socialnetworkwidget': {
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'network': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['whereabouts.SocialNetwork']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'widget_template': ('django.db.models.fields.TextField', [], {})
        }
    }
    
    complete_apps = ['whereabouts']
