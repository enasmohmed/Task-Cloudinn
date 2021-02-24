from django.urls import path, include
from rest_framework import routers
from . import views
from rest_framework import routers
from .views import EmpriesViewSet



app_name = 'Empires'

router = routers.DefaultRouter()
router.register('data_api', EmpriesViewSet)


urlpatterns = [
    path('', views.index, name='index'),
    path('data/', views.all_data, name='all_data'),
    path('search/', views.search ,name='search'),
    path('api/', include(router.urls), name='api_router'),
]