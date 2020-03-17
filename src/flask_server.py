from flask import Flask, session
from flask import redirect, url_for, jsonify, flash, request, render_template
from flask_session import Session


# set up Flask app
app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
SESSION_TYPE = 'filesystem'
app.config.from_object(__name__)
Session(app)

@app.route('/')
def index():
  return 'It works'
