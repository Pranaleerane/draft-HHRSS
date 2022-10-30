# %%
# patient dp.server.py


"""
Database format
[{
"patient_id": <patient_id>,
"attending_username": <attending_username_string>,
"patient_age": <patient_age>, # in years
"heart_rate": [<heart_rate_int>,<heart_rate_int>, ...]
"status": [<status_string>,<status_string>, ...]
"timestamp": [<time_stamp_string>,<time_stamp_string>, ...]
}]
"""
db_patient = []


# from email import message
# from flask import Flask, request, jsonify


# app = Flask(__name__)


# @app.route("/", methods = ["GET"])
# def server_on():
#     """
#         GET route to indicate that server is turned on
#     """
#     return "DB server is on"


def add_patient(patient_id, attending_username, patient_age):
    """
        Appends a new patient dictionary to the databse list
        This function recives basic information of a new patient, creates a
        dictionary containing that information

        Args:
            patient_id (int): Patient assigned ID
            attending_username (str): Full name of a doctor
            patient_age (int): Age of the patient
            heart_rate (lst): Heart rates of the patient
            status (lst): "tachycardic" or "not tachycardic"
                          for each heart rate.
            timestamp(lst): Time stamps for the heart rates.

        Returns:
            None
    """
    new_patient = {"patient_id": patient_id,
                   "attending_username": attending_username,
                   "patient_age": patient_age,
                   "heart_rate": [],
                   "status": [],
                   "timestamp": []
                   }
    db_patient.append(new_patient)


def print_patient_db():
    """
        Print the attending database to the console.
    """
    print("** Patient Database Output **")
    for i, patient in enumerate(db_patient):
        print("{}: {};".format(i, patient))
        print("\n")


def init_server():
    """
        Initial database for the program.
        Returns:
            None
    """
    add_patient(1, "Smith James", 23)
    add_patient(2, "Patrik Wang", 40)
    add_patient(3, "Patrik Wang", 65)
    print_patient_db()


if __name__ == "__main__":
    init_server()
    # app.run()
