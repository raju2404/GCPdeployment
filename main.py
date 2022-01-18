# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 17:01:22 2022

@author: rajui
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 21:59:13 2021

@author: rajui
"""

import os
from flask import Flask, jsonify
from flaskext.mysql import MySQL
from flask import Flask, jsonify, request


app = Flask(__name__)
mysql = MySQL()

# MySQL configurations
# app.config['MYSQL_DATABASE_USER'] = 'root'
# app.config['MYSQL_DATABASE_PASSWORD'] = 'Kallis@123'
# app.config['MYSQL_DATABASE_DB'] = 'db_test_scanify'
# app.config['MYSQL_DATABASE_HOST'] = 'weighty-casing-337008:us-central1:scanify-app-instance-demo'

app.config['MYSQL_DATABASE_USER'] = os.environ.get('CLOUD_SQL_USERNAME')
app.config['MYSQL_DATABASE_PASSWORD'] = os.environ.get('CLOUD_SQL_PASSWORD')
app.config['MYSQL_DATABASE_DB'] = os.environ.get('CLOUD_SQL_DATABASE_NAME')
app.config['MYSQL_DATABASE_HOST'] = os.environ.get('CLOUD_SQL_CONNECTION_NAME')


mysql.init_app(app)

@app.route('/') 
def hello():
    return "Hello world"


@app.route('/getEntities')
def getEntities():
    cur = mysql.connect().cursor()
    cur.execute('''select * from db_test_scanify.ENTITIES''')
    r = [dict((cur.description[i][0], value)
                for i, value in enumerate(row)) for row in cur.fetchall()]
    return jsonify({'myCollection' : r})



if __name__ == '__main__':
    app.run()
