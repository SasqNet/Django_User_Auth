"""
URL configuration for config project.

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
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('appUser.urls')),
    path('dj-rest-auth/', include(('dj_rest_auth.urls', 'dj_rest_auth'))),
]


# Here's a breakdown of each line:

# from django.contrib import admin: This line is importing Django's built-in admin module.

# from django.urls import path, include: This line is importing the path and include functions from Django's urls module. These functions are used to define URL patterns.

# urlpatterns = [...]: This line is defining a list of URL patterns for your application.

# path('admin/', admin.site.urls): This line is adding a URL pattern that maps URLs starting with admin/ to Django's built-in admin site.

# path('', include('appUser.urls')): This line is including the URL patterns defined in the urls.py file of the appUser application at the root URL (/). This means that the appUser application will handle requests to URLs that don't start with any other defined prefix.

# path('dj-rest-auth/', include(('dj_rest_auth.urls', 'dj_rest_auth'))),: This line is including the URL patterns defined in the dj_rest_auth.urls module under the base URL dj-rest-auth/. This means that the dj_rest_auth application will handle requests to URLs that start with dj-rest-auth/. The dj_rest_auth application provides RESTful API endpoints for authentication features like login, logout, password reset, etc.

# In summary, this code is defining the URL routing for your Django project. It's mapping URLs to views, which handle the HTTP requests and produce responses.