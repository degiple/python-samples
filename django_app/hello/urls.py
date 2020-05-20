from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('form', views.form, name='form'),
    path('query', views.query, name='query'),
    path('<int:id>/<nickname>/', views.query_smart, name='query_smart'),
    path('My_name_is_<name>.I_am_<int:age>_years_old.', views.me, name='me')
]
