# Simple Flask application using Docker and docker-compose

Our project
This small project demos use of the Flask framework with Jinja2 templates together with Docker / docker-compose for web development. It uses Gunicorn as an application server and NGINX as a proxy. Files are mounted in the container and both templates and the app.py will be reloaded automatically within the container when changed locally.

## Installation

```
# git clone https://github.com/Cookie12321/TedAI_Aesop
# cd TedAI_Aesop
```

## Team

# Tony Choi - Software Engineer
# Albert Le - Data Engineer

## Run

The following will build and deploy the container locally.

```
# docker-compose up
```

Go to http://localhost:8080/.

## Tech Stack

We use Flask, React, Docker, and the OpenAI API.

## Thanks

# Many thanks to Kunbbib because this is a fork off of https://github.com/Kungbib/flask-docker-example which we used to help jumpstart our Flask web app on Docker.