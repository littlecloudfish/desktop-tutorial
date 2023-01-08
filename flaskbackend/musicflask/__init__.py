# def create_app(test_config=None):
#     # create and configure the app
#     app = Flask(__name__, instance_relative_config=True)
#     app.config.from_mapping(
#         SECRET_KEY='dev',
#         DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
#     )

#     if test_config is None:
#         # load the instance config, if it exists, when not testing
#         app.config.from_pyfile('config.py', silent=True)
#     else:
#         # load the test config if passed in
#         app.config.from_mapping(test_config)

#     # ensure the instance folder exists
#     try:
#         os.makedirs(app.instance_path)
#     except OSError:
#         pass

#     # a simple page that says hello
#     @app.route('/hello')
#     def hello():
#         return 'Hello, World!'

#     return app

from flask import Flask, jsonify, url_for,escape,request,make_response, send_file, Response
from flask_cors import CORS
from sqlalchemy.orm import scoped_session
from flask_jwt_extended import JWTManager

UPLOAD_FOLDER = '/home/little/Documents/music_web/startproj/flaskbackend/savefile'

app = Flask(__name__)
CORS(app)


app.config["JWT_COOKIE_SECURE"] = False

app.config["JWT_SECRET_KEY"] = "GWDV4lTNj0UAuRm+pK1dao/Ol+Ik5ibP"
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif','mp3'}
jwt = JWTManager(app)

from musicflask import main, models
from musicflask.database import SessionLocal, engine

app.session = scoped_session(SessionLocal)

models.Base.metadata.create_all(bind=engine, checkfirst=True)




