# Install Python
https://www.python.org/downloads/

python3 --version

# Installing Django
pip3

pip3 install Django==4.0

python3 -m django

# Installing pillow
pip3 install pillow

# Managing migrations
python3 manage.py makemigrations

python3 manage.py migrate

# Running the Django local web server
python3 manage.py runserver

# Test
http://127.0.0.1:8000/media-example/

# Cloning code on to PythonAnywhere
## Create a beginner free account
https://www.pythonanywhere.com/registration/register/beginner/

Dashboard | New console | Bash

git clone <repo-url>

ls

## Configuring virtual environments
mkvirtualenv -p python3.10 mediaenv

pip install django pillow

# Setting up your web app
Path to your project's top folder – the folder that contains "manage.py": /home/<user>/media_project
Name of your project - the folder that contains your settings.py: /home/<user>/media_project/media_project
Name of your virtualenv: mediaenv

Click on the Web tab | Add a new web app | Select a Python Web framework | Manual configuration |
Select the right version of Python: 3.10 | Virtualenv section: mediaenv |
Code section:
    Source code: /home/<user>/media_project
    Working directory: /home/<user>
    Click the wsgi.py file: Delete everything except the Django section and uncomment that section

    # +++++++++++ DJANGO +++++++++++
    # To use your own django app use code like this:
    import os
    import sys
    path = '/home/<user>/media_project'
    if path not in sys.path:
        sys.path.append(path)
    os.environ['DJANGO_SETTINGS_MODULE'] = 'media_project.settings'
    from django.core.wsgi import get_wsgi_application
    application = get_wsgi_application()

substitute the correct path to your project, the folder that contains the manage.py file
    path = '/home/<user>/media_project'

put the correct value for DJANGO_SETTINGS_MODULE (where the settings.py file is located)
    os.environ['DJANGO_SETTINGS_MODULE'] = 
        'media_project.settings'

run deactivate in the Bash. To get back to a virtualenv, run the following command: workon mediaenv

Go to the PythonAnywhere Files tab and navigate through the source code directory
In settings.py, modify the ALLOWED_HOSTS variable:
    … 
    # SECURITY WARNING: don't run with debug turned on in
    production!
    DEBUG = True
    ALLOWED_HOSTS = ['*']
    …
Save the file

Go to the Web tab and hit the Reload button

Go to your project's URL: https://<user>.pythonanywhere.com/media-example/