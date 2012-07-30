# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Country.abbreviation'
        db.add_column('localization_country', 'abbreviation',
                      self.gf('django.db.models.fields.CharField')(default='OT', max_length=2),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Country.abbreviation'
        db.delete_column('localization_country', 'abbreviation')


    models = {
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
        }
    }

    complete_apps = ['localization']