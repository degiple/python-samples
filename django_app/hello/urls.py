# from django.conf.urls import url
from django.urls import path
from . import views
# from .views import HelloView

urlpatterns = [
    # url(r'', HelloView.as_view(), name='hello'),
    # path('form', views.form, name='form'),
    # path('query', views.query, name='query'),
    # path('<int:id>/<nickname>/', views.query_smart, name='query_smart'),
    # path('My_name_is_<name>.I_am_<int:age>_years_old.', views.me, name='me')
    path('', views.index, name='index'),
    path('<int:num>', views.index, name='index'),
    path('create', views.create, name='create'),
    path('edit/<int:num>', views.edit, name='edit'),
    path('delete/<int:num>', views.delete, name='delete'),
    path('find', views.find, name='find'),
    path('check', views.check, name='check'),
    path('message/', views.message, name='message'),
    path('message/<int:page>', views.message, name='message'),
]
