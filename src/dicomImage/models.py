from django.db import models

# Create your models here.
class Series(models.Model):
    uid = models.TextField(unique = True)
    pixelSpacingX = models.FloatField()
    pixelSpacingY = models.FloatField()
    imageOrientationPatientXX = models.FloatField()
    imageOrientationPatientYX = models.FloatField()
    imageOrientationPatientZX = models.FloatField()
    imageOrientationPatientXY = models.FloatField()
    imageOrientationPatientYY = models.FloatField()
    imageOrientationPatientZY = models.FloatField()
    seriesDescription = models.TextField()
    rows = models.IntegerField()
    columns = models.IntegerField() 

    def total_images(self):
        return len(self.image_set.all())

    def get_image(self, n):
        return self.image_set.order_by('sliceLocation')[n]

    def __unicode__(self):
        return self.uid

class Image(models.Model):
    relPath = models.TextField()
    imagePositionPatientX = models.FloatField()
    imagePositionPatientY = models.FloatField()
    imagePositionPatientZ = models.FloatField()
    sliceLocation = models.FloatField()
    imageSeries = models.ForeignKey('Series')
    def __unicode__(self):
        return "%s: %s" % (self.imageSeries, self.sliceLocation)
    
class StructureType(models.Model):
    name = models.TextField()
    def __unicode__(self):
        return self.name

class View(models.Model):
    name = models.TextField()
    image_series = models.ForeignKey('Series')
    def __unicode__(self):
        return self.name

class Structure(models.Model):
    slice_location = models.FloatField()
    view = models.ForeignKey('View')
    structure_type = models.ForeignKey('StructureType')
    json = models.TextField()

