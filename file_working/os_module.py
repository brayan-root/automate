# whenever we're using an absolute path in our code, we need to make sure we can provide alternatives for the platforms we want to support

# The OS module lets us do pretty much all the same tasks that we can normally do e.g. changing file permissions,deleting,renaming when working with files from the command line
import os
os.path.exists("newnovel.txt") #using os.path submodule to check whether a file exists
os.remove("novel.txt") #To delete a file, we can use the, "Remove" function from the OS module.
os.rename("novel.txt", "newnovel.txt") #renaming a file
