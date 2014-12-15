from django.conf.urls import patterns, include, url
from django.contrib import admin
from scrabble_server import views

admin.autodiscover()

genericViews = patterns('',
	url(r'^$', views.index, name='index')
)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'elemental_scrabble.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^', include(genericViews)),
    url(r'^admin/', include(admin.site.urls)),
    
)
