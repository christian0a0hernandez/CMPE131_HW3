from flask import Flask

myapp_obj = Flask(__name__)
myapp_obj.secret_key = 'jkHBJBB8877BBj/'

from app import routes
