
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import index, student_login_view, mentor_login_view, apply_for_mentor_view, register_view, login_view, logout_view, dashboard_view

urlpatterns = [
    path('', index, name='home'),
    path('student-login/', student_login_view, name='student_login'),
    path('mentor-login/', mentor_login_view, name='mentor_login'),
    path('apply-for-mentor/', apply_for_mentor_view, name='apply_for_mentor'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)