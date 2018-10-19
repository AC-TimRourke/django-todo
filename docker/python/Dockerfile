FROM python:3.7

# Send python stdout directly to terminal without buffering
ENV PYTHONUNBUFFERED 1

# Install pipenv
RUN pip install pipenv

WORKDIR /usr/src/app

COPY Pipfile ./
COPY Pipfile.lock ./

COPY . .

RUN pipenv install

EXPOSE 8000

STOPSIGNAL SIGINT

ENTRYPOINT ["pipenv", "run", "python", "./project/manage.py"]

CMD ["runserver", "0.0.0.0:8000"]
