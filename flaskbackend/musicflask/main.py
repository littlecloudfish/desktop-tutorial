from flask import Flask, jsonify, url_for,escape,request,make_response
from flask_cors import CORS
from sqlalchemy.orm import scoped_session
from sqlalchemy.sql import func, extract

import models
from database import SessionLocal, engine

from flask_jwt_extended import create_access_token,jwt_required,JWTManager,set_access_cookies,unset_jwt_cookies,current_user

from datetime import date

models.Base.metadata.create_all(bind=engine)

app = Flask(__name__)
CORS(app)
app.session = scoped_session(SessionLocal)

app.config["JWT_TOKEN_LOCATION"] = ["headers", "cookies", "json", "query_string"]
#change later
app.config["JWT_COOKIE_SECURE"] = False

app.config["JWT_SECRET_KEY"] = "GWDV4lTNj0UAuRm+pK1dao/Ol+Ik5ibP"
app.config['CORS_HEADERS'] = 'Content-Type'
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



#upload music page
@app.route("/uploadmusic/<name>/<int:user_id>")
def uploadmusic(name,user_id):
    newre=models.Music(name=name,user_id=user_id)
    try:
        app.session.add(newre)
        app.session.commit()
    except Exception as e:
        return "Wrong"
    return 'Add %s and date record successfully' % name 

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




# escape
# @app.route("/<name>")
# def hello(name):
#     return f"Hello, {escape(name)}"

@app.teardown_appcontext
def remove_session(*args, **kwargs):
    app.session.remove()


if __name__ == '__main__':

    app.run(host = '127.0.0.1',port=1943,debug=True)

