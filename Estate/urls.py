from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Estate import views

router = DefaultRouter()
router.register(r'estates', views.EstateViewSet)
router.register(r'profiles', views.ProfileViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api/v1/', include('likes.api.urls')),

]
