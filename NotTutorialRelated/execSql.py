import os,re
from subprocess import Popen, PIPE
from optparse import OptionParser

### ------------ Function Definitions ------------ ###

def getAllOracleSids():
    oracleSids = []
    p1 = Popen(["ps", "-ef"], stdout=PIPE)
    p2 = Popen(["grep", "pmon"], stdin=p1.stdout, stdout=PIPE)
    p3 = Popen(["grep", "-v", "grep"], stdin=p2.stdout, stdout=PIPE)
    p2.stdout.close()
    p1.stdout.close() 
    output = p3.communicate()[0].split(os.linesep)
    for line in output:
        if line:
            oracleSids.append(line.split("_")[-1])
    return oracleSids

def checkParameters(instances, sqlfile):
    for instance in instances:
        if instance not in getAllOracleSids():
            print "Instance \"%s\" not a valid oracle sid" % (instance)
            break
    if not os.path.isfile(sqlfile):
        print "File \"%s\" not found." % (os.path.abspath(options.sqlScript))

### ------------ Main Routine ------------ ###

instanceNames = []
parser = OptionParser()

parser.add_option("-d", "--instance", dest="instanceNames", action="append", type="string",
    help="INSTANCE NAME to connect, accept multiple entries [-d <instance1>, ... -d <instance2>]", 
    metavar="INSTANCE_NAME")
parser.add_option("-s", "--script", dest="sqlScript", 
    help="SQL SCRIPT to be executed", metavar="SQL_SCRIPT")

(options, args) = parser.parse_args()

checkParameters(options.instanceNames, options.sqlScript)

