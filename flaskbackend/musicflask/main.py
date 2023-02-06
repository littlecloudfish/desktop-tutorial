import mimetypes
from sqlalchemy.orm import scoped_session, selectinload
from sqlalchemy.sql import func, extract
import os
from musicflask import models

from flask_jwt_extended import create_access_token,jwt_required,set_access_cookies,unset_jwt_cookies,current_user

from datetime import date, datetime
from werkzeug.utils import secure_filename

from musicflask import app,jsonify, url_for,escape,request,make_response, send_file, Response,models, jwt

import json

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
    print(request.json) 
    try:
        name = request.json.get("name",None)
        password = request.json.get('password',None)
        email = request.json.get('email',None)
    except Exception as e:
        return make_response('wrong',202)
    
    try:
        newre=models.User(username=name,password=password,email=email)
        app.session.add(newre)
        app.session.commit()
    except Exception as e:
        return make_response('wrong',202)
    
    return make_response('success',201)



#upload music page
@app.route("/uploadmusic", methods = ['POST'])
# @jwt_required()
def uploadmusic():
    # user_id = current_user.id
    user_id = 1
    pic = request.files['pic']
    musicfile = request.files['mp3']
    musicname = request.form['musicname']
    release_date =datetime.strptime(request.form['releasedate'], '%Y-%m-%d')
    # print(type(release_date))
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
    newre=models.Music(name=musicname,user_id=user_id, coverimg=[image],post_date=release_date ,music_store=[storemusic])

    try:
        app.session.add(newre)
        app.session.add(image)
        app.session.add(storemusic)
        app.session.commit()
    except Exception as e:
        return make_response(e,500)
    return make_response('Add %s and date record successfully' % musicname, 200) 
#combine with uploadmusic later request.json.get maybe use it later
@app.route("/uploadmusicinfo",methods = ['POST'])
def uploadmusicinfo():
    musicinfo=json.loads(request.form.get('musicinfo'))
    imfile = request.files['imagefile']
    imfiletyep = imfile.mimetype
    newfileid = datetime.now().strftime("%m:%d:%Y:%H:%M:%S")+secure_filename(imfile.filename)
    print(imfiletyep)
    # imfile.save(os.path.join(app.config['UPLOAD_FOLDER'],newfileid))
    # imfile.save(filename=imfile.filename)
    # createdate = datetime.strptime(request.form.get('createdate')[4:23],'%b %d %Y %H:%M:%S')    
    # name = musicinfo['musicname']
    # gettrlink = musicinfo['musiclink']
    # singer = musicinfo['performers']
    # composer = musicinfo['Composer']
    # editor = musicinfo['Editor']
    # songwriter = musicinfo['Songwriter']
    # producer = musicinfo['Producer']
    # musiclyrics = musicinfo['Lyrics']
    # infoofmusic = models.MusicInfo(gettr_link=gettrlink,singername=singer,Composer=composer,create_date=createdate,Editor=editor,Songwriter=songwriter,Producer=producer)
    # addlyrics = models.MusicLyris(lyris = musiclyrics)
    # newre = models.Music(name = name, user_id = 1, coverimg=[])
    # try:
    #     app.session.add(infoofmusic)
    #     app.session.add(addlyrics)
    #     app.session.add(newre)
    #     app.session.commit()
    #     print(gettrlink)
    # except Exception as e:
    #     return make_response(e,500)
    # return make_response('Add %s and date record successfully' % gettrlink, 200) 
    return 'hello'


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

@app.route("/ratemusic",methods = ['POST'])
# @jwt_required
def ratemusic():
    # user_id = current_user.id
    musicid=request.json.get("musicid",None)
    musicgrade = request.json.get("musicscore",None)
    user_id =1 
    scoremusic = models.Score(grade = musicgrade, user_id=user_id,music_id=musicid)
    app.session.add(scoremusic)
    app.session.commit()
    return make_response('Add %s score successfully' % musicid, 200)

@app.route("/commentmusic",methods = ['POST'])
# @jwt_required
def commentmusic():
    # user_id = current_user.id
    musicid=request.json.get("musicid",None)
    musiccomment = request.json.get("comment",None)
    user_id =1 
    commentmusic = models.Music_Feedback(feedbackcomment = musiccomment, user_id=user_id,music_id=musicid)
    app.session.add(commentmusic)
    app.session.commit()
    return make_response('Add %s score successfully' % musicid, 200)

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

@app.route('/showmusicimage/<int:id>')
def get_musicimg(id):
    try:
        img = app.session.query(models.Music,models.Img).filter(id == models.Img.music_id).with_entities(models.Img.img,models.Img.mimetype).first()
        if not img:
            return make_response('Img Not Found!', 404)
    except Exception as e:
        print(e)
        return make_response("Wrong",400)

    return Response(img.img, mimetype=img.mimetype)
@app.route('/showuserimage/<int:id>')
def get_userimg(id):
    try:
        img = app.session.query(models.User,models.Img).filter(id == models.Img.user_id).with_entities(models.Img.img,models.Img.mimetype).first()
        if not img:
            return make_response('Img Not Found!', 404)
    except Exception as e:
        print(e)
        return make_response("Wrong",400)

    return Response(img.img, mimetype=img.mimetype)
    # try:
    #     img = app.session.query(models.Img).filter_by(id=id).first()
    #     if not img:
    #         return make_response('Img Not Found!', 404)
    # except Exception as e:
    #     print(e)
    #     return make_response("Wrong",400)

    # return Response(img.img, mimetype=img.mimetype)

@app.route('/showlyrics/<int:id>')
def showlyrics(id):
    lyrics ="今天我寒夜里看雪飘过\n怀著冷却了的心窝飘远方\n风雨里追赶\n雾里分不清影踪\n天空海阔你与我\n可会变(谁没在变)\n多少次迎著冷眼与嘲笑\n从没有放弃过心中的理想\n一刹那恍惚\n若有所失的感觉\n不知不觉已变淡\n心里爱(谁明白我)\n原谅我这一生不羁放纵爱自由\n也会怕有一天会跌倒\n被弃了理想谁人都可以\n那会怕有一天只你共我\nMusic\n仍然自由自我\n永远高唱我歌\n走遍千里 "
    return { 'lyrics':lyrics}
    # return jsonify()

@app.route('/listofuser/<int:listtype>')
def listofuser(listtype):
    if listtype == 4:
        records=app.session.query(models.User).all()
        # musicrecord = app.session.query(models.Music).all()
        # print(app.session.query(models.Music).options(selectinload(models.Music.coverimg)).all())
        # print(app.session.query(models.Music,models.Img).filter(models.Music.id == models.Img.music_id).with_entities(models.Img.img).all())
        # print(records)
    return jsonify([record.to_dict() for record in records])
    
@app.route('/userinfo/<int:user_id>/')
def oneuserinfo(user_id):
    record = app.session.query(models.User).filter(models.User.id==user_id).one()
    return jsonify(record.to_dict())

@app.route("/records/<int:user_id>/")
def playerwork(user_id):
    records = app.session.query(models.Music).filter(models.Music.user_id==user_id).all()
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


# if __name__ == '__main__':

#     app.run(host = '127.0.0.1',port=1943,debug=True)

