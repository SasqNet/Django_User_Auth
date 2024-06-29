# admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User  # Changed from CustomUser to User

class CustomUserAdmin(UserAdmin):
    # Define the fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser',
                                    'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    ordering = ('username',)

admin.site.register(User, CustomUserAdmin)  # Changed from CustomUser to User




# Here's a breakdown of each line:

# from django.contrib import admin: This line is importing Django's built-in admin module.

# from django.contrib.auth.admin import UserAdmin: This line is importing the UserAdmin class from Django's built-in authentication module. UserAdmin is a base class for the admin interface of the user model.

# from .models import User: This line is importing the User model from the current module's models.py file.

# class CustomUserAdmin(UserAdmin):: This line is defining a new class CustomUserAdmin that inherits from UserAdmin. This class is used to customize the admin interface for the User model.

# fieldsets = (...): This attribute is defining the layout for the change form page in the admin site. This page is used to edit an existing user.

# add_fieldsets = (...): This attribute is defining the layout for the add form page in the admin site. This page is used to create a new user.

# list_display = (...): This attribute is defining the fields to be displayed in the user list page in the admin site.

# search_fields = (...): This attribute is defining the fields that can be searched in the user list page in the admin site.

# ordering = (...): This attribute is defining the default ordering for the user list page in the admin site.

# admin.site.register(User, CustomUserAdmin): This line is registering the User model with the admin site, using the CustomUserAdmin class to customize the admin interface.

# In summary, this code is customizing the Django admin interface for the User model to change the layout of the form pages, the fields displayed in the user list page, the fields that can be searched, and the default ordering.