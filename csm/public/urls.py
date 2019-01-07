from django.conf.urls import url
from csm.public import views

urlpatterns = [
    # Home page
    url('^$', views.home, name='home'),
]
