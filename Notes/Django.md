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

    {$ include "external template" %} i.e. {$ include "navbar.html" %}

#### Rendering Content inside of templates

    To render other data to the view we simply need to modify our context which is mentioned in *Django Template Section, point 3*.
    We can just create a dictionary and pass it as a context to the view which will later be merged by Django and displayed as a view.
    The keys used inside of the dictionary are our context variables in the html template so we can just go to our html page and use those keys.

    example:
            In aboutUs_view:
                my_context = {
                    "my title" : "This is About US!"
                    "text" : "This is some random text."
                }

            now pass the dict like this:

                    path("contact/",view_contact,name='contact',my_context)

            Now in template.html we can call these keys as context variables provided by django as follows:

            <body> 
                <p>
                    {{ my_title }}
                    <br>
                    {{ text }}
                </p>
            </body>

### Using for loop in templates

    syntax:
        {% for var_name in context_list_var %}
         statements
        {% endfor %}
    
    {{ forloop.counter }} a statement to use for iteration display

### Conditions in templates

    if condition

    Syntax:
        {% if condition %}
        statements
        {% endif %}

    example:
        {% if True %}
        <li> Bazinga </li>
        {% endif %}

        {% if abc==9 %}
        <li> Bazinga </li>
        {% endif %}

    if else condition

    syntax:
        {% if condition %}
        statement
        {% else %}
        statement
        {% endif %}

    nested if else

    syntax:

        {% if condition %}
        statement
        {% elif %}
        statement
        {% else %}
        statement
        {% endif %}

### Django Template Built-in tags and filters

    Django has a lot to offer and we have been using tags from the very beginning some of these common tags are as follows:
    
    1. block
    2. comment
    3. cycle
    4. extends
    5. firstof
    6. for and for empty
    7. if | ifequal | ifnotequal | ifchanged
    8. include
    9. load
    10. now
    11. regroup
    12. with
    13. Widthration
    14. url
    15. spaceless

    To add filter we just use "|" to a tag and write filter next to it.
    we can also stack together some filters by adding "|" to the first filter and add another after it.
    There are lots of builtin filters for django some of common filters are as follows:

    1. add | addslashes
    2. capfirst | title | upper | lower
    3. cut
    4. date | time | timesince | timeuntil
    5. default | default_if_none
    6. dictsort | ductsortreversed
    7. divisibleby
    8. escape | escapejs
    9. filesizeformat
    10. join | join_script
    11. length | length_is
    12. linenumbers
    13. random
    14. safe | safeseq
    15. slugify
    16. truncatechars | truncatechars_html | truncatewords
    17. unorderdlist
    18. urlencode | urlize | urlizetrunc
    19. wordcount | wordwrap
    20. yesno

### Render data from database model

#### How to view blogs

    in blog app open view and then type:

    from .models import Blog

    def blog_detailed_view(request):
        _blog_obj = Blog.objects.get(id=1)
        context = {
            "title" = _blog_obj.title,
            "content" = _blog_obj.content,
            "date"= _blog_obj.title.date,
            author = _blog_obj.title.author,
        }
        return render(request, "blog/details.html",context)

    Now in urls.py in root directory

    import the blog_detailed_view and add url to the urlpatterns list

    path('blog_detailed',blog_detailed_view)

    Now edit the details.html, import the base template and in content section add your stuff

    for example:
         {% if title is != None and title != '' %} {{ title }} {{ description }} {{ date }} {{ author }} {% else %} Blog Coming Soon {% endif %}

#### Mapping data to the context

    object = { "object" : _blog_obj }

## Django Model Forms

    No one wants to provide users the admin panel or the shell access of the application so we want to create some way for the authorized users to create some blogs without having the access to the admin panel or shell.
    To do that we simply need need to create a Django form which will directly interact with the user and will help us keep the admin access to ourselves.

    to create form we need to do as follows:
        
        Create a file called forms.py in the app folder

        in forms.py import forms and models by following commands:

        from django import forms
        from .models import Blog

        now create a new class to create body of the form to do so one must write same statements:

        Class BlogForm(forms.ModelForm):
            Class Meta:
                model = Blog
                # These are the entries which we want user to interact with
                field = [
                    "title",
                    "content"
                    "author"
                ]

        After creating the form go to the view of the app and import the form there

        blog/views.py:

            from .forms import BlogForm

            # Now create a view for the form

            def create_blog(request):
                #initiate blog form and check whether the request is either post or none

                form = BlogForm(request.POST or None)
                if form.is_valid():
                    from.save()
                    form = BlogForm()

                context = { "form": form }

                return render(request, "blogs/create_blog.html",context)

        After creating the view update the create_blog.html with the form:

            {% extends "base.html" %}
            {% block content %}
            <form method = "POST"> {% csrf_token %}
                {{ form.as_p }}
                <input type='submit' value ="submit">
            </form>
            {% endblock %}

        Now import the view from the blog to urls.py and add the path to urlpatterns list
        There you have it a working blog creating form.

## Raw Django Form

