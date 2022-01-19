#So it keeps moving forward. We can also call the read method, which reads from the current position until the end of the file instead of just one line.
#open=file=close method
file = open ("new.txt")
print(file.readline())#It reads line by line
print(file.read()) #It reds from where the cursor is to the end
file.close() #allow other program to use it i.e it is not locked