from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Float
import os
from flask_marshmallow import Marshmallow

#config of flask app & what dir to store database file
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'api.db')

#SQLAlchemy & Marshmallow applications assigned to variables
db = SQLAlchemy(app)
ma = Marshmallow(app)

#SQLAlchemy/Flask CLI command to create api.db
@app.cli.command('db_create')
def db_create():
    db.create_all()
    print('Database created!')

#SQLAlchemy/Flask CLI command to delete contents in api.db DOES NOT REMOVE FILE
@app.cli.command('db_drop')
def db_drop():
    db.drop_all()
    print('Database dropped!')

#SQLAlchemy/Flask CLI command to seed data to api.db
@app.cli.command('db_seed')
def db_seed():
    mercury = Planet(planet_name='Mercury',
                     planet_type='Class D',
                     home_star='Sol',
                     mass=2.258e23,
                     radius=1516,
                     distance=35.98e6)

    venus = Planet(planet_name='Venus',
                         planet_type='Class K',
                         home_star='Sol',
                         mass=4.867e24,
                         radius=3760,
                         distance=67.24e6)

    earth = Planet(planet_name='Earth',
                     planet_type='Class M',
                     home_star='Sol',
                     mass=5.972e24,
                     radius=3959,
                     distance=92.96e6)

    db.session.add(mercury)
    db.session.add(venus)
    db.session.add(earth)

#test user added to api.db
    test_user = User(first_name='test',
                     last_name='user',
                     email='test@test.com',
                     password='password')


    db.session.add(test_user)
    db.session.commit()
    print('Database seeded!')

#404 test
@app.route('/not_found')
def not_found():
   return jsonify(message='Data requested not found :('), 404

@app.route('/planets', methods=['GET'])
def planets():
    planets_list = Planet.query.all()
    result = planets_schema.dump(planets_list)
    return jsonify(result)

#signup route where users pass 'email', 'first_name', 'last_name' and 'password' parameters to signup
@app.route('/signup', methods =['POST'])
def signup():
    email = request.form['email']
    test = User.query.filter_by(email=email).first()
    if test:
        return jsonify(message='Your email is already registered to the data base.'), 409
    else:
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        password = request.form['password']
        user = User(first_name=first_name, last_name=last_name, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        return jsonify(message="User created sucessfully."), 201


# database models
class User(db.Model):
    ___tablename___ = 'users'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)

class Planet(db.Model):
    __tablename__ = 'planets'
    planet_id = Column(Integer, primary_key=True)
    planet_name = Column(String)
    planet_type = Column(String)
    home_star = Column(String)
    mass = Column(Float)
    radius = Column(Float)
    distance = Column(Float)

class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'first_name', 'last_name', 'email', 'password')


class PlanetSchema(ma.Schema):
    class Meta:
        fields = ('planet_id', 'planet_name', 'planet_type', 'home_star', 'mass', 'radius', 'distance')


user_schema = UserSchema()
users_schema = UserSchema(many=True)

planet_schema = PlanetSchema()
planets_schema = PlanetSchema(many=True)

if __name__ == '__main__':
   app.run()
