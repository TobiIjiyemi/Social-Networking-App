from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from posts import views

#routers: can use default router to run all gets, posts, deletes
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'posts', views.PostViewSet)
router.register(r'businesses', views.BusinessViewSet)
router.register(r'categories', views.CategoryViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]