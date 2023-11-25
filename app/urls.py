from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('records/',views.student_records, name= 'records'),
    path('add_record/',views.add_record, name='add_record'),
    path('edit_record/<str:pk>',views.edit_record, name='edit_record'),
    path('details/<str:pk>',views.details, name='details'),
    path('add_details/<str:pk>',views.add_details, name='add_details'),
    path('delete/<str:pk>',views.delete_record, name='delete_record'),
    path('logout/',views.logout_user, name='logoutuser')
]