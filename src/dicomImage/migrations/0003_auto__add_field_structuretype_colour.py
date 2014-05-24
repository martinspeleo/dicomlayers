# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'StructureType.colour'
        db.add_column('dicomImage_structuretype', 'colour',
                      self.gf('django.db.models.fields.CharField')(default='FFEDA0', max_length=6),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'StructureType.colour'
        db.delete_column('dicomImage_structuretype', 'colour')


    models = {
        'dicomImage.image': {
            'Meta': {'object_name': 'Image'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagePositionPatientX': ('django.db.models.fields.FloatField', [], {}),
            'imagePositionPatientY': ('django.db.models.fields.FloatField', [], {}),
            'imagePositionPatientZ': ('django.db.models.fields.FloatField', [], {}),
            'imageSeries': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dicomImage.Series']"}),
            'relPath': ('django.db.models.fields.TextField', [], {}),
            'sliceLocation': ('django.db.models.fields.FloatField', [], {})
        },
        'dicomImage.series': {
            'Meta': {'object_name': 'Series'},
            'columns': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imageOrientationPatientXX': ('django.db.models.fields.FloatField', [], {}),
            'imageOrientationPatientXY': ('django.db.models.fields.FloatField', [], {}),
            'imageOrientationPatientYX': ('django.db.models.fields.FloatField', [], {}),
            'imageOrientationPatientYY': ('django.db.models.fields.FloatField', [], {}),
            'imageOrientationPatientZX': ('django.db.models.fields.FloatField', [], {}),
            'imageOrientationPatientZY': ('django.db.models.fields.FloatField', [], {}),
            'pixelSpacingX': ('django.db.models.fields.FloatField', [], {}),
            'pixelSpacingY': ('django.db.models.fields.FloatField', [], {}),
            'rows': ('django.db.models.fields.IntegerField', [], {}),
            'seriesDescription': ('django.db.models.fields.TextField', [], {}),
            'uid': ('django.db.models.fields.TextField', [], {'unique': 'True'})
        },
        'dicomImage.structure': {
            'Meta': {'object_name': 'Structure'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'json': ('django.db.models.fields.TextField', [], {}),
            'slice_location': ('django.db.models.fields.FloatField', [], {}),
            'structure_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dicomImage.StructureType']"}),
            'view': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dicomImage.View']"})
        },
        'dicomImage.structuretype': {
            'Meta': {'object_name': 'StructureType'},
            'colour': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dicomImage.StructureType']", 'null': 'True', 'blank': 'True'})
        },
        'dicomImage.view': {
            'Meta': {'object_name': 'View'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_series': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dicomImage.Series']"}),
            'name': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['dicomImage']