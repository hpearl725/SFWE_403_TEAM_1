# create a logger object that writes logs to a csv
# file and to the console
# contains class logger, log_obj, and event
from datetime import datetime
from enum import Enum
events = Enum('Events', ['login', 'logout', 'create_user', 'delete_user',
              'add_meds', 'remove_meds', 'add_rx', "remove_rx"])


class logger:
    """
    This class represents a logger object that writes logs to a CSV file and to the console.

    :param filename: The name of the CSV file to write logs to.
    :type filename: str
    """
    def __init__(self, filename):
        """
        Constructor for the logger class.

        :param filename: The name of the CSV file to write logs to.
        :type filename: str
        """
        assert filename != None and filename != "", "filename cannot be None or empty"
        self.log_file = open(filename, 'a')

    def __del__(self):
        """
        Destructor for the logger class.
        """
        self.log_file.close()

    def log(self, log):
        """
        Writes a log entry to the CSV file.

        :param log: The log object to be written.
        :type log: log_obj
        """
        assert type(log) == log_obj
        self.log_file.write(log.write())
        self.log_file.write('\n')  # Add a line break after each entry
        return


class log_obj:
    """
    This class represents a log object.

    :param event: The event associated with the log.
    :type event: event
    :param user: The user associated with the log.
    :type user: str
    """
    def __init__(self, event, user):
        """
        Constructor for the log_obj class.

        :param event: The event associated with the log.
        :type event: event
        :param user: The user associated with the log.
        :type user: str
        """
        self.timestamp = datetime.now()  # when it was done
        self.event = event  # what was done
        self.user = user  # who did it
        return

    def write(self):
        #TODO could make user and event objects have write methods that return strings
        """
        Writes the log entry as a string.

        :return: The log entry as a string.
        :rtype: str
        """
        return f"{self.timestamp},{self.user},{self.event.get_info()}"


class event:
    """
    This class represents an event.

    :param event_type: The type of the event.
    :type event_type: str
    :param event_name: The name of the event.
    :type event_name: str
    :param event_description: The description of the event.
    :type event_description: str
    """
    def __init__(self, event_type, event_name, event_description):
        #TODO to determine flow for use of event, will likely need objects
        """
        Constructor for the event class.

        :param event_type: The type of the event.
        :type event_type: str
        :param event_name: The name of the event.
        :type event_name: str
        :param event_description: The description of the event.
        :type event_description: str
        """
        self.event_type = event_type
        self.event_name = event_name
        self.event_description = event_description
        return

    def get_info(self):
        """
        Gets the information of the event as a string.

        :return: The information of the event as a string.
        :rtype: str
        """
        return f"{self.event_name},{self.event_type},{self.event_description}"
