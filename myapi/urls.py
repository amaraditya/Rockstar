from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import moviesViewSet
from .views import UserViewSet

router =routers.DefaultRouter()
router.register('User',UserViewSet)
router.register('movies',moviesViewSet)


urlpatterns =[
    path('',include(router.urls)),

]