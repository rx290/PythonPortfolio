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

## Pure Django Form

    So we want to create a new form which is purely based on DJango and it should have a custom touch ? 

    well for that particular reasons we will be creating a class with form model and then creating fields according to our needs.

    in forms.py add this class to create a new pure django form

    class PureDjangoForm(forms.Form):
        title = forms.CharField()
        date = forms.DateField()
        content = forms.TextField()
        author = forms.CharField()

    now after creating a pure django form we have to initialize that form in our views.py
    and pass it as a context variable

    by doing this:
        my_form = PureDjangoForm(request.GET)
        if request.method = "POST":
            my_form = PureDjangoForm(request.POST)
            if my_form.is_valid():
                #do something
            else:
                # do something else
        context = { "form" : my_form }

### Django Forms Widget

    This section deals with the parameters passed with the django data fields in the form some of which are as follows:
    1. label
    2. required
    3. initial
    4. widget = textarea etc

### Form Validation Method

    Let say we want something in our context and without that form is not going to get submitted, we can do that with form validation which is done as follows:

    create a function 
    
    def clean_name_of_field(self):
        content - self.cleaned_data.get("content")
        if "any_word or any_sentence" in content:
            return content
        else:
            raise forms.ValidationError("Content doesn't have required word or sentence")

        # Above example is for single validation if we want to create multiple validations we need to tweak our code a little bit 
        # which would be like this

        if not "any_word or any_sentence" in content:
            raise forms.ValidationError("Content doesn't have required word or sentence")
        if not "any_word or any_sentence" in content:
            raise forms.ValidationError("Content doesn't have required word or sentence")
        else:
            return content

        # what this above mentioned chunk of code is going to do is it'll check for each if not statement and will return default i.e.
        # else part when all the statements validation are true.

### Setting Initial Values on a form

    to set initial values we need to create a dictionary same as context when rendering a template and assign an initial value to that key in that dictionary

    initial_data = {
        "author" : "Anonymous"
    }

    Let say we have to edit a user and want to set initial data from the database of that particular person what to do then?
    well it is quite easy when initializing a form just add a parameter of instance and set it equal to the object and it'll add the data accordingly i.e. 

    in views.py

        def edit_blog(request):
            obj = Blog.objects.get(id=1)
            form = BlogForm(request.POST or None, instance = obj)
            if form.is_valid():
                form.save()
            context = {'form':form}
            return render(request,"blogs/blog_create.html",context)

### Dynamic URL Routing

    in urls.py add a param to the string path i.e.

    "blogs/<int:id>"

    now in views.py parse in id as a parameter to the view function

    def blog_detailed_view(request,id):
        _blog_obj = Blog.objects.get(id)
        context = {
           "object" : _blog_obj
        }
        return render(request, "blog/details.html",context)

    Now your blogs app have that dynamic url handling enabled

### Handle DoesNotExist Error

    import get_object_or_404 from django.shortcuts or Http404 form django.http
    
    get_object_or_404:
        def blog_detailed_view(request,id):
            _blog_obj = get_object_or_404(Blog,id=id)
            context = {
            "object" : _blog_obj
            }
            return render(request, "blog/details.html",context)

    Http404:
        def blog_detailed_view(request,id):
            try:
                _blog_obj = Blog.objects.get(id=id)
            except Blog.DoesNotExist:
                raise Http404
            context = {
            "object" : _blog_obj
            }
            return render(request, "blog/details.html",context)

## Delete and Confirm

    create a simple form for it which would be like this

        {% extends 'base.html' %}

        {% block content %}

        <form action='.' method = "POST">{% csrf_token %}
            <h1>Do you want to delete the blog "{{ object.title }}"?</h1>
            <p><input type="submit" value ="yes"> <a href='../'>Cancel</a></p>
        </form>
        {% endblock %}

    url path
        path('blogs/<int:id>/delete',blog_delete_view, name='blog-delete')

    view:

        def blog_delete_view(request,id):
            obj = get_object_or_4040(Blot,id=id)
            #POST request

            if request.method == "POST":
                obj.delete()
            context = { "object" : obj }
            return render (request, "blogs/blog_delete.html",context)

## View of a list of database objects

    view:
        def blog_list_view(request):
            queryset = Blog.objects.all()
            context = {
                'object_list' : queryset
            }
            return render(request, "blog/blog_list.html", context)

    template:
        
        {% extends 'base.html' %}

        {% block content %}

        {% for instance in object_list %}
        
            <p> {{ instance.id }} - {{ instance.title }}</p>
        
        {% endfor %}
        {% endblock %}

## Dynamic Url Linking

    When dealing with tons of objects we can't just hard code thousands of urls to our views so what we are going to learn today is to create dynamic url linking for the objects stored in the database

    to generate a dynamic url we need to create a method to obtain an absolute url which have an editable part to navigate to certain pages to achieve that we need to edit models.py

    in models.py create a function get_absolute_url

        def get_absolute_url(self):
            return "/blogs/{self.id}/"
            # this method is returning a string which contains our absolute and finalized url along with a dynamic tag to navigate to 
            # desired page

    now in template we need to change these things
        {% extends 'base.html' %}

        {% block content %}

        {% for instance in object_list %}
        
            <p> {{ instance.id }} - <a href='{{ instance.get_absolute_url }}'>{{ instance.title }}</a></p>
        
        {% endfor %}
        {% endblock %}

## Django URLs Reverse

    This is the easy approach of above mentioned method where we are going to use the provided attributes and kwargs provided int he urls.py.

    example:

        def get_absolute_url(self):
            
            # now rather than returning a string we are going to return an expression using the name and kwargs defined earlier
            # return reverse("name", kwargs={ kwargs parameters here })

            return reverse("blog-detail", kwargs = { "id" : self.id })

## In App URLs and Namespaces

    so a lot of confusion can occur if we declare all url paths in main url.py so what we are going to do is to create a new urls.py for in app uses and then import that into the main urls.py to avoid any sort of breaching

    firs to create a urls.py in app we need to create this template:

        from django.urls import path
        from .views import (
            blog_create_view,
            blog_detail_view,
            blog_delete_view,
            blog_list_view,
            blog_update_view
        )

        urlpatterns= [
            
            #reason we have removed blogs/ from the path is the include feature used in the root urls.py which will add blogs/ to 
            # these paths itself.
            
            path('', blog_list_view, name = 'blog-list'),
            path('create/', blog_create_view, name = 'blog-crete'),
            path('<int:id>/', blog_detail_view, name = 'blog-detail'),
            path('<int:id>/update', blog_update_view, name = 'blog-update'),
            path('<int:id>/delete', blog_delete_view, name = 'blog-delete'),
        ]

    Now back at main urls.py 

        from django.contrib import admin
        from django.urls import include, path
        
        urlpatterns= [
            path('blogs/', include('blogs.urls')),
            
            path('', home_view, name = 'home'),
            path('aboutUs/', about_view, name = 'AboutUs'),
            path('contact/', contact_view, name = 'contact'),
            path('admin/', admin.site.urls),
        ]

### namespaces

    After cleaning and writing efficient code our code won't work as we want because it lacks the leading medium something which tells the paths to look to the exact app place where it is directing to.

    for that particular problem django has provided us with namespaces like app_name which performs above mentioned task.
    so to add it simply add this above urlpatterns

    app_name = 'blogs'

    after doing that go to blogs models.py and add blogs: to the url path like this

    return reverse("blogs:blog-detail", kwargs = { "id" : self.id })

## Class Based Operation

### Views - List Views

    These tricks are essential and easy to learn to use class based view you should have a good understanding of Objects and class inheritance.

    now lets make a class based view of a blog:

    in views.py

        from django.shortcuts import render
        from django.views.generic import(
            CreateView,
            DetailView,
            ListView,
            UpdateView,
            ListView,
            DeleteView
        )
        from .models import Article

        # Here article List view is going to inherit the structure and behavior from Listview 
        class ArticleListView(ListView):

            # to override the template lookup we can also create a variable to store the lookup pattern which is as follows:
            # template_name = "articles/article_list.html"

            queryset = Article.objects.all()

        after that import the class to the app urls.py and create a path for it i.e.

        from .views import(
            ArticleListView,
        )

        app_name = 'articles'
        urlpatterns= [
            path ('',ArticleListView.as_View(), name='article_list')
        ]

        There we go we have classed based list view

### View - Detail view

    in same file create another class called ArticleDetailedView like this

        class ArticleDetailView(DetailView):
            template_name = 'articles/article_detail.html'
            queryset= Article.objects.all()

    now in urls.py add path and import ArticleDetail view

        path ('',ArticleDetailView.as_View(), name='article_detail')

### View - Create View

    Create a class ArticleCreateView and inherit CreateView like this

        class ArticleCreateView(CreateView):
            template_name = 'article/article_create.html'
            form_class =ArticleModelForm
            queryset = Article.objects.all()
            <!-- success_ur = '/' -->

            def form_validation(self,form):
                print(form.cleaned_data)
                return super().form_valid(form)
            
            <!-- def get_success_url(self):
                return '/' -->


    now in urls.py add path and import ArticleDetail view

        path ('',ArticleCreateView.as_View(), name='article_detail')

### Views - Update View

        Create a class ArticleCreateView and inherit CreateView like this

        class ArticleUpdateView(UpdateView):
            template_name = 'article/article_create.html'
            form_class =ArticleModelForm
            queryset = Article.objects.all()

            def get_object(self):
                _id = self.kwargs.get("id")
                return get_object_or_404(Article,id = _id)


            def form_validation(self,form):
                print(form.cleaned_data)
                return super().form_valid(form)
            


    now in urls.py add path and import ArticleUpdate view

        path ('',ArticleUpdateView.as_View(), name='article_update')

### View - Delete view

    in same file create another class called ArticleDeleteView like this

        class ArticleDeleteView(DeleteView):
            template_name = 'articles/article_detail.html'
        
            def get_object(self):
                _id = self.kwargs.get("id")
                return get_object_or_404(Article,id = _id)
            
            def get_success_url(self):
                return reverse('blog:article-view')

    now in urls.py add path and import ArticleDelete view

        path ('',ArticleDeleteView.as_View(), name='article_delete')

### Getting an object in classes

    you can't simple fetch something like in the conventional way so you need to use another builtin method known as get_object_or_404

    define a method and fetch the object like this

    def get_object(self):
        _id = self.kwargs.get("id")
        return get_object_or_404(Article,id = _id)

## Function based view to class based view

    so here is a function class 

        from django.shortcuts import render
        
        def my_fbv(request, *args, **kwargs):
            return render(request, 'about.html',{})

    so how to convert that into a class based view?

    to do that we need to import a base view from a class with this statement

    from django.views import View

    so the in previous file just import this class and create a class and initialize the same function with name of get and an extra parameter self
    the file will now look like this


    from django.shortcuts import render
    from django.views import View

    class CourseView(View):
        template_name = "about.htm"
        def get(self, request, *args, **kwargs):
            return render(request, self.template_name,{})

    and in url we just need to add a path to this class and that's it. function based class is converted into a class based view
