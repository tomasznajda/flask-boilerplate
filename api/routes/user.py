from flask import Blueprint
from flask_restful import Api
from ..resources.user import UserAPI, UserListAPI

USERS_BLUEPRINT = Blueprint('users', __name__)
Api(USERS_BLUEPRINT).add_resource(UserListAPI, '/users/')
Api(USERS_BLUEPRINT).add_resource(UserAPI, '/users/<int:id>/')
