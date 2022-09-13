from flask import Flask, jsonify, url_for,escape,request,make_response
from flask_cors import CORS
from sqlalchemy.orm import scoped_session

import models
from database import SessionLocal, engine

from flask_jwt_extended import create_access_token,jwt_required,JWTManager,set_access_cookies,unset_jwt_cookies,current_user

# import flask_login
# import flask

# from flask_restful import Resource, Api


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





# app.secret_key = 'super secret string'  
# login_manager = flask_login.LoginManager()
# login_manager.init_app(app)

# api = Api(app)

# @login_manager.user_loader
# def user_loader(id):
#     user=app.session.query(models.User).filter_by(id = id).first()
#     if user is None:
#         return
    
#     return user

#not verified http://gouthamanbalaraman.com/blog/minimal-flask-login-example.html

# @login_manager.request_loader
# def request_loader(request):
#     token = request.headers.get('Authorization')
#     if token is None:
#         token = request.args.get('token')
#     else:
#         username,password = token.split(":")
#         user_entry = app.session.query(models.User).get(username)
#         if (user_entry is not None):
#             user = user_entry
#             if (user.password == password):
#                 return user
    
#     return



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


# @app.route("/protected", methods=["GET", "POST"])
# @jwt_required()
# def protected():
#     return jsonify(foo="bar")


@app.route("/only_headers")
@jwt_required(locations=["headers"])
def only_headers():
    return jsonify(foo="baz")

# @app.route("/login", methods=["POST"])
# def login():
#     username = request.json.get("username", None)
#     password = request.json.get("password", None)
#     if username != "test" or password != "test":
#         return jsonify({"msg": "Bad username or password"}), 401
#     # print(type(username)) str

#     access_token = create_access_token(identity=username)
#     return jsonify(access_token=access_token)

@app.route("/protected", methods=["GET", "POST"])
@jwt_required()
def protected():
    return jsonify(foo="bar")


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
    print(type(user))
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
        full_name=current_user.full_name,
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
    return 'Add %s record successfully' % name


@app.route("/musics/")
def show_musics():
    records = app.session.query(models.Music).all()
    return jsonify([record.to_dict() for record in records])

@app.route("/records/")
def show_records():
    records = app.session.query(models.User).all()
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

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if flask.request.method == 'GET':
#         return '''
#                <form action='login' method='POST'>
#                 <input type='text' name='email' id='email' placeholder='email'/>
#                 <input type='password' name='password' id='password' placeholder='password'/>
#                 <input type='submit' name='submit'/>
#                </form>
#                '''

#     email = flask.request.form['email']
#     password = flask.request.form['password']
#     user = app.session.query(models.User).filter_by(email = email).first()
#     if user and user.password == password: 
#         flask_login.login_user(user,remember= True)
#         return flask.redirect(flask.url_for('protected'))


#     return 'Bad login'



# @app.route('/logout')
# def logout():
#     flask_login.logout_user()
#     return 'Logged out'

# @login_manager.unauthorized_handler
# def unauthorized_handler():
#     return 'Unauthorized', 401

# escape
# @app.route("/<name>")
# def hello(name):
#     return f"Hello, {escape(name)}"

@app.teardown_appcontext
def remove_session(*args, **kwargs):
    app.session.remove()


if __name__ == '__main__':

    app.run(host = '127.0.0.1',port=1943,debug=True)

