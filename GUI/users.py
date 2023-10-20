import csv
import os
"""_summary_
    
    First digit of userID specifies user type
    1 Patient
    2 Cashier
    3 Technician
    4 PharmacyManager
    
"""

def createUser(userID):
    """
    Finds user in users.csv by userID and creates an object of said user    
    """
    with open(os.path.join("GUI", "users.csv"), "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == userID:
                # print("Found user " + userID)
                return User(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
        raise Exception("The specified User DNE")

    
class User():
    def __init__(self, userID, username, password, role, fname, lname, dob, phonenumber, emailaddress):
        self.userID = userID
        self.username = username
        self.password = password
        self.role = role
        self.fname = fname
        self.lname = lname
        self.dob = dob
        self.phonenumber = phonenumber
        self.emailaddress = emailaddress

if __name__ == "__main__":
    createUser("09000")