from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

app_name = 'api_v1'

router_v1 = DefaultRouter()
router_v1.register('materials', views.MaterialViewSet, basename='materials')
router_v1.register('category', views.CategoryViewSet, basename='category')
router_v1.register('tree', views.TreeViewSet, basename='tree')

urlpatterns = [
    path('', include(router_v1.urls)),
    path(
        'import-materials/',
        views.MaterialImportView.as_view(),
        name='import-materials'
    )
]