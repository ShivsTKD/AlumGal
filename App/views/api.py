from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify
from App.models import Profile

api_views = Blueprint('api_views', __name__, template_folder='../templates')

@api_views.route('/loadusers/<offset>', methods=['GET'])
def load_more_users(offset):
    users = Profile.query.offset(offset).limit(25).all()
    users = [user.toDict() for user in users]
    return jsonify(users)