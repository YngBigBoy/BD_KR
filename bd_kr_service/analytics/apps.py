from django.apps import AppConfig

# This is an AppConfig class for the 'analytics' app in a Django project.
# The AppConfig class is used to configure and customize the behavior of a Django app.
class AnalyticsConfig(AppConfig):
    # The default_auto_field attribute specifies the default auto-incrementing field type
    # for models in this app. In this case, it is set to 'django.db.models.BigAutoField',
    # which is a 64-bit integer field that automatically increments.
    default_auto_field = 'django.db.models.BigAutoField'
    
    # The name attribute specifies the name of this app, which is 'analytics'.
    name = 'analytics'
