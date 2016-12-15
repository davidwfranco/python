from sys import argv
import os.path

script, filename = argv

while not os.path.isfile(filename):
    print "File not found!"
    filename = raw_input("Insert the correct filename:")

#file = open(filename, 'r').read
text = open(filename, 'r').read()

print "That's what you've writed on the previous script:" + "\n"

for i in text.split():
    print i 

print "\n"