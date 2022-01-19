#If you open a file for writing and the file already exists, the old contents will be deleted as soon as the file is opened
with open("new.txt","a") as file: #"w" it is a mode =write only "r"=read only "a" =append "r+" =can both read contents and overwrite it
    file.write("It was first published in 1920, more as a song for adults in Camp and camino in lower California with the words blooming, bloody instead of itsy bitsy.")
file = open ("new.txt")
print(file.read()) #It reds from where the cursor is to the end
file.close() 