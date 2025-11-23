# Flask

    Python flask is Python based microframework for building web applications.It is Fast and light in weight. Flask was developed by Armin Ronacher in 2010. This Framework is completely written in Python Programming Language and does not require particular tools or libraries to run.

## Questions

### Python Flask Interview Questions

1. Explain what is Python Flask?
    Python Flask is a lightweight WSGI web application framework. It is designed to make getting started quick and easy, with the ability to scale up to complex applications. It began as a simple wrapper around Werkzeug and Jinja and has become one of the most popular Python web application frameworks.

2. How to install python flask?
    Flask supports Python 3.5 and newer, Python 2.7, and PyPy. You can install flask through pip using below command.

    pip install flask

3. What is g in python flask?
    g is an object provided by Flask. It is a global namespace for holding any data you want during a single app context. For example, a before_request handler could set g.user, which will be accessible to the route and other functions.

    from flask import g
    @app.before_request
    def load_user():
        user = User.query.get(request.session.get("user_id"))
        g.user = user

    @app.route("/admin")
    def admin():
        if g.user is None or not g.user.is_admin:
            return redirect(url_for("index"))
    In Flask, an app context lasts for one request / response cycle, g is not appropriate for storing data across requests.

4. How to get http headers in flask?
    In Flask, flask.request.headers is used to get http headers.

    Example

    app = flask.Flask(__name__)
    @app.route("/")
    def index():
        headers = flask.request.headers
        return "Request headers:\n" + str(headers)

    app.run(host="127.1.0.1", port=8080)

5. How to check installed version of python flask?
    You can run the below command to check the installed version of the python flask

    import flask
    flask.__version__

6. How do you enable logging in python flask?
    Standard Python logging is used in flask framework for logging. You can log messages about your Flask Application using app.logger, which takes the same name as app.name.

    Below is an example to log your own messages in Python Flask

    def login():
        user = get_user(request.form['username'])

        if user.check_password(request.form['password']):
            login_user(user)
            app.logger.info('%s logged in successfully', user.username)
            return redirect(url_for('index'))
        else:
            app.logger.info('%s failed to log in', user.username)
            abort(401)

7. How to redirect to a url in python flask?
    You can use redirect() method to redirect a url in Python Flask. Here is an example code

    import os
    from flask import Flask,redirect

    app = Flask(__name__)

    @app.route('/')
    def hello():
        return redirect("http://www.abc.com", code=301)

8. What are macros in python flask?
    A macro in Flask is a tool to build modular user interface on web pages. Macro in flask contains

    Html file with the macro definition.
    Styles in the homonymous css file.
    Scripts in the homonymous js file with the class for manage of ui element.

9. What is Flask-WTF?
    WTF in Flask stands for WT Forms which is intended to provide the interactive user interface for the user. The WTF is a built-in module of the flask which provides an alternative way of designing forms in the flask web applications.

10. What is use of jsonify() in flask?

    jsonify() in Flask is a function in flask. json module. It serializes data to JavaScript Object Notation (JSON) format, wraps it in a Response object with the application/json mimetype. Note that jsonify is sometimes imported directly from the flask module instead of from flask.

11. How to get visitor ip address in Flask?
    You can use request.remote_addr to get visitor IP address in Flask.

    Example Code

    from flask import request
    from flask import jsonify

    @app.route("/get_user_ip", methods=["GET"])
    def get_user_ip():
        return jsonify({'ip': request.remote_addr}), 200

12. What is Flask Sijax?
    Flask-Sijax is an extension for the Flask microframework, to simplify Sijax (PyPi, GitHub) setup and usage for Flask users. Sijax is a Python/jQuery library that makes AJAX easy to use in web applications.

13. How to get logged user id in flask?
    You can use current_user.get_id() to get logged in user id in flask.

    Example Code

    from flask import g
    if current_user.is_authenticated():
        g.user = current_user.get_id()

14. List some important Flask extensions?
    Below are few important extentions in Flask, that makes development easier and quick

    flask-debugtoolbar
    Flask-WTF & WTForms-Components
    Flask-Login
    Flask-Limiter
    Flask-Philo-SQLAlchemy
    flask-pwa

15. What is WSGI middleware component in flask?
    A WSGI middleware component is a Python callable that is itself a WSGI application, but may handle requests by delegating to other WSGI applications. These applications can themselves be WSGI middleware components.

    A middleware component can perform such functions as:

    Routing a request to different application objects based on the target URL, after changing the environment variables accordingly.
    Allowing multiple applications or frameworks to run side-by-side in the same process
    Load balancing and remote processing, by forwarding requests and responses over a network
    Performing content post-processing, such as applying XSLT stylesheets