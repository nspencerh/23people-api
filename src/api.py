from flask import Flask, abort, jsonify
from google.cloud import datastore

# Create a datastore client object to connect to Datastore.
# An Environment Variable called GOOGLE_APPLICATION_CREDENTIALS with the path
# to the Credential file must be created (Inside Dockerfile).
datastore_client = datastore.Client()

app = Flask(__name__)

#########################################################
# Returns all the elements in the Kind (Table) "people" #
#########################################################
@app.route("/people", methods=['GET'])
def api_return_all_people():
    #query object with the Kind (Table) 'people' from Datastore
    query = datastore_client.query(kind='people')
    #fetch the results into a list of Entities (rows) objects
    entity_list = list(query.fetch())
    #empty list where results will be stores
    results = []
    #convert every Entity into a Dictionary (json) and append to results list
    for entity in entity_list:
        results.append(dict(entity))

    return jsonify(results)
############################################
# Returns a person based on his nationalId #
############################################
@app.route("/people:<string:nationalId>", methods=['GET'])
def api_search_a_person(nationalId):
    #query object with the Kind (Table) 'people' from Datastore
    query = datastore_client.query(kind='people')
    #add a filter so it returns only enities that match nationalId = input
    query.add_filter('nationalId', '=', nationalId)
    #fetch the results into a list of Entities (rows) objects
    entity_list = list(query.fetch())
    #empty list where results will be stores
    results = []
    #convert every Entity into a Dictionary (json) and append to results list
    for entity in entity_list:
        results.append(dict(entity))
    if results:
        return jsonify(results[0])
    else:
        abort(404, description="Person not found")

#To handle a 404 status when a person is not found
@app.errorhandler(404)
def person_not_found(e):
    return jsonify(response=str(e)), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("5000"), debug=True)
