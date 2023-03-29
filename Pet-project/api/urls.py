from django.urls import path
from . import views


urlpatterns = [
    path('', views.apiOverview, name='apiOverview'),
    path('stock-list/', views.DisplayAll, name='stock-list'),
    path('product-detail/<int:pk>/', views.ViewProduct, name='product-detail'),
    path('product-create/', views.CreateProduct, name='product-create'),
    path('product-update/<int:pk>', views.UpdateProduct, name='product-update'),
    path('product-delete/<int:pk>', views.DeleteProduct, name='product-delete'),
]