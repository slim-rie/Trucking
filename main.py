from flask import Flask, render_template, request, redirect, session, flash
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__) 

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'SADPROJECT'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@localhost/payrolltrucking'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_POOL_SIZE'] = 20
    app.config['SQLALCHEMY_POOL_RECYCLE'] = 3600
    app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
        'pool_pre_ping': True,
        'pool_timeout': 30,
        'connect_args': {
            'connect_timeout': 30
        }
    }

@app.route('/', methods=['GET'])
def login():      
    return render_template("login.html") 

@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up():      
    return render_template("sign_up.html") 


if __name__ == '__main__':
    app.run(debug=True)
