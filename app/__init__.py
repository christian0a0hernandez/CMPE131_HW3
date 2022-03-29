from flask import Flask

myobj = Flask(__name__)
myobj.secret_key = 'jkHBJBB8877BBj/'

from app import routes
