from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('index/', views.main_view),
    path('index/home/', views.home_view),
    path('index/home/submit/', views.home_view_submit),
    path('index/attendance/', views.attendance_view),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
