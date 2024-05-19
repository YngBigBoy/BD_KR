from django.apps import AppConfig

# The AuthenticationConfig class is a subclass of AppConfig for the authentication app.
class AuthenticationConfig(AppConfig):
    # The default_auto_field attribute specifies the default auto-incrementing integer field type
    # for models in this app. In this case, it is set to Django's BigAutoField, which is an integer
    # field that uses 8 bytes to store the value.
    default_auto_field = 'django.db.models.BigAutoField'
    
    # The name attribute is required for all AppConfig subclasses and should be set to the
    # Python module name for the app. Here, it is set to 'authentication', which is the name
    # of the Django app that this AppConfig configuration applies to.
    name = 'authentication'
