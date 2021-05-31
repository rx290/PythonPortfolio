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