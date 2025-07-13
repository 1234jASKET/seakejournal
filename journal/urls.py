from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('politique/', views.politique, name='politique'),
    path('contact/', views.contact, name='contact'),
    path('publicite/', views.publicite, name='publicite')
]