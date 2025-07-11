import os
from flask import Flask
from flask_socketio import SocketIO
from flask_mail import Mail
from dotenv import load_dotenv

socketio = SocketIO()

def create_app(debug=False):
	app = Flask(__name__)
	load_dotenv()
	
	app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
	app.debug = debug
	app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
	app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER')
	app.config['MAIL_PORT'] = int(os.getenv('MAIL_PORT', 587))
	app.config['MAIL_USE_TLS'] = True
	app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
	app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
	app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_DEFAULT_SENDER')
	UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'static', 'uploads')
	os.makedirs(UPLOAD_FOLDER, exist_ok=True)
	app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
	##from .utils.database import database
	##db = database()
	##db.createTables(purge=False)



	socketio.init_app(app)

	with app.app_context():
		from . import routes
		return app
