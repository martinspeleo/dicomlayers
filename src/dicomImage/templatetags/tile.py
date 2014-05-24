from django import template
from django.core.urlresolvers import reverse

register = template.Library()

def tile(series_pk, window, level):
    #the reverse function URL encodes the result, however we want to produce a pattern for OpenLayers, hence %7B needs changing back to { and %7D to }
    return reverse('tile', args=[series_pk, "depth", window, level, "${z}", "${y}", "${x}"]).replace("%7B", "{").replace("%7D", "}").replace("%24", "$")

def structures(series_pk, structure_type_pk):
    #the reverse function URL encodes the result, however we want to produce a pattern for OpenLayers, hence %7B needs changing back to { and %7D to }
    return reverse('structures', args=[series_pk, "depth", "StructureType"])


register.simple_tag(tile)
register.simple_tag(structures)
