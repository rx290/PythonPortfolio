# Introduction

## Installation

    To install Django or Django restful one must run these commands
    ~ pip install django / djangorestframework

## New Project in Django

    To start a new project one must use following commands

    ~ django-admin startproject "Project Name Without quotes"

## Adding new modules / apps to the project

    Simply typed INSTALLED_APPS = [
            
            'App name',
    ]

## Adding a new Admin

    python -m manage createsuperuser

## Adding new apps

    Python -m manage startapp "App name without quotes"

## Making changes / adding items to database

    Whenever models.py is modified in the entire project regardless of the app one must run following commands:

    python -m manage makemigrations

    python -m manage migrate

## Registering App with Admin

    Go to admin.py and import app model and register it with following command

    admin.site.register("Name of the class imported from models")

## Django Shell

    Make sure we are in root folder and run following command to open shell

    python -m manage shell

    now a shell with all django properties will open where we can use it for our testing / deployment purposes

    ### Commands and Working ###

        To create an object we are simply going to use following command:

        from blog.models import Blog

        # Now to create a blog we will use following command
        Blog.objects.create(pram1,pram2,...)

        # to view our blogs we will use following command:
        Blog.objects.all()

## Django Fields

    Lets get back to django models and now instead of creating a generic form we are going to specify stuff for our fields

    we have lots of fields in django model but most common of them are as follows:

    1. Text field
    2. Char field
    3. Email field
    4. file field
    5. image field
    6. integer field
    7. float field
    8. date field
    9. datetime field
    10. Time field
    11. Url field
    12. Auto field

## Altering Database or models file

    Let say we have decided to add a text field called topics to our model class how do we make sure that it is added to previous entries and will be added to the future ones?

    Django provides two options for that particular things which are as follows:
    1.  Add default to values to all previous entries
    2.  Add default to the current value and make migration which will only add fields to stuff added in future

## Creating Views and setting home in Django

    So we want to change the default landing page of our django app and we want some html or other frontend technology to be our default landing page.
    so what we gotta do is to create a view function in the views.py of our app and link it to the urls.py add the custom url of our project.
    Example:

    in blog/views.py
        import django.http import HttpResponse
        
        def home_view(*args, **Kwargs):
            return HttpResponse("<h1>Hello World!</h1>")

    now in main_working_directory/project/url.py

    from blog import views

    # now edit the urlpattern list with this
    path('',views.home_view,name='home')

### Url pattern and routing in Django

    To understand the actual routing in Django we are going to break a sample route into understandable code chunks

    our route is like this : path("", view_name, name='some name')
    so we have four parts of the commands here with their explanation:
    1. Path keyword which is actually handling the HttpRequest we are making while interacting with the domain
    2. String Pram for adding domain section with the actual url
    3. Calling og the actual view function imported view from the app
    4. some name to refer that view

    So to route to a contact page we are going to do as follows:

    path("contact/",view_contact,name='contact')

## Django Template

    Till now we have been dealing with simple html elements which are not nice to look at so we are going to use Django provided tools to display a webpage as per our routes.
    This procedure is called templates and it can be achieved as follows:

    1. Create a templates folder at the root of the project
    2. Create your html files there
    3. User render function to display the webpage created eg. render(request,"name of the html file", {})
    4. Now go to settings and go to templates sections in the dirs list add this line os.path.join(BASE_DIR,"templates")
    5. hit restart and you're good to go

### Django Templating Engine Basics

    {{ request.user }}: By defaults active, checks which user is accessing the webpage

    {{ request.user.isAuthenticated }}: check whether the user is authenticated or not

    {{ extends 'base.html' }}: used to inherit everything from the base html file

    {%block content %} {% endblock %} / {%block content %} {% endblock content %}: used to manipulate body element of html pages

