#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""

import os
import sys

def main():
    """
    Run administrative tasks. This function sets the default environment variable for Django settings module and then calls the `execute_from_command_line` function from Django's core management module.
    """
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bd_kr_service.settings')
    
    try:
        # Import the `execute_from_command_line` function from Django's core management module.
        # If the import fails, an ImportError is raised.
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # If the import fails, this block is executed. It raises the ImportError with a more detailed error message.
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    
    # Call the `execute_from_command_line` function with the command line arguments.
    execute_from_command_line(sys.argv)

# Call the `main` function if the script is run as the main program.
if __name__ == '__main__':
    main()
