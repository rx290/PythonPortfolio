# Introduction

## Questions

    1. What is flask?
    2. What is WSGI?
    3. What are new features of Flask?
    4. What is Werkzeug in Flask?
    5. Explain Jinja?
    6. What is Flask-WTF and what are some of its attributes?
    7. Explain how sessions are accessed in Flask?
    8. What are Database Connections in Flask?
    9. What is Flask Sijax?
    10. What Methods are provided by Python Flask for HTTPS?
    11. What are endpoint? How can we make one is Flaks?
    12. Flask vs Pyramid vs Django
    13. What is redirect() Function?
    14. Delimiters in jinja2
    15. Please Explain 1xx,2xx,3xx,and 5xx errors
    16. How to get user id logged in Flask?
    17. How to get visitor ip address in Flask?
    18. How memory is managed in Flask Python?
    19. how can we get a query string from flask?
    20. What is pickling and unpckling?
    21. Debugging in Flask? Default port? 
    22. What are validators class of WTForm in Flask?
    23. What is Authentication? Explain the differences between OAuth, Simple Auth Etc? What is Salting?
    24. What are client errors in Flask? 4xx
    25. App routing in Flask?

## Answers
    
    13. What is redirect() Function?
    14. Delimiters in jinja2
    15. Please Explain 1xx,2xx,3xx,and 5xx errors
    16. How to get user id logged in Flask?
    17. How to get visitor ip address in Flask?
    18. How memory is managed in Flask Python?
        

    19. how can we get a query string from flask?
        
        @app.route('/data')
            def data():
                pass
        user= request.org.get('user')

    20. What is pickling and unpckling?
        Serialized representation of objects, converted into a string and dumped in a file is known as pickling.
        Retrieving these serialized representation of objets from the stored string form is called unpickling.


    21. What are validators class of WTForm in Flask?
        List of Validators Class of WTForm in Flask is as follows:
        1. DataRequired: To check whether input field is empty or not
        2. Email: To check if the text follows email id convections
        3. IPAddress: To validate IP address in input Field
        4. Length: To verify if the length of string in input field is in given range
        5. NumberRange: To validate a number in input field within given range
        6. URL: To validate URL entered in input Field

    22. Debugging in Flask? Default port? 
        To enable debugging we must set debug=True in the app.run function
        Default Port for flask is 5000

    23. What are client errors in Flask?
        All 4xx errors are client side errors and some of the common ones are as follows:
        1. HTTP_400_BAD_REQUEST
        2. HTTP_401_UNAUTHORIZED
        3. HTTP_402_PAYMENT_REQUIRED
        4. HTTP_403_FORBIDDEN
        5. HTTP_404_NOT_FOUND
        6. HTTP_405_METHOD_NOT_ALLOWED
        7. HTTP_408_REQUEST_TIMEOUT
        8. HTTP_409_CONFLICT
        9. HTTP_415_UNSUPPORTED_MEDIA_TYPE
        10. HTTP_429_TOO_MANY_REQUEST
    
    24. App routing in Flask?

        A mapping technique for specified url associated with methods which are intended to perform some tasks.

    