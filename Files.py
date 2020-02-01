# Python functions for creating, updating, reading, and deleting files.

# Open a file

myFile = open('myfile.txt', 'w')

#Get some info
print('Name:', myFile.name)
print('Is Closed:', myFile.closed)
print('Opening Mode:', myFile.mode)

# write to file
myFile.write('This is python code')
myFile.write(' for writing into files')
myFile.close()

# Append to file
myFile = open('myfile.txt', 'a')
myFile.write(' Python is good')
myFile.close()

#Read from file
myFile = open('myFile.txt', 'r+')
text = myFile.read(100)
print(text)
