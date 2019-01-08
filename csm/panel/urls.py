from django.conf.urls import url
from csm.panel import views

urlpatterns = [
    # panel page
    url('^$', views.home, name='home'),
    url('^owners/', views.owners, name='owners'),
]
