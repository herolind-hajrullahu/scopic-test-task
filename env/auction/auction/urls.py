"""auction URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from home import views as home_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home_views.home, name='home'),
    path('item/<slug:title>/', home_views.item_details_page, name='items'),
    path('login/<slug:username>/<slug:password>', home_views.login, name='login'),
    path('search/<slug:filter>', home_views.search, name='search'),
    path('bid/<slug:title>/', home_views.bid, name='bid'),
    path('auto_bid/<slug:title>/<int:max_bid>', home_views.auto_bid, name='auto_bid'),
]
