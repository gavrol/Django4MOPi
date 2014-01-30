from django.conf.urls import patterns, include, url
import mopi.views

#there wont be admin
#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'MOPIsite.views.home', name='home'),
    url(r'^$', mopi.views.home, {'template_name': 'index.html'}),
    url(r'^index$', mopi.views.home, {'template_name': 'index.html'}),
    url(r'^feedback$', mopi.views.home,{'template_name': 'feedback.html'}),
    url(r'^projects$', mopi.views.home,{'template_name': 'projects.html'}),
    url(r'^philosophy$', mopi.views.home,{'template_name': 'faq.html'}),
     url(r'^faq$', mopi.views.home,{'template_name': 'faq.html'}),
    url(r'^shortCV$', mopi.views.home,{'template_name': 'shortCV.html'}),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
)
