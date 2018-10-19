# pipenv vs virtualenv

## virtualenv

- virtualenv is entirely isolated from your system's install of python
- all python deps for the virtualenv are isolated in the env dir

## pipenv

- pipenv allows to avoid overhead of dealing with sourcing the activate file
- gives you a Pipfile and Pipfile.lock
- pipenv install only installs prod
- pipenv install --dev installs prod AND dev

## pyenv

- installs specific versions of python and manages them for you
- can work in conjunction with pipenv, pipenv can see pyenv is there and uses it to automatically pick the correct version of python for your app
- prob don't need this in a Docker env because python will be the docker dep

## see also

- pipenv can tell us if there are any known security vulnerabilities, make this fail CI builds