#Great in working with single file
#Right on! Both methods read from the current position. The readline() method reads one line, while read() reads until the end of the file.
with open("new.txt") as file:    #python automatically closes the file 
    print(file.readline()) 