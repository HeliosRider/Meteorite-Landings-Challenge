#Import dependencies

import os
import csv
import numpy as np
import pandas as pd
import datetime as dt

# Python SQL toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from flask import Flask, jsonify

#################################################
# Database Setup
#################################################

MetLandings = os.path.join("C:\Class\Challenges\MOD 16 Challenge\Meteorite-Landings-Challenge\Resources\Meteorite_Data.csv")

# Verify database incorporates the correct csv data

# Open and read csv
with open(MetLandings, encoding='UTF-8') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    
    # Read the header row of csv file
    csv_header = next(csv_reader)
    
    # Print the header
    print("Header:", csv_header)
    
    # Initialize a list to store the rows
    data_rows = []
    
    # Read each row in the csv
    for row in csv_reader:
        data_rows.append(row)

# Print the data rows
    for row in data_rows:
        print(row)

# Create our session (link) from Python to the DB
session = Session (MetLandings)

#################################################
# Flask Setup
#################################################

app = Flask(__name__)

#################################################
# Flask Routes
#################################################

@app.route("/")

@app.route("/api/v1.0/name")
def names():

    """Return a list of all meteorite names"""
    # Query all meteorites
    results = session.query(MetLandings.name).all()

    session.close()

    # Convert list of tuples into normal list
    all_names = list(np.ravel(results))

    return jsonify(all_names)

if __name__ == '__main__':
    app.run(debug=True)

