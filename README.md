arunafelt
=========

A bootstrap-themed web application framework built on top of Django. The purpose of this framework is to make website 
development is easier. The specific goals are:

1. **Reducing development time** by implementing a lot of standard features
2. **Secure and stable** by implement pre-defined security features
3. **High performance** by setting performance tuning by default
 
 
 It features are:

1. Custom User model with email or username authentication
2. Mandatory-boring-to-develop pages like sign in, sign up, contact, and reset password
3. Admin page protection with django-admin-honeypot and admin log activity
4. Assets pipelining with django-pipeline with jsmin and gzip compression for static files
5. Twitter Bootstrap default integration

How to use
==========

Libraries
=========

In this section, I will explain the usage of every libraries that have been included in the application

Django
------

The main framework.

bpython
-------

bpython is an alternative interface from the standard python interpreter. It has auto complete feature and in-line 
syntax highlighting

django-braces
-------------

django-braces provides a lot of mixin class to help you to write clean code in Django class based views. Probably the 
most useful Mixin is `LoginRequiredMixin`
 
django-model-utils
------------------



This repo is in under heavy development!