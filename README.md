Docker-Django Boilerplate
=========================

!Docker-Django

Overview
--------

Docker-Django is a boilerplate repository designed to kickstart your Django project with Dockerized services. It includes PostgreSQL and Redis support, making it easy to set up a development environment and deploy to production.

### Features

-   Django project setup with Docker containers
-   PostgreSQL database integration
-   Redis caching support
-   Whitenoise for serving static files
-   Production hosting options included

Getting Started
---------------

1.  Clone the Repository:

    ```
    git clone https://github.com/MasterKale/Docker-Django.git

    ```

2.  Remove the Existing Git History:

    ```
    rm -rf Docker-Django/.git

    ```

3.  Initialize a New Git Repository:

    ```
    cd Docker-Django
    git init

    ```

4.  Install Dependencies:

    ```
    pipenv install --three

    ```

5.  Create a New Django Project:

    ```
    pipenv run django-admin startproject myproject .

    ```

6.  Configure `settings.py`:

    -   Set the `SECRET_KEY` (used in production).
    -   Enable or disable `DEBUG` mode based on environment.
    -   Configure `ALLOWED_HOSTS` and `CSRF_TRUSTED_ORIGINS`.
    -   Point Django to the Docker-hosted Postgres database.
7.  Run the Development Server:

    ```
    docker-compose up

    ```

Deployment
----------

-   Customize the boilerplate according to your project's requirements.
-   Explore deployment options such as Kubernetes, AWS ECS, or Heroku.

Additional Resources
--------------------

-   Scaling Python with Docker and Django: A step-by-step guide on deploying Django apps with Docker.
-   Other Django-Docker examples:
    -   negeek/django-docker
    -   nickjj/docker-django-example

Feel free to adapt this boilerplate for your own projects! 🚀

* * * * *

If you have any specific questions or need further assistance, feel free to ask! 😊👍 .
