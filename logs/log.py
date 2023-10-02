# create a logger object that writes logs to a csv
# file and to the console
# contains class logger, log_obj, and event
from datetime import datetime
from enum import Enum
events = Enum('Events', ['login', 'logout', 'create_user', 'delete_user',
              'add_meds', 'remove_meds', 'add_rx', "remove_rx"])


class logger:
    # constructor
    # This function __init__ is part of this module.
    def __init__(self, filename):
        # open a file for writing in append mode
        assert filename != None and filename != "", "filename cannot be None or empty"
        self.log_file = open(filename, 'a')
    # destructor

    # This function __del__ is part of this module.
    def __del__(self):
        self.log_file.close()

    # This function log is part of this module.
    def log(self, log):
        # write msg to the file
        assert type(log) == log_obj
        self.log_file.write(log.write())
        self.log_file.write('\n')  # Add a line break after each entry
        return


class log_obj:
    # This function __init__ is part of this module.
    def __init__(self, event, user):
        self.timestamp = datetime.now()  # when it was done
        self.event = event  # what was done
        self.user = user  # who did it
        return

    # This function write is part of this module.
    def write(self):
        # note could make user and event objects have write methods that return strings
        return f"{self.timestamp},{self.user},{self.event.get_info()}"


class event:
    # This function __init__ is part of this module.
    def __init__(self, event_type, event_name, event_description):
        # need to determine flow for use of event, will likely need objects
        self.event_type = event_type
        self.event_name = event_name
        self.event_description = event_description
        return

    # This function get_info is part of this module.
    def get_info(self):
        return f"{self.event_name},{self.event_type},{self.event_description}"
