# import the dependencies
from pprint import pprint
import pymongo
from bson.json_util import dumps

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# create a database
mydb = myclient["merteorite_landings_db"]

# list all the databases
print(myclient.list_database_names())

 #Create a collection called "landings":
landings = mydb["landings"]
# print("\n",landings.find_one());

# Import the dependencies.
from flask import Flask, jsonify, Response

# Create an app, being sure to pass __name__
app = Flask(__name__)

@app.route("/")
def home():
    return (
        f"<h1>Welcome to Merteorite Landings API!</h1>"
        f"<h2>Available Routes:</h2>"
        f"<h2>/api/v1.0/meteorite-landings</h2>"
        f"<h2>/api/v1.0/meteorite-landings/name?</h2>"
        f"<h2>/api/v1.0/meteorite-landings/first-rec</h2>"
        f'<h2>/api/v1.0/meteorite-landings/unique-years</h2>'
        f'<h2>/api/v1.0/meteorite-landings/count-all-years</h2>'
        f'<h2>/api/v1.0/meteorite-landings/year/<int:year></h2>'
        f'<h2>/api/v1.0/meteorite-landings/max-year-count</h2'
    )

@app.route("/api/v1.0/meteorite-landings/first-rec")
def first_doc():
    result=landings.find_one()
    #print(f"name {list[result]}")
    return dumps(result), 200, {'Content-Type': 'application/json'}

# Select all the documents
@app.route("/api/v1.0/meteorite-landings")
def all_rec():
    #print all the documents 
    result=landings.find()
    #print(f"name {list[result]}")
    return dumps(result), 200, {'Content-Type': 'application/json'}

# Define when user select particular document based on name
@app.route("/api/v1.0/meteorite-landings/<mert_name>")
def search_by_name(mert_name):
    #Find the number of landings with name ; AAchen'
    query = {'name': mert_name}
    results= landings.find(query)
    return dumps(results), 200, {'Content-Type': 'application/json'}


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
    # Query MongoDB for the given year
    query = {'year': year}
    results = landings.find(query)
    # Return the results as JSON
    return Response(
        dumps(results),
        status=200,
        mimetype='application/json'
    ) 




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
