from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from forms import AddData
from flask_mail import Mail, Message
import os

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
####################Configure################################

app.config['SECRET_KEY'] = 'mysecret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
############################# Mail config #####################
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'webdevpy1998@gmail.com'
app.config['MAIL_PASSWORD'] = '$hubhamK98'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True


##############################################################
db = SQLAlchemy(app)
Migrate(app, db)
mail = Mail(app)
################################################################


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = AddData()
    if form.validate_on_submit():
        name = form.name.data
        number = form.number.data
        msg = Message('Hello', sender='webdevpy1998@gmail.com',
                      recipients=['webdevpy1998@gmail.com'])
        msg.body = f"Customer name is {name} \n Customer phone number {number}"
        mail.send(msg)
        return redirect(url_for('sub'))
    return render_template('contact.html', form=form)


@app.route('/Sub')
def sub():
    return render_template('Sub.html')


if __name__ == '__main__':
    app.run()
