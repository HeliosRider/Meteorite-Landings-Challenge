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
from flask import Flask, jsonify

# Create an app, being sure to pass __name__
app = Flask(__name__)

@app.route("/")
def home():
    return (
        f"<h1>Welcome to Merteorite Landings API!</h1>"
        f"<h2>Available Routes:</h2>"
        f"<h2>/api/v1.0/merteorite-landings</h2>"
        f"<h2>/api/v1.0/merteorite-landings/<mert_name></h2>"
        f"<h2>/api/v1.0/merteorite-landings/first-rec</h2>"
        f"<h2>/first-rec</h2>"
    )

@app.route("/first-rec")
def first_doc():
    result=landings.find_one()
    #print(f"name {list[result]}")
    return dumps(result), 200, {'Content-Type': 'application/json'}

# Select all the documents
@app.route("/api/v1.0/merteorite-landings")
def all_rec():
    #print all the documents 
    result=landings.find()
    #print(f"name {list[result]}")
    return dumps(result), 200, {'Content-Type': 'application/json'}

# Define when user select particular document based on name
@app.route("/api/v1.0/merteorite-landings/<mert_name>")
def search_by_name(mert_name):
    #Find the number of landings with name ; AAchen'
    query = {'name': mert_name}
    results= landings.find(query)
    return dumps(results), 200, {'Content-Type': 'application/json'}



# Define when user select particular document based on 
@app.route("/api/v1.0/merteorite-landings/<mert_year>")
def search_by_year(mert_year):
    #Find the number of landings with name ; AAchen'
    query = {'year': mert_year}
    results= landings.find(query)
    return dumps(results), 200, {'Content-Type': 'application/json'}



   

if __name__ == "__main__":
    app.run(debug=True)
