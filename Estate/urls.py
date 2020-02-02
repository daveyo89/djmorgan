from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Estate import views

router = DefaultRouter()
router.register(r'estates', views.EstateViewSet)
router.register(r'profiles', views.ProfileViewSet)
router.register(r'likes', views.LikedViewset)

urlpatterns = [
    path('', include(router.urls)),
]
