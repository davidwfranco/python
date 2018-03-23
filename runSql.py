import os
from subprocess import Popen, PIPE
from optparse import OptionParser

# ------------ Function Definitions ------------ #


def getAllOracleSids():
    oracleSids = []
    p1 = Popen(["ps", "-ef"], stdout=PIPE)
    p2 = Popen(["grep", "pmon"], stdin=p1.stdout, stdout=PIPE)
    p3 = Popen(["grep", "-v", "grep"], stdin=p2.stdout, stdout=PIPE)
    p4 = Popen(["grep", "-v", "ASM"], stdin=p3.stdout, stdout=PIPE)
    p3.stdout.close()
    p2.stdout.close()
    p1.stdout.close()  # Allow p1 to receive a SIGPIPE if p2 exits.
    output = p4.communicate()[0].split(os.linesep)
    for line in output:
        if line:
            oracleSids.append(line.split("_")[-1])
    return oracleSids


def checkSid(instances):
    for instance in instances:
        if instance not in getAllOracleSids():
            parser.error("Instance \"%s\" not a valid oracle sid" % (instance))
    return True


def checkScript(sqlFile):
    if not os.path.isfile(sqlFile):
        parser.error("File \"%s\" not found." % (os.path.abspath(sqlFile)))
    return True


def runSqlQuery(sqlCommand, connectString, instanceName):
    session = Popen(['sqlplus', '-S', connectString],
                    stdin=PIPE, stdout=PIPE, stderr=PIPE)
    session.stdin.write(sqlCommand)
    return session.communicate()


# ------------ Main Routine ------------ #

instanceNames = []
parser = OptionParser()

parser.add_option("-u", "--user", dest="dbUser",
                  help="database user", metavar="DB_USER")
parser.add_option("-p", "--password", dest="dbPassword",
                  help="database password", metavar="DB_PASSWORD")
parser.add_option("-i", "--instance", dest="instanceNames", action="append",
                  type="string", help="INSTANCE NAME to connect accept " +
                  "multiple entries [-i <instance1>, ... -i <instanceN>] or " +
                  "[-i ALL] for all instances",
                  metavar="INSTANCE_NAME")
parser.add_option("-s", "--script", dest="sqlScript",
                  help="SQL SCRIPT to be executed", metavar="SQL_SCRIPT")

(options, args) = parser.parse_args()

if not options.instanceNames or not options.sqlScript:
    parser.error("Incorrect Number of Arguments")
elif "ALL" in str(options.instanceNames).upper():
    checkScript(options.sqlScript)
    print("Instances: All")
else:
    checkScript(options.sqlScript)
    checkSid(options.instanceNames)

if options.dbUser and options.dbPassword:
    connectString = "%s/%s" % (options.dbUser, options.dbPassword)
else:
    connectString = "/ as sysdba"

sqlCommand = "@" + options.sqlScript

if os.path.dirname(options.sqlScript):
    logFile = os.path.dirname(options.sqlScript) + "/log_" + os.path.split(options.sqlScript)[1].replace(".sql", "")
else:
    logFile = "log_" + os.path.split(options.sqlScript)[1].replace(".sql", "")

if os.path.isfile(logFile):
    os.remove(logFile)

with open(logFile, 'a') as logF:
    if "ALL" in str(options.instanceNames).upper():
        for sid in getAllOracleSids():
            os.environ['ORACLE_SID'] = sid
            queryResult, queryError = runSqlQuery(sqlCommand, connectString,
                                                  options.instanceNames[0])
            logF.write("Result Set %s: \n%s" % (sid,
                                                  # time.strftime("%Y%m%d-%H%M"),
                                                  queryResult))
            if queryError:
                logF.write("Eror %s: \n%s" % (sid,
                                                # time.strftime("%Y%m%d-%H%M"),
                                                queryError))
    else:
        print("Instance: %s" % str(options.instanceNames))
        for sid in options.instanceNames:
            os.environ['ORACLE_SID'] = sid
            queryResult, queryError = runSqlQuery(sqlCommand, connectString,
                                                  options.instanceNames[0])
            logF.write("Result Set %s: \n%s" % (sid,
                                                  # time.strftime("%Y%m%d-%H%M"),
                                                  queryResult))
            if queryError:
                logF.write("Eror %s: \n%s" % (sid,
                                                # time.strftime("%Y%m%d-%H%M"),
                                                queryError))

