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