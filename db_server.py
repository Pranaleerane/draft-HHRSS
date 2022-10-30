# db_server.py

from flask import Flask, request, jsonify
import logging

"""
    Database format: A list of new attending

    [
        {"attending_username": <string>,
        "attending_email": <string>,
        "attending_phone": <string>}
    ]
"""

db_attending = []

app = Flask(__name__)

@app.route("/", methods=["GET"])
def server_on():
    """
        GET route to indicate that server is turned on
    """
    return "DB server is on"

def add_attending(attending_username, attending_email, attending_phone):
    """
        Appends a new attending dictionary to the databse list

        This function recives basic information of a new attending doctor, creates a 
        dictionary containing that information

        Args:
            attending_username (str): Full name of a doctor
            attending_email (str): The email of the doctor
            attending_phone (str): The phone number of the doctor
        
        Returns: 
            None
    """
    new_attending = {"attending_username": attending_username,
                     "attending_email": attending_email,
                     "attending_phone": attending_phone}
    db_attending.append(new_attending)

def print_attending_database():
    """
        Print the attending database to the console in order to visual changes to the
        database during server operation
    """
    print("\n** Attending Database Output **")
    for i, doctor in enumerate(db_attending):
        print("{}: {};".format(i, doctor))
        print("\n")


def init_database():
    """
        Initializes database upon program start

        Returns:
            None
    """
    add_attending("Smith James", "smith.james@example_hospital.com", "919-555-1212")
    add_attending("Patrik Wang", "patrik.wang@example_hospital.com", "919-222-3434")
    print_attending_database()

if __name__ == "__main__":
    init_database()
    # app.run()
