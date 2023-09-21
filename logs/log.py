# create a logger object that writes logs to a csv
# file and to the console
import sys
import os
import csv
from datetime import datetime
from enum import Enum
events = Enum('login', 'logout', 'create_user', 'delete_user', 'add_meds','remove_meds','add_rx',"remove_rx")

class logger:
    # constructor
    def __init__(self, filename):
        # open a file for writing in append mode
        assert(filename != None and filename != "", "filename cannot be None or empty")
        self.log_file = open(filename, 'a')
    # destructor
    def __del__(self):
        self.log_file.close()
    
    def log(self, log -> log_obj):
        # write msg to the file
        self.log_file.write(log)
        return

 
class log_obj:
    def __init__(self,event,user):
        self.timestamp = datetime.now() # when it was done
        self.event = event # what was done
        self.user = user # who did it


class event:
    def __init__(self, event_type, event_name, event_description):
        self.event_type = event_type
        self.event_name = event_name
        self.event_description = event_description