# render template is to render the html file imported from flask
from fileinput import filename
from random import seed
from flask import Flask, render_template, request, session, redirect

# import flask sql Alchemy
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# import json file
import json
from matplotlib.style import use


# import os for file uploader ka liya use hota hai yeah
import os

# import math file for mathematic operation
import math

# this is also used for file name
from werkzeug.utils import secure_filename

from psutil import users
from pytest import param
from sympy import content


# to send mails
# from flask_mail import Mail

with open('config.json', 'r') as c:
    params = json.load(c)["params"]

local_server = True

app = Flask(__name__)
# secret-key for login purpose
app.secret_key = 'super-secret-key'
app.config['UPLOAD_FOLDER'] = params['upload_location']

# to send mails
# app.config.update(
#     MAIL_SERVER='smtp.gmail.com',
#     MAIL_PORT='465',
#     MAIL_USE_SSL=True,
#     MAIL_USERNAME=params['gmail_username'],
#     MAIL_PASSWORD=params['gmail_password']
# )

# mail=Mail(app)


# connect to database
# if we ave install XAMP withput any password then username will be root and the password will be null

# syntax
# app.config['SQLALCHEMY_DATABASE_URI']='mysql://username:password@localhost/db_name'

if(local_server):
    app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['prod_uri']

db = SQLAlchemy(app)


class Contacts(db.Model):
    '''
    sno, name phone_num, msg, date, email
    '''
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    phone_num = db.Column(db.String(12), nullable=False)
    msg = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(12), nullable=True)
    email = db.Column(db.String(20), nullable=False)


class Posts(db.Model):
    '''
    sno, name phone_num, msg, date, email
    '''
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    slug = db.Column(db.String(21), nullable=False)
    content = db.Column(db.String(120), nullable=False)
    tagline = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(12), nullable=True)
    img_file = db.Column(db.String(12), nullable=True)


@app.route("/")
def home():

    posts = Posts.query.filter_by().all()
    last = math.ceil(len(posts)/int(params['no_of_post']))

    page = request.args.get('page')
    if(not str(page).isnumeric()):
        page = 1
    page = int(page)
    posts = posts[(page-1)*int(params['no_of_post']):(page-1) *
                  int(params['no_of_post'])+int(params['no_of_post'])]
    # pagination logic
    # # First
    # prev=#
    # next=page+1
    # # Middle
    # prev=page-1
    # next=page+1
    # # last
    # prev=page-1
    # next=#

    if(page == 1):  # first
        prev = "#"
        next = "/?page="+str(page+1)
    elif(page == last):  # last
        prev = "/?page="+str(page-1)
        next = "#"
    else:  # middle
        prev = "/?page="+str(page-1)
        next = "/?page="+str(page+1)

    return render_template('index.html', params=params, posts=posts, prev=prev, next=next)


@app.route("/about")
def about():
    return render_template('about.html', params=params)


@app.route("/dashboard", methods=['GET', 'POST'])
def dashboard():

    if ('user' in session and session['user'] == params['admin_user']):
        posts = Posts.query.all()
        return render_template('dashboard.html', params=params, posts=posts)

    if request.method == 'POST':
        username = request.form.get('uname')
        userpass = request.form.get('pass')
        if(username == params['admin_user'] and userpass == params['admin_password']):
            # set the session variable
            session['user'] = username
            posts = Posts.query.all()
            return render_template('dashboard.html', params=params, posts=posts)

    return render_template('login.html', params=params)


@app.route("/edit/<string:sno>", methods=['GET', 'POST'])
def edit(sno):
    if ('user' in session and session['user'] == params['admin_user']):
        if request.method == "POST":
            tline = request.form.get('tline')
            box_title = request.form.get('title')
            slug = request.form.get('slug')
            content = request.form.get('content')
            img_file = request.form.get('img_file')
            date = datetime.now()

            if sno == '0':
                post = Posts(title=box_title, slug=slug, content=content,
                             tagline=tline, img_file=img_file, date=date)
                db.session.add(post)
                db.session.commit()

            else:
                post = Posts.query.filter_by(sno=sno).first()
                post.box_title = box_title
                post.tline = tline
                post.slug = slug
                post.content = content
                post.img_file = img_file
                post.date = date

                db.session.commit()
                return redirect('/edit/'+sno)

        post = Posts.query.filter_by(sno=sno).first()
        return render_template('edit.html', params=params, post=post, sno=sno)
    # return render_template('edit.html', params=params, post=post)


@app.route("/uploader", methods=['GET', 'POST'])
def uploader():
    if ('user' in session and session['user'] == params['admin_user']):
        if(request.method == 'POST'):
            f = request.files['file1']
            f.save(os.path.join(
                app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
            return "Uploaded successfully"


@app.route("/logout")
def logout():
    session.pop('user')
    return redirect('/dashboard')


@app.route("/delete/<string:sno>", methods=['GET', 'POST'])
def delete(sno):
    if ('user' in session and session['user'] == params['admin_user']):
        post = Posts.query.filter_by(sno=sno).first()
        db.session.delete(post)
        db.session.commit()
    return redirect('/dashboard')


@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if(request.method == 'POST'):
        '''Add entry to the database'''
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')
        entry = Contacts(name=name, phone_num=phone,
                         msg=message, date=datetime.now(), email=email)
        db.session.add(entry)
        db.session.commit()

        # mail.send_message('New message from ' + name,
        #                 sender=email,
        #                 recipients=[params['gmail_username']],
        #                 body=message + "\n" + phone
        #                 )

    return render_template('contact.html', params=params)


@app.route("/post/<string:post_slug>", methods=['GET'])
def post_route(post_slug):
    post = Posts.query.filter_by(slug=post_slug).first()
    return render_template('post.html', params=params, post=post)


# debug=True is used if you make any chances it will automatically reload the server for you
app.run(debug=True)
