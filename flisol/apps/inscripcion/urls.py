from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('flisol.apps.inscripcion.views',
	url(r'^$', 'index_view', name = 'vista_principal'),
)