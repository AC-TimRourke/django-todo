# django-todos

A first app written using Django

## Host dependencies

Make sure you are using python v.3.7.0. See below for details about how to use this version of Python on your local machine.

## Getting started

Running python on your local host machine can be greatly simplified by using 2 tools:
1. [pyenv](https://github.com/pyenv/pyenv) helps manage different versions of python installed on the same computer
2. [pipenv](https://github.com/pypa/pipenv) helps manage python dependencies for your app, like Composer or NPM


### Getting Python 3.7.0 installed

First, install `pyenv`. This tool is similar to rbenv, phpenv, etc., and will allow you to install and use different versions of python at will without creating conflicts on your OS.

```bash
brew update && brew install pyenv
```

Now you can use pyenv to install python version 3.7.0:

```bash
pyenv install 3.7.0
```

Now, to make that version of python the default version for your system:

```bash
pyenv global 3.7.0
```

_Note that you can use pyenv at any time to also revert to the default version of python your OS shipped with to return to "normal"._

### Installing pipenv

`pipenv` is an excellent package manager for python projects. Now that you are running python v3.7.0, you can use the default python package manager `pip` to install pipenv. pipenv is better than `pip` by itself; pipenv will create a `Pipfile`, which is similar to a `composer.json` file in PHP, and a `Pipfile.lock`, which like a `composer.lock` file, helps specify _exactly_ which version of a dependency you mean to install for a project.

```bash
pip install pipenv
```

## Running the application using docker-compose

To spin up the application server, use the `docker-compose.yml` services that are configured for you:

```bash
docker-compose up --build
```

This should create the container, install the application's depencencies, and start the application server.

Now you can browse to [http://localhost:8000/todos](http://localhost:8000/todos) to see the app's index page.

**NOTE:** If you are using docker-machine, you'll probably need to use [http://192.168.99.100:8000/todos](http://192.168.99.100:8000/todos) instead.

### Run the application's migrations

To run the migrations for this application, create a bash session using `docker-compose`:

```bash
docker-compose exec python bash
```

Once inside the bash session, use the app's main `project`'s entrypoint `project/manage.py` to run the Django `migrate` command:

```bash
pipenv run python project/manage.py migrate
```

### Create the application's superuser

Django ships with a very nice administration panel out of the box. To start using it, we must first create the app's main admin "superuser". Be sure to do this from within a bash session to the `python` service. It is interactive, and will prompt you for input:


```
pipenv run python project/manage.py createsuperuser
```

Once you have created the first Django "superuser", you can browse to [http://localhost:8000/admin](http://localhost:8000/admin) to log in (or [http://192.168.99.100:8000/admin](http://192.168.99.100:8000/admin) if you are running docker-machine). Log in with the user and password you just created the superuser with to see the administration options.

You should be able to create Users, assign them to Groups, and manage a given User's Todos.