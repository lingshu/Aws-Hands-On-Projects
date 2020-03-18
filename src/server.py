from flask import Flask, session
from flask import redirect, url_for, jsonify, flash, request, render_template
from flask_session import Session

import MySQLdb

# set up Flask app
app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
SESSION_TYPE = 'filesystem'
app.config.from_object(__name__)
Session(app)

# RDS configs
RDS_USER = 'admin'
RDS_PASSWORD = 'rdsrdsdemo'
RDS_HOST = 'rds-demo.cxe35jtcqcdm.us-east-2.rds.amazonaws.com'
RDS_PORT = 3306
RDS_DB = 'ads_db'

def rds_get_connection():
  return MySQLdb.connect(
    host=RDS_HOST,
    port=RDS_PORT,
    user=RDS_USER,
    password=RDS_PASSWORD,
    database=RDS_DB)

def rds_execute_query(query):
  conn = rds_get_connection()
  cursor = conn.cursor()
  cursor.execute(query)
  rows = cursor.fetchall()
  cursor.close()
  conn.commit()
  conn.close()
  return rows

def insert_ad(name, description):
  query = "INSERT INTO ads(name, description) VALUES ('{}', '{}')".format(name, description)
  rds_execute_query(query)

def list_ads():
  ads = []
  res = rds_execute_query('SELECT * FROM ads')
  for (name, description) in res:
    ads.append({'name': name, 'description': description})
  return ads

@app.route('/')
def index():
  return render_template('index.html', ads=list_ads())

@app.route('/upload', methods=['GET', 'POST'])
def upload():
  insert_ad(request.form['name'], request.form['description'])
  return redirect(url_for('index'))
