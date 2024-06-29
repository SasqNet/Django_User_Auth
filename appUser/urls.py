from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls)),
]


# Here's a breakdown of each line:

# from django.urls import include, path: This line is importing the include and path functions from Django's urls module. These functions are used to define URL patterns.

# from rest_framework.routers import DefaultRouter: This line is importing the DefaultRouter class from Django REST Framework. This class automatically creates URL patterns for your viewsets.

# from .views import UserViewSet: This line is importing the UserViewSet class from the current module's views.py file.

# router = DefaultRouter(): This line is creating an instance of DefaultRouter.

# router.register(r'users', UserViewSet, basename='users'): This line is registering the UserViewSet with the router under the base URL users. This means that the UserViewSet will handle requests to URLs that start with users/.

# urlpatterns = [path('', include(router.urls)),]: This line is defining the URL patterns for your application. The include(router.urls) part is including all the URL patterns that were automatically generated by the router. The path('', include(router.urls)) part means that these URL patterns will be included at the root URL (/).

# In summary, this code is setting up URL routing for your Django application so that requests to URLs that start with users/ are handled by the UserViewSet. The DefaultRouter automatically generates the appropriate URL patterns for all the standard create, retrieve, update, and delete operations provided by UserViewSet.