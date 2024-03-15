"""
URL configuration for Captive project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from Portal.views import captive_portal, success, view_profiles

urlpatterns = [
    path('', captive_portal, name='captive_portal'),
    path('success/', success, name='success'),
    path('view_profiles/', view_profiles, name='view_profiles'),
]


# if settings.DEBUG:
#     urlpatterns += [
#         path('sslserver/', include('sslserver.urls')),
#     ]