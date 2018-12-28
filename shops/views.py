from django.shortcuts import render

# Create your views here.
from django.views import generic
from django.contrib.gis.geos import fromstr
from django.contrib.gis.db.models.functions import Distance
from .models import Shop
from django.contrib.gis.geos import Point



longitude = 139.839478
latitude = 35.652832

user_location = Point(longitude, latitude, srid=4326)


class Home(generic.ListView):
    model = Shop
    context_object_name = 'shops'
    queryset = Shop.objects.annotate(distance=Distance('location',
                                                       user_location)).order_by('distance')[0:6]
    template_name = 'shops/index.html'
