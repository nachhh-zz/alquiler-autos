from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^avail_cars/(?P<start>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\+\d{2}:\d{2})/(?P<end>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\+\d{2}:\d{2})/$', views.available_cars, name='avail_cars'),
    url(r'^avail_cars/$', views.available_cars, name='avail_cars'),
    url(r'^reserved_cars/(?P<start>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\+\d{2}:\d{2})/(?P<end>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\+\d{2}:\d{2})/$', views.reserved_cars, name='reserved_cars'),
    url(r'^reserved_cars/$', views.reserved_cars, name='reserved_cars'),
    url(r'^rent_car/(?P<car_id>[0-9]+)/(?P<start>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\+\d{2}:\d{2})/(?P<end>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\+\d{2}:\d{2})/$', views.rent_car, name='rent_car')
]
                    
