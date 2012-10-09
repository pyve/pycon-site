# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'UserProfile.what'
        db.add_column('profiles_userprofile', 'what',
                      self.gf('django.db.models.fields.TextField')(max_length=64, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'UserProfile.what'
        db.delete_column('profiles_userprofile', 'what')


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
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'localization.country': {
            'Meta': {'object_name': 'Country'},
            'abbreviation': ('django.db.models.fields.CharField', [], {'default': "'OT'", 'max_length': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        'localization.state': {
            'Meta': {'object_name': 'State'},
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['localization.Country']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        'profiles.passwordrecovery': {
            'Meta': {'object_name': 'PasswordRecovery'},
            'consumed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'encoded': ('django.db.models.fields.CharField', [], {'max_length': '256', 'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'token': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
        'profiles.registrationprofile': {
            'Meta': {'object_name': 'RegistrationProfile'},
            'consumed': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'encoded': ('django.db.models.fields.CharField', [], {'max_length': '256', 'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'token': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
        'profiles.sponsor': {
            'Meta': {'object_name': 'Sponsor'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'sponsorship_type': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'})
        },
        'profiles.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'about': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'available_votes': ('django.db.models.fields.IntegerField', [], {'default': '5'}),
            'contributor': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['localization.Country']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'pycon': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['localization.State']", 'null': 'True', 'blank': 'True'}),
            'twitter': ('django.db.models.fields.TextField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'}),
            'what': ('django.db.models.fields.TextField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['profiles']