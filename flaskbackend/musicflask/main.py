import mimetypes
from flask import Flask, jsonify, url_for,escape,request,make_response, send_file, Response
from flask_cors import CORS
from sqlalchemy.orm import scoped_session
from sqlalchemy.sql import func, extract

import models
from database import SessionLocal, engine

from flask_jwt_extended import create_access_token,jwt_required,JWTManager,set_access_cookies,unset_jwt_cookies,current_user

from datetime import date
from werkzeug.utils import secure_filename

models.Base.metadata.create_all(bind=engine, checkfirst=True)

app = Flask(__name__)
CORS(app)
app.session = scoped_session(SessionLocal)

UPLOAD_FOLDER = '/home/little/Documents/music_web/startproj/flaskbackend/savefile'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif','mp3'}

app.config["JWT_TOKEN_LOCATION"] = ["headers", "cookies", "json", "query_string"]
#change later
app.config["JWT_COOKIE_SECURE"] = False

app.config["JWT_SECRET_KEY"] = "GWDV4lTNj0UAuRm+pK1dao/Ol+Ik5ibP"
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


jwt = JWTManager(app)





@app.route("/")
def main():
    return f"See the data at {url_for('show_records')}"

@app.route("/login_without_cookies", methods=["POST"])
def login_without_cookies():
    access_token = create_access_token(identity="example_user")
    return jsonify(access_token=access_token)

@app.route("/login_with_cookies", methods=["POST"])
def login_with_cookies():
    response = jsonify({"msg": "login successful"})
    access_token = create_access_token(identity="example_user")
    set_access_cookies(response, access_token)
    return response

@app.route("/logout_with_cookies", methods=["POST"])
def logout_with_cookies():
    response = jsonify({"msg": "logout successful"})
    unset_jwt_cookies(response)
    return response


@app.route("/only_headers")
@jwt_required(locations=["headers"])
def only_headers():
    return jsonify(foo="baz")

# @app.route("/protected", methods=["GET", "POST"])
# @jwt_required()
# def protected():
#     return jsonify(foo="bar")


@jwt.user_identity_loader
def user_identity_lookup(user):
    return user.id

@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data["sub"]
    return app.session.query(models.User).filter_by(id=identity).one_or_none()

@app.route("/login", methods=["POST"])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    user = app.session.query(models.User).filter_by(username=username).one_or_none()
    if not user or not user.check_password(password):
        return jsonify("Wrong username or password"), 401
    

    # Notice that we are passing in the actual sqlalchemy user object here
    access_token = create_access_token(identity=user)
    return jsonify(access_token=access_token)



@app.route("/who_am_i", methods=["GET"])
@jwt_required()
def who_am_i():
    # We can now access our sqlalchemy User object via `current_user`.
    # current_user = get_jwt_identity()
    return jsonify(
        id=current_user.id,
        username=current_user.username,
    )

@app.route("/register", methods = ['POST'])
def register():
    
    try:
        name = request.json.get("username",None)
        password = request.json.get('password',None)
    except Exception as e:
        return make_response('wrong',202)
    
    try:
        newre=models.User(username=name,password=password)
        app.session.add(newre)
        app.session.commit()
    except Exception as e:
        return make_response('wrong',202)

    return make_response('success',201)



# @app.route('/uploadimg', methods=['POST'])
# def uploadimg():
#     if request.method == 'POST':
#         print(request.files)
#         pic = request.files['pic']
#     if not pic:
#         return 'No pic uploaded!', 400
#     filename = secure_filename(pic.filename)
#     mimetype = pic.mimetype
#     if not filename or not mimetype:
#         return 'Bad upload!', 400
#     img = models.Img(img=pic.read(), name=filename, mimetype=mimetype)
#     app.session.add(img)
#     app.session.commit()
#     return 'Img Uploaded!', 200

# @app.route('/uploadmp3', methods = ['POST'])
# def uploadmp3():
#     if request.method == 'POST':
#         print(request.files)
#         mp3 = request.files['mp3']      
#     if not mp3:
#         return 'No pic uploaded!', 400
#     filename = secure_filename(mp3.filename)
#     mimetype = mp3.mimetype
#     if not filename or not mimetype:
#         return 'Bad upload!', 400
#     mp3 = models.StoreMusic(mp3=mp3.read(), name=filename, mimetypes=mimetype)
#     app.session.add(mp3)
#     app.session.commit()
#     return 'Music Uploaded!', 200

#upload music page
@app.route("/uploadmusic", methods = ['POST'])
# @jwt_required()
def uploadmusic():
    # user_id = current_user.id
    user_id = 1
#    musicname = request.json.get("musicname",None) #musicname in json
    musicname = "test"
    pic = request.files['pic']
    musicfile = request.files['mp3']
    if not pic or not musicfile:
        return make_response('No pic uploaded!', 400)
    imagename = secure_filename(pic.filename)
    imagemimetype = pic.mimetype
    musicfilename = secure_filename(musicfile.filename)
    musicmimetype = musicfile.mimetype
    if not imagename or not imagemimetype or not musicfilename or not musicmimetype:
        return make_response('Bad upload',400)
    image = models.Img(img=pic.read(), name=imagename, mimetype=imagemimetype)
    storemusic = models.StoreMusic(mp3=musicfile.read(), name=musicfilename, mimetypes=musicmimetype)
    newre=models.Music(name=musicname,user_id=user_id, coverimg=[image],music_store=[storemusic])

    try:
        app.session.add(newre)
        app.session.add(image)
        app.session.add(storemusic)
        app.session.commit()
    except Exception as e:
        return make_response(e,500)
    return make_response('Add %s and date record successfully' % musicname, 200) 


# today:0,thisweek:1,thismonth:2,thisyear:3,all:4
@app.route("/listmusics/<int:timeperiod>")
def show_musics(timeperiod):
    year,week_num,day_of_week = date.today().isocalendar()
    if timeperiod == 4:
        records = app.session.query(models.Music).all()
    elif timeperiod == 3:
        records = app.session.query(models.Music).filter(extract('year',models.Music.post_date)==year)
    elif timeperiod == 2:
        current_month = date.today().month
        records = app.session.query(models.Music).filter(extract('month',models.Music.post_date)==current_month)
    elif timeperiod == 0:
        current_day = date.today().day
        records = app.session.query(models.Music).filter(extract('day',models.Music.post_date)==current_day)
    elif timeperiod == 1:
        records = app.session.query(models.Music).filter(extract('week',models.Music.post_date)==week_num)


    return jsonify([record.to_dict() for record in records])

@app.route("/music/<int:music_id>")
def playmusic(music_id):
    record = app.session.query(models.Music).get(music_id)
    return jsonify([record.to_dict()])

@app.route('/enjoymusic/<int:id>')
def enjoymusic(id):
    try:
        music = app.session.query(models.StoreMusic).filter_by(id=id).first()
        if not music:
            return make_response('Img Not Found!', 404)
    except Exception as e:
        print(e)
        return make_response("Wrong",400)

    return Response(music.mp3, mimetype=music.mimetypes)

@app.route('/showimage/<int:id>')
def get_img(id):
    try:
        img = app.session.query(models.Img).filter_by(id=id).first()
        if not img:
            return make_response('Img Not Found!', 404)
    except Exception as e:
        print(e)
        return make_response("Wrong",400)

    return Response(img.img, mimetype=img.mimetype)

@app.route("/records/<int:user_id>/")
def playerwork(user_id):
    records = app.session.query(models.Music).filter(user_id=user_id).all()
    return jsonify([record.to_dict() for record in records])

# username
@app.route("/usernamerecords/<user_name>")
def usernamesearch(user_name):
    try:
        # records = app.session.query(models.User).all()
        records = app.session.query(models.User).filter(models.User.username.contains(user_name)).all()
    except:
        return "Empty"

    return jsonify([record.to_dict() for record in records])



@app.route("/add/<name>")
def add_record(name):
    newre=models.Record(country=name)
    try:
        app.session.add(newre)
        app.session.commit()
    except Exception as e:
        return "Wrong"
    return 'Add %s record successfully' % name

#

# return image file 
# @app.route('/get_image')
# def get_image():

# escape
# @app.route("/<name>")
# def hello(name):
#     return f"Hello, {escape(name)}"

@app.teardown_appcontext
def remove_session(*args, **kwargs):
    app.session.remove()


if __name__ == '__main__':

    app.run(host = '127.0.0.1',port=1943,debug=True)

