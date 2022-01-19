import os
import datetime
os.path.getsize("new.txt") # returns the size of the file
os.path.getmtime("new.txt") # timestamp when a file was last modified
timestamp = os.path.getmtime("new.txt")
datetime.datetime.fromtimestamp(timestamp) #e're using the fromtimestamp method of the datetime class inside the datetime module.