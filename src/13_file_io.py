"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

# YOUR CODE HERE

with open("./foo.txt") as fooFile:
    for line in fooFile:
        print(line, end='')
    fooFile.close()

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make 
# sure that it contains what you expect it to contain

# YOUR CODE HERE
print('')

with open("./bar.txt", 'w') as barFile:
    barFile.write("1\n")
    barFile.write("2\n")
    barFile.write("3\n")
    barFile.close()

with open("bar.txt") as barFile:
    for line in barFile:
        print(line, end="")
    barFile.close()