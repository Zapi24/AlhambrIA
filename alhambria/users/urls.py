from django.urls import path
from . import views

urlpatterns = [
    # Para al portada "landing page"
    path('', views.landing_page, name='landing'),
]