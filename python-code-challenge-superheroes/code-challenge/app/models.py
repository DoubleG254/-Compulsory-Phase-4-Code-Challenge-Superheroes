from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# models.py



class Hero(db.Model):
    __tablename__="heroes"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    super_name = db.Column(db.String(50), nullable=False)
    powers = db.relationship('HeroPower', backref='hero', lazy=True)

class Power(db.Model):
    __tablename__="powers"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), nullable=False)
    description = db.Column(db.String(20), nullable=False)
    heroes = db.relationship('HeroPower', backref='power', lazy=True)

class HeroPower(db.Model):
    __tablename__="heropower "
    id = db.Column(db.Integer, primary_key=True)
    strength = db.Column(db.String(50), nullable=False)
    hero_id = db.Column(db.Integer, db.ForeignKey('hero.id'), nullable=False)
    power_id = db.Column(db.Integer, db.ForeignKey('power.id'), nullable=False)

 