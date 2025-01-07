#Import dependencies
import pandas as pd

# Python SQL toolkit and Object Relational Mapper

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify
mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.3.3
#################################################
# Database Setup
#################################################
# Create the session (link) from Python to the DB
#from sqlalchemy import inspect

# Create the SQLite engine

engine = create_engine('sqlite:///Meteorites_data.db')

# Create an inspector object to inspect the database
#inspector = inspect(engine)

# Get all table names in the database
#print(inspector.get_table_names())

#session = Session (engine)

# Reflect Database into ORM classes

#Base = automap_base()
#Base.prepare(autoload_with=engine)

# Save reference to the table

#Meteorites = Base.classes.meteorites
#print(Meteorites)

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
    
    query = "SELECT name FROM meteorites;"
    df = pd.read_sql(query, engine)
    names = df.to_dict(orient='records')

    return names

# #app routing for meteorites mass 
@app.route("/api/v1.0/Mass(g)")
def mass():

    """Return a list of the mass of all meteorites"""
    # Query all meteorites
    results = session.query(Meteorites.mass).all()
    names = [name for name, in results]

    session.close()

    return jsonify(names)

# #app routing for year meteorites fell
@app.route("/api/v1.0/Year")
def year():

    """Return a list of the impact year of all meteorites"""
    # Query all meteorites
    results = session.query(Meteorites.year).all()
    names = [name for name, in results]

    session.close()

    return jsonify(names)

# #app routing lat/Lon
@app.route("/api/v1.0/GeoLocation")
def GeoLocation():
 
    """Return a list of the lat/lon of all meteorites"""
    # Query all meteorites
    results = session.query( Meteorites.GeoLocation).all()
    names = [name for name, in results]

    session.close()

    return jsonify(names)

if __name__ == '__main__':
    app.run(debug=True)

