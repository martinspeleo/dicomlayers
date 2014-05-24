from django.shortcuts import render
from django.conf import settings
from django import forms
from django.http import HttpResponse, HttpResponseRedirect
import os, sys
import dicom
import PIL
import PIL.Image
import numpy
from math import log, ceil
from subprocess import call
import json

from models import Image, Series, View, StructureType, Structure

TILE_SIZE = 256

def load_all(request):
    for fn in os.listdir(settings.DICOM_INPUT_DIR):
        path = os.path.join(settings.DICOM_INPUT_DIR, fn)
        if os.path.isfile(path):
            try:
                d = dicom.read_file(path)
            except:
                print "DICOM read error %s:" % path, sys.exc_info()[0]
            series, created = Series.objects.get_or_create(
                                   uid = d.SeriesInstanceUID,
                                   pixelSpacingX = d.PixelSpacing[0],
                                   pixelSpacingY = d.PixelSpacing[1],
                                   imageOrientationPatientXX = d.ImageOrientationPatient[0],
                                   imageOrientationPatientYX = d.ImageOrientationPatient[1],
                                   imageOrientationPatientZX = d.ImageOrientationPatient[2],
                                   imageOrientationPatientXY = d.ImageOrientationPatient[3],
                                   imageOrientationPatientYY = d.ImageOrientationPatient[4],
                                   imageOrientationPatientZY = d.ImageOrientationPatient[5],
                                   seriesDescription = d.SeriesDescription,
                                   rows = d.Rows,
                                   columns = d.Columns)
            if created:
                series.save()
            image, created = Image.objects.get_or_create(
                                   relPath = d.SOPInstanceUID,
                                   imagePositionPatientX = d.ImagePositionPatient[0],
                                   imagePositionPatientY = d.ImagePositionPatient[1],
                                   imagePositionPatientZ = d.ImagePositionPatient[2],
                                   sliceLocation = d.SliceLocation,
                                   imageSeries = series)
            if created:
                image.save()
                if d.file_meta.TransferSyntaxUID == 'JPEG 2000 Image Compression':
                    call(["gdcmconv", "-w", path, os.path.join(settings.DICOM_DATA_DIR, d.SOPInstanceUID)])
                    call(["rm", path])
                else:
                    call(["mv", path, os.path.join(settings.DICOM_DATA_DIR, d.SOPInstanceUID)])
            else:
                print "DICOM SOP UID already exists %s:" % path
    return HttpResponse(status=204) 

def list_views(request):
    return render(request, 'listViews.html', {"views": View.objects.all()})


def home(request):
    return render(request, 'home.html', {"views": View.objects.all(), 
                                         "structure_types": StructureType.objects.all()})

def view(request, view_pk):
    v = View.objects.get(pk = view_pk)
    return render(request, 
                  'view.html', 
                  {"view": v, 
                   "structure_types": StructureType.objects.all()})

def structures(request, view_pk, depth, structure_type_pk):
    if request.method == 'GET':
        return render(request, 
                      'structures.json', 
                      {"structures": Structure.objects.filter(slice_location = depth,
                                                              structure_type__pk = structure_type_pk,
                                                              view__pk = view_pk)})
    else:
        new_structure = json.loads(request.raw_post_data)
        s = Structure(slice_location = depth,
                      view = View.objects.get(pk = view_pk),
                      structure_type = StructureType.objects.get(pk = structure_type_pk),
                      json = new_structure["features"][0]['geometry']['coordinates'])
        s.save()
        return HttpResponse(status=204)


def structures_modify(request, view_pk, depth, structure_type_pk):
    if request.method == 'PUT':
        modified_structure = json.loads(request.raw_post_data)
        s = Structure.objects.get(pk=modified_structure['properties']['pk'])
        s.json = modified_structure['geometry']['coordinates']
        s.save()
        return HttpResponse(status=204)


def tile(request, series_pk, depth, window, level, z, x, y):
    window, level = float(window), float(level)
    x, y, z = int(x), int(y), int(z)
    depth = int(depth)
    s = Series.objects.get(pk = series_pk)
    i = s.get_image(depth)
    d = dicom.read_file(os.path.join(settings.DICOM_DATA_DIR, i.relPath))
    data = d.pixel_array
    zoom_level = z - ceil(log(max(data.shape) / float(TILE_SIZE), 2))
    tile_data_size = TILE_SIZE * 2 ** -zoom_level
    tile_data = data[x * tile_data_size: (x + 1) * tile_data_size, y * tile_data_size: (y + 1) * tile_data_size]
    windowed_data = numpy.piecewise(tile_data,
                        [tile_data <= (level - 0.5 - (window - 1) / 2),
                         tile_data > (level - 0.5 + (window - 1) / 2)],
                        [0, 255, lambda x: ((x - (level - 0.5)) / (window - 1) + 0.5) * (255 - 0)])

    img = PIL.Image.fromarray(numpy.uint8(windowed_data)).resize((TILE_SIZE, TILE_SIZE))
    
    response = HttpResponse(mimetype="image/png")
    img.save(response, "PNG")
    return response
    

