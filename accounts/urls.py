from django.urls import path
from . import views
# from django.conf import settings
# from django.conf.urls.static import static

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup_view, name="signup"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    # path('submitvote/',views.submit_vote,name="submitvote")
] 

# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)