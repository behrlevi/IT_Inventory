from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    #path('login', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('equipment/<int:pk>',views.list_equipment, name='equipment'),
    path('delete_record/<int:pk>',views.delete_record, name='delete_record'),
    path('add_record/',views.add_record, name='add_record'),
    path('edit_equipment/<int:pk>',views.edit_equipment, name='edit_equipment'),
    path('add_equipment/<int:pk>',views.add_equipment, name='add_equipment'),
    path('delete_equipment/<int:pk>',views.delete_equipment, name='delete_equipment'),
]
