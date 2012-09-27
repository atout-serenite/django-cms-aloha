from cmsaloha.views import alohapost
from django.conf.urls import patterns, url

urlpatterns = patterns('cmsaloha.views',
                       url(r'update',alohapost),
                       )
print "MY URLS!"
