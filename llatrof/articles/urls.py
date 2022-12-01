from django.urls import path
from . import views

urlpatterns = [
    path('', views.articles_list),
    path('category', views.category),
    path('category/<str:category>', views.category_goods),
    path('brand', views.brand),
    path('brand/<str:brand>', views.brand_goods),
]