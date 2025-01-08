# import the dependencies
from flask_cors import CORS
from pprint import pprint
import pymongo
from bson.json_util import dumps
from bson import json_util
import json
from flask import Flask, jsonify, Response

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# create a database
mydb = myclient["merteorite_landings_db"]

# list all the databases
#print(myclient.list_database_names())

 #Create a collection called "landings":
landings = mydb["landings"]

# Create an app, being sure to pass __name__
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
@app.route("/")
def home():
    return ("""
<h1>Welcome to the Meteorite Landings Application API!</h1>
<img src="https://img.freepik.com/free-photo/milky-way-illum…d-generated-by-ai_24640-93529.jpg?semt=ais_hybrid?" alt="Meteorite Landings"/>
</style>	
		
		<div id="map-locator-filter"> 
			<form id="form-map-locator" action="" name="form-map-locator" method="post" >
				<div class="row">
					<div class="col-xs-12 col-sm-12 col-md-12">
						<div class="row" style="background-color: tan;padding: 20px 5px 5px 5px;">
							<div class="col-xs-12">
								<div class="col-sm-3">
									<div class="mb">
										<div class="icon"><img src="https://impact.uwo.ca/wp-content/plugins/map-locator//images/hypervelocity.png"></div>
										<div  class="txt">Meterorite Shower</div>
										<div style="clear:both;"></div>
									

<h2>Available API's</h2>
            
<p>Meteorite-Landings:</p>
<ul>
  <li><a href="/api/v1.0/meteorite-landings">/api/v1.0/meteorite-landings</a></li>
</ul>

<p>First-Record:</p>
<ul>
  <li><a href="/api/v1.0/meteorite-landings/first-record">/api/v1.0/meteorite-landings/first-record</a></li>
</ul>

<p>Unique-Years:</p>
<ul>
  <li><a href="/api/v1.0/meteorite-landings/unique-years">/api/v1.0/meteorite-landings/unique-years</a></li>
</ul>

<p>Count-All-Years:</p>
<ul>
  <li><a href="/api/v1.0/meteorite-landings/count-all-years">/api/v1.0/meteorite-landings/count-all-years</a></li>
</ul>

<p>Maximum-Year:</p>
<ul>
  <li><a href="/api/v1.0/meteorite-landings/max-year-count">/api/v1.0/meteorite-landings/max-year-count</a></li>
</ul>
            
<p>Specific Meteor Name:</p> 
<ul>
  <li><a href="/api/v1.0/meteorite-landings/name/<name>">/api/v1.0/meteorite-landings/name/<name></a></li>
</ul>
            
<p>Specific Landing Year:</p> 
<ul>
  <li><a href="/api/v1.0/meteorite-landings/year/<int:year>">/api/v1.0/meteorite-landings/year/<int:year></a></li>
</ul>
</html>
""")

# Select all landings
@app.route("/api/v1.0/meteorite-landings")
def filter_landings():
    try:
        # Example query with multiple filters (year and mass)
        query = {'year': 1979, 'mass': {'$gt': 1000}}  # Mass greater than 1000g
        results = landings.find(query)
        
        # Convert MongoDB cursor to a list of dictionaries
        results_list = list(results)
        
        if not results_list:
            return jsonify({"message": "No meteorite landings found with the given criteria."}), 404
        
        # Return the filtered results as JSON
        return Response(
            json.dumps(results_list, default=json_util.default), 
            status=200, 
            mimetype='application/json'
        )
    except Exception as e:
        return jsonify({"message": str(e)}), 500


# Define when user select particular document based on name
@app.route("/api/v1.0/meteorite-landings/name/<name>")
def search_by_name(name):
  
        query = {'name': name}
        results = landings.find(query)
        return dumps(results), 200, {'Content-Type': 'application/json'}
   

# Select first recorded landing
@app.route("/api/v1.0/meteorite-landings/first-record")
def first_doc():
    result=landings.find_one()
    #print(f"name {list[result]}")
    return dumps(result), 200, {'Content-Type': 'application/json'}

# Select various types of landinng years
@app.route("/api/v1.0/meteorite-landings/unique-years")
def get_unique_years():
    # Use distinct to get unique values of the 'year' field
    unique_years = landings.distinct('year')

    # Return the result as a JSON response
    return jsonify({"unique_years": unique_years}), 200 

@app.route("/api/v1.0/meteorite-landings/count-all-years")
def count_meteorites_by_year():
    # MongoDB aggregation pipeline
    pipeline = [
        {"$group": {
            "_id": "$year",  # Group by the 'year' field
            "count": {"$sum": 1}  # Count the number of meteorites in each year
        }},
        {"$sort": {"_id": 1}}  # Optional: Sort the years in ascending order
    ]
    
    # Run the aggregation pipeline
    result = list(landings.aggregate(pipeline))

    # Format the response as a dictionary
    response = []
    for doc in result:
        year_count = {
            "year": doc["_id"],
            "meteorite_count": doc["count"]
        }
        response.append(year_count)
    return jsonify(response), 200

# Define when user select particular document based on year
@app.route("/api/v1.0/meteorite-landings/year/<int:year>")
def search_by_year(year):
    try:
        # Query MongoDB for the given year
        query = {'year': year}
        results = landings.find(query)
        
        # Convert the results to a list of dictionaries
        results_list = list(results)
        
        if not results_list:
            return jsonify({"message": "No meteorite landings found for this year."}), 404
        
        # Return the results as JSON with json_util to handle MongoDB-specific types
        return Response(
            json.dumps(results_list, default=json_util.default), status=200, mimetype='application/json'
        )
    
    except ValueError:
        # In case the year is not a valid integer
        return jsonify({"message": "Invalid year format."}), 400
    except Exception as e:
        # General error handling
        return jsonify({"message": str(e)}), 500

@app.route("/api/v1.0/meteorite-landings/max-year-count")
def max_meteorites_by_year():
    # MongoDB aggregation pipeline
    pipeline = [
        {"$group": {
            "_id": "$year",  # Group by the 'year' field
            "count": {"$sum": 1}  # Count the number of meteorites in each year
        }},
        {"$sort": {"count": -1}},  # Sort by count in descending order (highest count first)
        {"$limit": 1}  # Get only the first document (the one with the highest count)
    ]
    
    # Run the aggregation pipeline
    result = list(landings.aggregate(pipeline))

    # Check if result is not empty and return the response
    if result:
        max_year_data = result[0]  # Get the document with the maximum count
        response = {
            "year": max_year_data["_id"],
            "meteorite_count": max_year_data["count"]
        }
        return jsonify(response), 200
    else:
        return jsonify({"message": "No data found"}), 404
    

if __name__ == "__main__":
    app.run(debug=True)

