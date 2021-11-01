from django.urls import path
from . import views

urlpatterns = [
	path('',views.vote),
	path('vote/', views.votingPage),
]