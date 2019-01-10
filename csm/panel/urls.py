from django.conf.urls import url
from csm.panel import views

urlpatterns = [
    # panel page
    url('^$', views.home, name='home'),
    url('^owners/', views.owners, name='owners'),
    url('^cars/', views.cars, name='cars'),
    url('^view/(?P<car_id>[\d]+)/car/$', views.car_single, name='car_single'),

]
