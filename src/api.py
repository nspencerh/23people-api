from flask import Flask, jsonify, request
from google.cloud import datastore

# Create a datastore client object to connect to Datastore.
# An Environment Variable called GOOGLE_APPLICATION_CREDENTIALS with the path
# to the Credential file must be created (Inside Dockerfile).
datastore_client = datastore.Client()

app = Flask(__name__)

################################################################################
#************* Returns all the elements in the Kind (Table) "people" **********#
################################################################################
@app.route("/people", methods=['GET'])
def api_return_all_people():
    try:
        if request.content_type != 'application/json':
            content_type_error_message = {"error": {"code": 400, "message": "Testing the pipeline...."}}
            return jsonify(content_type_error_message), 400
        else:
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
    except:
        message = {"error": {"code": 500, "message": "Internal error"}}
        return jsonify(message), 500

################################################################################
#******************* Returns a person based on his nationalId *****************#
################################################################################
@app.route("/people/<string:nationalId>", methods=['GET'])
def api_search_a_person(nationalId):
    try:
        if request.content_type != 'application/json':
            content_type_error_message = {"error": {"code": 400, "message": "Bad content_type"}}
            return jsonify(content_type_error_message), 400
        else:
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
                not_found_message = {"response": {"code": 404, "message": "Person not found"}}
                return jsonify(not_found_message), 404
    except:
        message = {"error": {"code": 500, "message": "Internal error"}}
        return jsonify(message), 500

################################################################################
#************* Inserts a Person in the Database based on a payload ************#
################################################################################
@app.route("/people", methods=['POST'])
def api_insert_a_person():
    try:
        #check if content_type is 'application/json'
        if request.content_type != 'application/json':
            content_type_error_message = {"error": {"code": 400, "message": "Bad content_type"}}
            return jsonify(content_type_error_message), 400
        else:
            #request data from POST payload
            request_data = request.get_json()
            #insert data into people Kind (table)
            insert = datastore.Entity(datastore_client.key('people'))
            insert.update(request_data)
            datastore_client.put(insert)
            success_message = {"response": {"code": 201, "message": "Person added successfully"}, "person": request_data}
            return jsonify(success_message), 201
    except:
        message = {"error": {"code": 500, "message": "Internal error"}}
        return jsonify(message), 500

################################################################################
#******************* Updates a person based on nationalId *********************#
################################################################################
@app.route("/people/<string:nationalId>", methods=['PUT'])
def api_update_a_person(nationalId):
    try:
        #check if content_type is 'application/json'
        if request.content_type != 'application/json':
            content_type_error_message = {"error": {"code": 400, "message": "Bad content_type"}}
            return jsonify(content_type_error_message), 400
        else:
            #query object with the Kind (Table) 'people' from Datastore
            query = datastore_client.query(kind='people')
            #add a filter so it returns only enities that match nationalId = input
            query.add_filter('nationalId', '=', nationalId)
            #fetch the results into a list of Entities (rows) objects
            entity_list = list(query.fetch())
            #if the list is not empty, delete every Entity (row) that matches nationalId
            #and add the new payload to Datastore
            if entity_list:
                #request data from PUT payload
                request_data = request.get_json()
                #deletes every entity that matches nationalId
                for entity in entity_list:
                    datastore_client.delete(datastore_client.key('people', entity.key.id))
                #insert the new payload after the previous is deleted
                insert = datastore.Entity(datastore_client.key('people'))
                insert.update(request_data)
                datastore_client.put(insert)

                success_message = {"response": {"code": 200, "message": "Successfully updated"}}
                return jsonify(success_message), 200
        #if the list is empty, it means the person was not found
            else:
                not_found_message = {"response": {"code": 404, "message": "Person not found"}}
                return jsonify(not_found_message), 404
    except:
        message = {"error": {"code": 500, "message": "Internal error"}}
        return jsonify(message), 500

################################################################################
#******************* Deletes a person based on nationalId *********************#
################################################################################
@app.route("/people/<string:nationalId>", methods=['DELETE'])
def api_delete_a_person(nationalId):
    try:
        if request.content_type != 'application/json':
            content_type_error_message = {"error": {"code": 400, "message": "Bad content_type"}}
            return jsonify(content_type_error_message), 400
        else:
            #query object with the Kind (Table) 'people' from Datastore
            query = datastore_client.query(kind='people')
            #add a filter so it returns only enities that match nationalId = input
            result = query.add_filter('nationalId', '=', nationalId)
            #fetch the results into a list of Entities (rows) objects
            entity_list = list(query.fetch())
            #if the list is not empty, delete every Entity (row) that matches nationalId
            if entity_list:
                for entity in entity_list:
                    datastore_client.delete(datastore_client.key('people', entity.key.id))
                success_message = {"response": {"code": 200, "message": "Person deleted successfully"}}
                return jsonify(success_message), 200
            #if the list is empty, it means the person was not found
            else:
                not_found_message = {"response": {"code": 404, "message": "Person not found"}}
                return jsonify(not_found_message), 404
    except:
        message = {"error": {"code": 500, "message": "Internal error"}}
        return jsonify(message), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("5000"), debug=True)
