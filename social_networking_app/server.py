from waitress import serve
from social_networking_app.wsgi import application

if __name__ == '__main__':
    serve(application, port='8000')