from sys import argv
import os.path

script, filename = argv

while not os.path.isfile(filename):
    filename = raw_input("""File not found!
        Insert the correct filename: """)

file = open(filename, 'w')

print "Truncating the file..."
file.truncate()

text = raw_input("Insert some text to write on file: ")

file.write(text + "\n")

print "Saving file and ending this ex."

file.close
