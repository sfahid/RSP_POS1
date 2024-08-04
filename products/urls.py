# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.product_list, name='product_list'),
#     path('<int:id>/', views.product_detail, name='product_detail'),
#     path('create/', views.product_create, name='product_create'),
#     path('<int:id>/update/', views.product_update, name='product_update'),
#     path('<int:id>/delete/', views.product_delete, name='product_delete'),
# ]


# # from django.contrib import admin
# # from django.urls import path, include

# # urlpatterns = [
# #     path('admin/', admin.site.urls),
# #     path('products/', include('products.urls')),
# # ]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_spa'),
    path('<int:id>/', views.product_detail, name='product_detail'),
    path('create/', views.product_create, name='product_create'),
    path('<int:id>/update/', views.product_update, name='product_update'),
    path('<int:id>/delete/', views.product_delete, name='product_delete'),
    
    # API endpoints
    path('api/', views.product_list_api, name='product_list_api'),
    path('api/<int:id>/', views.product_detail_api, name='product_detail_api'),
    path('api/create/', views.product_create_api, name='product_create_api'),
    path('api/<int:id>/update/', views.product_update_api, name='product_update_api'),
    path('api/<int:id>/delete/', views.product_delete_api, name='product_delete_api'),
]
