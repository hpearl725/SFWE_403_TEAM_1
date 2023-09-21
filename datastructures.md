# The following document will outline the archtecture for the following objects:
- Logger
- Log
- Event
  
## Logger
description: The idea behind this object is that it is created on login, then when the user does anything it logs the event by that user, the only thing that it takes as input is a filename. TBD (could have it take user info too) 
### inputs:
 - filename: this is the name of the file which logs will be added to. Note file must be a csv
### methods:
 - log: this function when called will create

## Log
description: The idea behind this object is that it is created everytime a user logs in, logs out, fills meds, adds an rx, removes rx, adds inventory, removes inventory, etc. It will need to include the date and time, user name, role.

## Event
description: The idea behidn this object is it will be the parent for the events listed in log, but will have all info needed to be written to logs
