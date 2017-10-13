# Python imports

# Core Flask imports
from flask import Flask
# Third-Party imports
from flask_restful import Api
# Apps Imports
from backend_api_app.routers.routers import Router

app = Flask(__name__)
app.config.from_object('config')

Router(Api(app))
