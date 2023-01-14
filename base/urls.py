from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.endpoints),
    path('advocates/', views.advocates_list),
    path('advocates/<str:username>', views.advocate_detail),


]
