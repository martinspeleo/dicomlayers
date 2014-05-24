from django.conf.urls import patterns, url

import views

structures_url = r'^structures/(.+)/(.+)/(.+)\.json'

urlpatterns = patterns('',
#    url(r'^import_index$', views.import_index, name='import_index'),
    url(r'^$', views.home, name='home'),
    url(r'^load_all$', views.load_all, name='load_all'),
    url(r'^list_views$', views.list_views, name = 'list_views'),
    url(r'^view/(.+)$', views.view, name = 'view'),
    url(r'^edit/(.+)$', views.edit, name = 'edit'),
    url(r'^tile/(.+)/(.+)/(.+)/(.+)/(.+)/(.+)/(.+).png$', views.tile, name = 'tile'),
    url(structures_url + r'$', views.structures, name = 'structures'),
    url(structures_url + r'/null$', views.structures_modify, name = 'structures_modify'),
    url(r'^all_structures/(.+)/(.+)\.json', views.all_structures, name = 'all_structures'),
)
