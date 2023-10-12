import csv

"""_summary_
    
    First digit of userID specifies user type
    1 Patient
    2 Cashier
    3 Technician
    4 PharmacyManager
    
"""

def createUser(userID):
    """
    Finds user in users.csv by userID and creates object of said user    
    """
    with open("GUI/users.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if(row[0] == userID):
                print("found user " + userID)
                if(userID[0] == 1):
                    return Patient(row[1],row[2],row[3],row[4],row[5],row[6],row[7])
                if(userID[0] == 2):
                    return Cashier(row[1],row[2],row[3],row[4],row[5],row[6],row[7])
                if(userID[0] == 3):
                    return Technician(row[1],row[2],row[3],row[4],row[5],row[6],row[7])
                if(userID[0] == 4):
                    return PharmacyManager(row[1],row[2],row[3],row[4],row[5],row[6],row[7])
        raise Exception("The specified User DNE")
    
class User():
    def __init__(self,fname,lname,dob,address,phonenumber,emailaddress,insurance):
        self.fname = fname
        self.lname = lname
        self.dob = dob
        self.address = address
        self.phonenumber = phonenumber
        self.emailaddress = emailaddress
        self.insurance = insurance

class PharmacyManager(User):
    def __init__(self,fname,lname,dob,address,phonenumber,emailaddress,insurance):
        User.__init__(self,fname,lname,dob,address,phonenumber,emailaddress,insurance)
        
class Technician(User):
    def __init__(self,fname,lname,dob,address,phonenumber,emailaddress,insurance):
        User.__init__(self,fname,lname,dob,address,phonenumber,emailaddress,insurance)
        
class Cashier(User):
    def __init__(self, fname,lname,dob,address,phonenumber,emailaddress,insurance):
        User.__init__(self,fname,lname,dob,address,phonenumber,emailaddress,insurance)
        
class Patient(User):
    def __init__(self,fname,lname,dob,address,phonenumber,emailaddress,insurance):
        User.__init__(self,fname,lname,dob,address,phonenumber,emailaddress,insurance)
        
createUser("09000")