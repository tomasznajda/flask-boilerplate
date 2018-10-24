from flask_restful import Resource, abort
from flask_restful.reqparse import Argument
from flasgger import swag_from
from ..repositories.user import UserRepository
from ..utils import parse_params
from ..utils.responses import response_success, response_error
from ..utils.error_codes import ERROR_CODE_USER_DOES_NOT_EXIST


class UserAPI(Resource):

    @staticmethod
    @parse_params.parse_params(
        Argument('first_name', location = 'json', type = str, required = True),
        Argument('last_name', location = 'json', type = str, required = True),
        Argument('age', location = 'json', type = int, required = False)
    )
    @swag_from('../docs/user/POST.yml')
    def post(id, first_name, last_name, age):
        user = UserRepository.get(id = id)
        if not user:
            return response_error(ERROR_CODE_USER_DOES_NOT_EXIST, "User does not exist")
        user = UserRepository.update(id = id, first_name = first_name, last_name = last_name, age = age)
        return response_success(user.json)

    @staticmethod
    @swag_from('../docs/user/DELETE.yml')
    def delete(id):
        user = UserRepository.get(id = id)
        if not user:
            return response_error(ERROR_CODE_USER_DOES_NOT_EXIST, "User does not exist")
        UserRepository.delete(id = id)
        return response_success(None, 204)

    @staticmethod
    @swag_from('../docs/user/GET.yml')
    def get(id):
        user = UserRepository.get(id = id)
        if not user:
            return response_error(ERROR_CODE_USER_DOES_NOT_EXIST, "User does not exist")
        return response_success(user.json)


class UserListAPI(Resource):

    @staticmethod
    @parse_params.parse_params(
        Argument('first_name', location = 'json', type = str, required = True),
        Argument('last_name', location = 'json', type = str, required = True),
        Argument('age', location = 'json', type = int, required = False)
    )
    @swag_from('../docs/user-list/POST.yml')
    def post(first_name, last_name, age):
        user = UserRepository.add(first_name = first_name, last_name = last_name, age = age)
        return response_success(user.json, 201)
