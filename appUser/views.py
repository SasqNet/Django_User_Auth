from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    

# Here's a breakdown of each line:

# from rest_framework import viewsets: This line is importing the viewsets module from Django REST Framework. Viewsets are a type of class-based view that provide operations for creating, retrieving, updating, and deleting instances of a model.

# from .models import User: This line is importing the User model from the current module's models.py file.

# from .serializers import UserSerializer: This line is importing the UserSerializer class from the current module's serializers.py file. Serializers allow complex data types, like Django model instances, to be converted to Python data types that can then be easily rendered into JSON, XML, or other content types.

# class UserViewSet(viewsets.ModelViewSet):: This line is defining a new class UserViewSet that inherits from viewsets.ModelViewSet. ModelViewSet is a type of viewset that provides the complete set of default read and write operations.

# queryset = User.objects.all(): This line is defining the default queryset that will be used for this viewset. In this case, it's getting all instances of the User model.

# serializer_class = UserSerializer: This line is specifying that the UserSerializer class should be used to serialize and deserialize instances of the User model for this viewset.

# In summary, this code is defining a RESTful API endpoint for the User model that supports creating, retrieving, updating, and deleting users. The UserSerializer class is used to convert between User instances and JSON.    