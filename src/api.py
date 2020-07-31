from flask import Flask, abort, jsonify

app = Flask(__name__)

people = [
    {'nationalId': '12345678-9',
     'name': 'Hari',
     'lastName': 'Seldon',
     'age': 45,
     'originPlanet': 'helicon',
     'pictureUrl': 'https://your.picture.com/hari-seldon'},
    {'nationalId': '435434-9',
     'name': 'Samuel',
     'lastName': 'Gomez',
     'age': 36,
     'originPlanet': 'Saturno',
     'pictureUrl': 'https://your.picture.com/samuel-gomez'},
    {'nationalId': '345345-5',
     'name': 'Andres',
     'lastName': 'Jelvez',
     'age': 37,
     'originPlanet': 'Marte',
     'pictureUrl': 'https://your.picture.com/andres-jelvez'}
]
#########################################################
# Returns all the elements in the table (Kind) "people" #
#########################################################
@app.route("/people", methods=['GET'])
def api_return_all_people():
    return jsonify(people)
############################################
# Returns a person based on his nationalId #
############################################
@app.route("/people:<string:nationalId>", methods=['GET'])
def api_search_a_person(nationalId):
    result = None
    for person in people:
        if person['nationalId'] == nationalId:
            result = person
    if result is None:
        abort(404, description="Person not found")
    return jsonify(result)

#To handle a 404 status when a person is not found
@app.errorhandler(404)
def person_not_found(e):
    return jsonify(response=str(e)), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("5000"), debug=True)
