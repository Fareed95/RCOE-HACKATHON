
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import index, mentor_login_view, apply_for_mentor_view, SignupPage, LoginPage , HomePage, LogoutPage, HomePageMentor
app_name = 'chat'
urlpatterns = [
    path('', index, name='home'),
    path('signup/',SignupPage,name='signup'),
    path('login/',LoginPage,name='login'),
    path('mentor-login/', mentor_login_view, name='mentor_login'),
    path('apply-for-mentor/', apply_for_mentor_view, name='apply_for_mentor'),
    path('studentdash/',HomePage,name='studentdash'),
    path('mentordash/',HomePageMentor,name='mentordash'),
    path('logout/',LogoutPage,name='logout'),
    
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)