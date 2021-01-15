from flask import request, Blueprint, session, jsonify

from ..views.users_views import save_new_user, get_all_users, get_a_user

@api.route('/')
class UserList():
    def get(self):
        return get_all_users()

    @api.response(201, 'User successfully created.')
    def post(self):
        data = request.json
        return save_new_user(data=data)
