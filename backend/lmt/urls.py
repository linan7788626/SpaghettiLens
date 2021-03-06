from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'lmt.views.home', name='home'),
    # url(r'^lmt/', include('lmt.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^get_initdata/', 'ModellerApp.views.getInitData'),
    url(r'^get_modeldata/(?P<model_id>\d+)', 'ModellerApp.views.getSingeModelData'),
    url(r'^get_modeldata/', 'ModellerApp.views.getModelData'),
    url(r'^save_model/', 'ModellerApp.views.saveModel'),
    url(r'^save_model_final/', 'ModellerApp.views.saveModelFinal'),
    url(r'^load_model/', 'ModellerApp.views.loadModel'),
    url(r'^result/(?P<result_id>\d+).json', 'ModellerApp.views.getSimulationJSON'),
    url(r'^result/(?P<result_id>\d+)/(?P<filename>.+)', 'ModellerApp.views.getSimulationFiles'),
    
    url(r'^data/(?P<result_id>\d+)', 'ModellerApp.views.getData'),

    url(r'^api', 'ModellerApp.views.api'),
    
    url(r'^tools/', include('tools.urls')),
)


# if settings.role == 'standalone_app':
#   (r'^(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/path/to/static_html'}),