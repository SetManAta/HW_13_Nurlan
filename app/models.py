from app import db, bcrypt,login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Transactions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    period = db.Column(db.String, nullable=False,unique=True)
    value = db.Column(db.Integer)
    status = db.Column(db.String)
    unit = db.Column(db.String)
    subject = db.Column(db.String)

    def __repr__(self):
        return f'{self.period}'- {self.value}

class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False,unique=True)
    password_hash = db.Column(db.String,nullable=False)

    def __repr__(self):
        return self.username
    
    @property
    def password(self):
        return None


    @password.setter
    def password(self,password):
        self.password_hash = bcrypt.generate_password_hash(password)

    def check_password(self,password):
        return bcrypt.check_password_hash(self.password_hash, password)
