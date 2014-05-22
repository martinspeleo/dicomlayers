# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Series'
        db.create_table(u'dicomImage_series', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('uid', self.gf('django.db.models.fields.TextField')(unique=True)),
            ('pixelSpacingX', self.gf('django.db.models.fields.FloatField')()),
            ('pixelSpacingY', self.gf('django.db.models.fields.FloatField')()),
            ('imageOrientationPatientXX', self.gf('django.db.models.fields.FloatField')()),
            ('imageOrientationPatientYX', self.gf('django.db.models.fields.FloatField')()),
            ('imageOrientationPatientZX', self.gf('django.db.models.fields.FloatField')()),
            ('imageOrientationPatientXY', self.gf('django.db.models.fields.FloatField')()),
            ('imageOrientationPatientYY', self.gf('django.db.models.fields.FloatField')()),
            ('imageOrientationPatientZY', self.gf('django.db.models.fields.FloatField')()),
            ('seriesDescription', self.gf('django.db.models.fields.TextField')()),
            ('rows', self.gf('django.db.models.fields.IntegerField')()),
            ('columns', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'dicomImage', ['Series'])

        # Adding model 'Image'
        db.create_table(u'dicomImage_image', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('relPath', self.gf('django.db.models.fields.TextField')()),
            ('imagePositionPatientX', self.gf('django.db.models.fields.FloatField')()),
            ('imagePositionPatientY', self.gf('django.db.models.fields.FloatField')()),
            ('imagePositionPatientZ', self.gf('django.db.models.fields.FloatField')()),
            ('sliceLocation', self.gf('django.db.models.fields.FloatField')()),
            ('imageSeries', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dicomImage.Series'])),
        ))
        db.send_create_signal(u'dicomImage', ['Image'])

        # Adding model 'StructureType'
        db.create_table(u'dicomImage_structuretype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'dicomImage', ['StructureType'])

        # Adding model 'View'
        db.create_table(u'dicomImage_view', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.TextField')()),
            ('image_series', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dicomImage.Series'])),
        ))
        db.send_create_signal(u'dicomImage', ['View'])

        # Adding model 'Structure'
        db.create_table(u'dicomImage_structure', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slice_location', self.gf('django.db.models.fields.FloatField')()),
            ('view', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dicomImage.View'])),
            ('structure_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dicomImage.StructureType'])),
            ('json', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'dicomImage', ['Structure'])


    def backwards(self, orm):
        # Deleting model 'Series'
        db.delete_table(u'dicomImage_series')

        # Deleting model 'Image'
        db.delete_table(u'dicomImage_image')

        # Deleting model 'StructureType'
        db.delete_table(u'dicomImage_structuretype')

        # Deleting model 'View'
        db.delete_table(u'dicomImage_view')

        # Deleting model 'Structure'
        db.delete_table(u'dicomImage_structure')


    models = {
        u'dicomImage.image': {
            'Meta': {'object_name': 'Image'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagePositionPatientX': ('django.db.models.fields.FloatField', [], {}),
            'imagePositionPatientY': ('django.db.models.fields.FloatField', [], {}),
            'imagePositionPatientZ': ('django.db.models.fields.FloatField', [], {}),
            'imageSeries': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dicomImage.Series']"}),
            'relPath': ('django.db.models.fields.TextField', [], {}),
            'sliceLocation': ('django.db.models.fields.FloatField', [], {})
        },
        u'dicomImage.series': {
            'Meta': {'object_name': 'Series'},
            'columns': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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
        u'dicomImage.structure': {
            'Meta': {'object_name': 'Structure'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'json': ('django.db.models.fields.TextField', [], {}),
            'slice_location': ('django.db.models.fields.FloatField', [], {}),
            'structure_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dicomImage.StructureType']"}),
            'view': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dicomImage.View']"})
        },
        u'dicomImage.structuretype': {
            'Meta': {'object_name': 'StructureType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {})
        },
        u'dicomImage.view': {
            'Meta': {'object_name': 'View'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_series': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dicomImage.Series']"}),
            'name': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['dicomImage']