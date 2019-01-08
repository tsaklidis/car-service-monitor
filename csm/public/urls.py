from django.conf.urls import url
from csm.public import views

urlpatterns = [
    # Home page
    url('^$', views.home, name='home'),
    url('^denied', views.no_rights, name='no_rights'),
]
