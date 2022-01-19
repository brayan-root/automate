import os

os.path.abspath("new.txt")
file = "new.txt"
if os.path.isfile(file):
    print(os.path.isfile(file))
    print(os.path.getsize(file))
else:
    print("File not found")
    
    





