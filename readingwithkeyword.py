#Great in working with single file
#Right on! Both methods read from the current position. The readline() method reads one line, while read() reads until the end of the file.
with open("new.txt") as file:    #python automatically closes the file 
    print(file.readline()) 
    
#Using a "with" block is a good way to open and work on a single file then have the file automatically closed at the end of the block. On the flip side, using open outside of a block means we can use a file object in other places in our code. So we're not restricted to just one single block.