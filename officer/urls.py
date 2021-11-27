from django.urls import path
from . import views

app_name = 'officer'

urlpatterns = [
    path('', views.officer, name="officercrud"),
    path('addcand/', views.add_candidate, name="addcand"),
    path('delcand/', views.delete_candidate, name="delcand"),
    path('editcand/<int:id>/', views.edit_candidate, name="editcand"),
]