"""accoacco URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from ra.admin.admin import ra_admin_site
from debug_toolbar import urls as durls
from django.conf.urls import include
from reports import views

handler500 = 'ra.utils.views.server_error'
handler404 = 'ra.utils.views.not_found_error'

urlpatterns = [
    path('ajax/validate_username/', views.validate_username),
    path('reports/clients/', views.accountp),
    path('reports/projects/', views.txntype),
    path('', ra_admin_site.urls),
    path('__debug__/', include(durls), name='debug_toolbar'),
]
