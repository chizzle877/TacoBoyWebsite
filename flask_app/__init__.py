#this is made from doctor ghassimi's code and modified for our use

import os
from flask import Flask
from flask_socketio import SocketIO

socketio = SocketIO()

def create_app(debug=False):
	app = Flask(__name__)

	
	app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
	app.debug = debug
	app.secret_key = 'AKWNF1231082fksejfOSEHFOISEHF24142124124124124iesfhsoijsopdjf'

	##from .utils.database import database
	##db = database()
	##db.createTables(purge=False)
	

	socketio.init_app(app)

	with app.app_context():
		from . import routes
		return app
