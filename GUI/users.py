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

    def save(self):
        """
        Saves user to users.csv
        """
        with open(os.path.join("GUI", "users.csv"), "r") as file:
            reader = csv.reader(file)
            data = list(reader)
            for row in data:
                if row[0] == self.userID:
                    row[1] = self.username
                    row[2] = self.password
                    row[3] = self.role
                    row[4] = self.fname
                    row[5] = self.lname
                    row[6] = self.dob
                    row[7] = self.phonenumber
                    row[8] = self.emailaddress
                    break
        with open(os.path.join("GUI", "users.csv"), "w") as file:
            writer = csv.writer(file)
            writer.writerows(data)
