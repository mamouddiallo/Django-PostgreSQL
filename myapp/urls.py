
from django.urls import path

from .import views
from .views import my_form_view, success_view, report_view


urlpatterns = [
    path('', views.index, name="index"),
    path('new/', views.new, name="new"),
    path('my_form', my_form_view, name='my_form'),
    path('success/', success_view, name='success_view'),
    path('report/', report_view, name='report')
]