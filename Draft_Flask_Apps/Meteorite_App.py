# Import Python SQL toolkit and Object Relational Mapper

<<<<<<< HEAD
=======
#import csv
#import numpy as np
#import pandas as pd
#import datetime as dt

# Python SQL toolkit and Object Relational Mapper
>>>>>>> 44d444a380ad098f4a991c40cef8c5fd88d90b2c
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

<<<<<<< HEAD
# Create an SQLite engine
engine = create_engine('sqlite:///Meteorites_data.db')
=======
#os.path.join("C:\Class\Challenges\Meteorite-Landings-Challenge\Resources\Meteorite_Data.csv")
>>>>>>> 44d444a380ad098f4a991c40cef8c5fd88d90b2c

 #Create the session (link) from Python to the DB
session = Session (engine)

<<<<<<< HEAD
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

=======
# Open and read csv
#with open(MetData_csv, encoding='UTF-8') as csv_file:
   # csv_reader = csv.reader(csv_file, delimiter=",")
    
    # Read the header row of csv file
    #csv_header = next(csv_reader)
    
    # Print the header
    #print(f"Header: {csv_header}")
    
    # Initialize a list to store the rows
    #data_rows = []
    
    # Read each row in the csv
    #for row in csv_reader:
        #data_rows.append(row)

# Print the data rows
    #for row in data_rows:
        #print(row)
# Create an SQLite engine
engine = create_engine('sqlite:///meteorite_data.db')

 #Create the session (link) from Python to the DB
session = Session (engine)

# Read the CSV file into a pandas DataFrame
#df = pd.read_csv("C:\Class\Challenges\Meteorite-Landings-Challenge\Resources\Meteorite_Data.csv")

# Write the DataFrame to an SQL table
#df.to_sql('meteorites', con=engine, if_exists='replace', index=False)

# Query the table to check if data is inserted
#result = pd.read_sql('SELECT * FROM meteorites', con=engine)
#print(result.head())

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

# Create all tables (this is required if you're not sure if the table exists)
#Base.metadata.create_all(engine)

# Create a session
#Session = sessionmaker(bind=engine)
#session = Session()

# Query the data
#Meteorites = session.query(Meteorite).all()

# Print the results
#for meteorite in Meteorites:
    #print(meteorite.name, meteorite.year)


# reflect an existing database into a new model
#Base = automap_base()

# reflect the tables
#Base.prepare(autoload_with=engine)

# Save reference to the table
#Meteorites = Base.classes.keys()
>>>>>>> 44d444a380ad098f4a991c40cef8c5fd88d90b2c

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
<<<<<<< HEAD
=======
    #print(names)
>>>>>>> 44d444a380ad098f4a991c40cef8c5fd88d90b2c

    session.close()

    return jsonify(names)

# #app routing for meteorites mass 
@app.route("/api/v1.0/Mass(g)")
def mass():
<<<<<<< HEAD
  
=======
    # Create the session (link) from Python to the DB
    #session = Session (engine )

>>>>>>> 44d444a380ad098f4a991c40cef8c5fd88d90b2c
    """Return a list of the mass of all meteorites"""
    # Query all meteorites
    results = session.query(Meteorite.mass).all()
    names = [name for name, in results]
<<<<<<< HEAD
=======
    #print(names)
>>>>>>> 44d444a380ad098f4a991c40cef8c5fd88d90b2c

    session.close()

    return jsonify(names)

# #app routing for year meteorites fell
@app.route("/api/v1.0/Year")
def year():
<<<<<<< HEAD
=======
    # Create the session (link) from Python to the DB
    #session = Session (engine )
>>>>>>> 44d444a380ad098f4a991c40cef8c5fd88d90b2c

    """Return a list of the impact year of all meteorites"""
    # Query all meteorites
    results = session.query(Meteorite.year).all()
    names = [name for name, in results]
<<<<<<< HEAD
=======
    #print(names)
>>>>>>> 44d444a380ad098f4a991c40cef8c5fd88d90b2c

    session.close()

    return jsonify(names)

# #app routing lat/Lon
@app.route("/api/v1.0/GeoLocation")
def GeoLocation():
<<<<<<< HEAD
=======
    # Create the session (link) from Python to the DB
    #session = Session (engine )
>>>>>>> 44d444a380ad098f4a991c40cef8c5fd88d90b2c

    """Return a list of the lat/lon of all meteorites"""
    # Query all meteorites
    results = session.query( Meteorite.GeoLocation).all()
    names = [name for name, in results]
<<<<<<< HEAD
=======
    #print(names)
>>>>>>> 44d444a380ad098f4a991c40cef8c5fd88d90b2c

    session.close()

    return jsonify(names)

if __name__ == '__main__':
    app.run(debug=True)