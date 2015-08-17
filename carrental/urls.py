from django.conf.urls import url
from . import views


# TIM NOTE: This url design is not RESTful. See link for more details.
# Particularly:
# 1) Filtering should be in GET params, not in URL.
# 2) rent_car endpoint should not be its own url. It should a POST on a "available_cars" endpoint.
# 3) URLs should be resource-oriented, in this case (and correctly in your design) available_cars and reserved_cars.
# With no params, you get a list, and with the id param you get one instance.
# http://www.vinaysahni.com/best-practices-for-a-pragmatic-restful-api#restful
urlpatterns = [
    url(r'^avail_cars/(?P<start>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\+\d{2}:\d{2})/(?P<end>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\+\d{2}:\d{2})/$', views.available_cars, name='avail_cars'),
    url(r'^avail_cars/(?P<car_id>[0-9]+)/(?P<start>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\+\d{2}:\d{2})/(?P<end>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\+\d{2}:\d{2})/$', views.available_cars, name='avail_cars'),
    url(r'^avail_cars/$', views.available_cars, name='avail_cars'),
    url(r'^avail_cars/(?P<car_id>[0-9]+)/$', views.available_cars, name='avail_cars'),
    url(r'^reserved_cars/(?P<start>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\+\d{2}:\d{2})/(?P<end>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\+\d{2}:\d{2})/$', views.reserved_cars, name='reserved_cars'),
    url(r'^reserved_cars/$', views.reserved_cars, name='reserved_cars'),
    url(r'^rent_car/(?P<car_id>[0-9]+)/(?P<start>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\+\d{2}:\d{2})/(?P<end>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\+\d{2}:\d{2})/$', views.rent_car, name='rent_car')
]
