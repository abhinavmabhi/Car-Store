"""
URL configuration for premium_cars project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.Home_page_view, name="home"),
    path("car/list/",views.List_all_cars,name="car-list"),
    path("details/<int:id>/",views.Car_details_view,name="car-details"),
    path("about/",views.about_view,name="about"),
    path("service/",views.Service_view,name="service"),
    path("contact/",views.Contact_view,name='contact'),
    path('gallery/',views.Gallery_view,name="gallery")


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
