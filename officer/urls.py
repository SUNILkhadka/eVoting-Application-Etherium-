from django.urls import path
from . import views

app_name = 'officer'

urlpatterns = [
    path('', views.officer, name="officercrud"),
    path('addcand/', views.add_candidate, name="addcand"),
    path('delcand/', views.delete_candidate, name="delcand"),
    path('editcand/<int:id>/', views.edit_candidate, name="editcand"),
    # path('adduser/', views.add_user, name="adduser"),
    path('deluser/', views.delete_user, name="deluser"),
    path('edituser/<int:id>/', views.edit_user, name="edituser"),
]