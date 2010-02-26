
from south.db import db
from django.db import models
from whereabouts.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'SocialNetwork'
        db.create_table('whereabouts_socialnetwork', (
            ('id', orm['whereabouts.SocialNetwork:id']),
            ('name', orm['whereabouts.SocialNetwork:name']),
            ('site_url', orm['whereabouts.SocialNetwork:site_url']),
            ('icon', orm['whereabouts.SocialNetwork:icon']),
            ('profile_template', orm['whereabouts.SocialNetwork:profile_template']),
        ))
        db.send_create_signal('whereabouts', ['SocialNetwork'])
        
        # Adding model 'SocialNetworkProfile'
        db.create_table('whereabouts_socialnetworkprofile', (
            ('id', orm['whereabouts.SocialNetworkProfile:id']),
            ('network', orm['whereabouts.SocialNetworkProfile:network']),
            ('content_type', orm['whereabouts.SocialNetworkProfile:content_type']),
            ('object_id', orm['whereabouts.SocialNetworkProfile:object_id']),
            ('profile_id', orm['whereabouts.SocialNetworkProfile:profile_id']),
        ))
        db.send_create_signal('whereabouts', ['SocialNetworkProfile'])
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'SocialNetwork'
        db.delete_table('whereabouts_socialnetwork')
        
        # Deleting model 'SocialNetworkProfile'
        db.delete_table('whereabouts_socialnetworkprofile')
        
    
    
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
        }
    }
    
    complete_apps = ['whereabouts']
