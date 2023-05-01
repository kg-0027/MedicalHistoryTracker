from flask import Flask, jsonify, request
from db_connector import ItemDatabase
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)


# Trial API
@app.route('/')
@cross_origin(origin='*')
def hello_world():
    return 'Hello, World!'

# API for getting details of all students


@app.route('/student/all')
@cross_origin(origin='*')
def all_student_rec():
    result = db.get_details_all()
    return jsonify(result)

# API for getting details of only one student whose enroll is given


@app.route('/student/<int:id>')
@cross_origin(origin='*')
def student_rec(id):
    result = db.get_details_roll(id)
    return jsonify(result)

# API for getting getting all medical records in the system


@app.route('/students/medrec/all')
@cross_origin(origin='*')
def all_medrec():
    result = db.get_all_med()
    return jsonify(result)

# API for putting the medical record of a student in the database


@app.route('/postapi', methods=["POST"])
@cross_origin(origin='*')
def add_medrec():
    data_json = request.get_json(force=True)
    id = data_json['enroll']

    med_rec = {
        'symptoms': data_json['symptoms'],
        'disease': data_json['disease'],
        'treatment': data_json['treatment'],
        'referred': data_json['referred'],
        'critical': data_json['critical']
    }
    db.add_record(id, med_rec)
    # return saved successfully message
    return jsonify({"message": "Saved Successfully"})


# API for getting the all the med records of the student whose enroll is mentioned
@app.route('/students/medrec/id/<int:id>')
@cross_origin(origin='*')
def get_medrec_enroll(id):
    medrec = db.get_med_roll(id)
    return jsonify(medrec)

# API for getting the all the med records of the particular date


@app.route('/students/medrec/date', methods=["POST"])
@cross_origin(origin='*')
def get_medrec_date():
    data_json = request.get_json(force=True)
    date = data_json['date']
    medrec = db.get_med_date(date)
    return jsonify(medrec)


if __name__ == "__main__":
    global db
    db = ItemDatabase()
    app.run(debug=True)
