from extension import db 


class User(db.Model):    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    priority = db.Column(db.Integer, default=0)
