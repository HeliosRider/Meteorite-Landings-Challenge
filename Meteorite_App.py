# Import Python SQL toolkit and Object Relational Mapper

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, Column, Integer, String, Float

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from flask import Flask, jsonify

#################################################
# Database Setup
#################################################

# Create an SQLite engine
engine = create_engine('sqlite:///Meteorites_data.db')

 #Create the session (link) from Python to the DB
session = Session (engine)

# Define the base class
Base = declarative_base()

# Define the meteorites table as a class
class Meteorite(Base):
    __tablename__ = 'meteorites'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    mass = Column(Integer)
    year = Column(Integer)
    GeoLocation = Column(String)


#################################################
# Flask Setup
#################################################

app = Flask(__name__)

#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """list all available API routes"""
    return """
<h1>Welcome to the Meteorite Landings Application API!</h1>

<img src="https://img.freepik.com/free-photo/milky-way-illum…d-generated-by-ai_24640-93529.jpg?semt=ais_hybrid?" alt="Meteorite Landings"/>
<p>Name:</p>
<ul>
  <li><a href="/api/v1.0/Name">/api/v1.0/Name</a></li>
</ul>
<p>Mass(g):</p>
<ul>
  <li><a href="/api/v1.0/Mass(g)">/api/v1.0/Mass(g)</a></li>
</ul>
<p>Year:</p>
<ul>
  <li><a href="/api/v1.0/Year">/api/v1.0/Year</a></li>
</ul>
<p>GeoLocation:</p>
<ul>
  <li><a href="/api/v1.0/GeoLocation">/api/v1.0/GeoLocation</a></li>
</ul>
</html>
"""

@app.route("/api/v1.0/Name")
def names():
   
    """Return a list of all meteorite names"""
    # Query all meteorites
    results = session.query(Meteorite.name).all()
    names = [name for name, in results]

    session.close()

    return jsonify(names)

# #app routing for meteorites mass 
@app.route("/api/v1.0/Mass(g)")
def mass():
  
    """Return a list of the mass of all meteorites"""
    # Query all meteorites
    results = session.query(Meteorite.mass).all()
    names = [name for name, in results]

    session.close()

    return jsonify(names)

# #app routing for year meteorites fell
@app.route("/api/v1.0/Year")
def year():

    """Return a list of the impact year of all meteorites"""
    # Query all meteorites
    results = session.query(Meteorite.year).all()
    names = [name for name, in results]

    session.close()

    return jsonify(names)

# #app routing lat/Lon
@app.route("/api/v1.0/GeoLocation")
def GeoLocation():

    """Return a list of the lat/lon of all meteorites"""
    # Query all meteorites
    results = session.query( Meteorite.GeoLocation).all()
    names = [name for name, in results]

    session.close()

    return jsonify(names)

if __name__ == '__main__':
    app.run(debug=True)