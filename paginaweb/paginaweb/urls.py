"""paginaweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path,include
from home import views as home_views
"""from Administrador import views as Admin_views"""
from django.conf import settings
from Administrador.urls import Administrador_patterns
from Developer.urls import Developer_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
     path('accounts/',include('django.contrib.auth.urls'),name="login"),
     path('accounts/',include('registration.urls'),name="Registro"),
    path('',include(Administrador_patterns)),
    path('usuario/',include(Developer_patterns)),


]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

