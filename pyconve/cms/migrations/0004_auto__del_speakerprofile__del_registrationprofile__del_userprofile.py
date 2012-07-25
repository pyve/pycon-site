# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'SpeakerProfile'
        db.delete_table('cms_speakerprofile')

        # Deleting model 'RegistrationProfile'
        db.delete_table('cms_registrationprofile')

        # Deleting model 'UserProfile'
        db.delete_table('cms_userprofile')


    def backwards(self, orm):
        # Adding model 'SpeakerProfile'
        db.create_table('cms_speakerprofile', (
            ('userprofile_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.UserProfile'], unique=True, primary_key=True)),
            ('picture', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('about', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('cms', ['SpeakerProfile'])

        # Adding model 'RegistrationProfile'
        db.create_table('cms_registrationprofile', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('consumed', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('token', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('encoded', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('cms', ['RegistrationProfile'])

        # Adding model 'UserProfile'
        db.create_table('cms_userprofile', (
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['localization.Country'])),
            ('state', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['localization.State'], null=True, blank=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('available_votes', self.gf('django.db.models.fields.IntegerField')(default=5)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('cms', ['UserProfile'])


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'cms.presentation': {
            'Meta': {'object_name': 'Presentation'},
            'approved': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'duration': ('django.db.models.fields.IntegerField', [], {'default': '60'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'requirements': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'speakers': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.User']", 'symmetrical': 'False'}),
            'tutorial': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'votes': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['cms']