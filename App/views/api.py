from flask import Blueprint, redirect, render_template, request, send_from_directory

api_views = Blueprint('api_views', __name__, template_folder='../templates')

