import os
import re
from optparse import OptionParser

# --------------- Declare Stuff --------------- #


countries = ["CO", "PA"]
spool = re.compile('^spool[ ]+c..temp/', flags=re.IGNORECASE)
alterSessBra = re.compile('CURRENT_SCHEMA.BRAXTS.CFG')
alterSessBatch = re.compile('CURRENT_SCHEMA.BATCHMODULE')
alterSessRepWeb = re.compile('CURRENT_SCHEMA.REPORTWEB')


# -------------- Main Routine


parser = OptionParser()

parser.add_option("-s", "--script", dest="sqlScript",
                    help="SQL Script to be formatted")

(options, args) = parser.parse_args()

if not options.sqlScript:
    parser.error("No script received.")
else:
    for country in countries:
        countryFileName = os.path.dirname(sqlScript) + "/" + country + "_" + os.path.basename(sqlScript)
        with open(sqlScript, "r") as baseScript:
            with open(countryFileName, "w") as countryFile:
                for line in baseScript.readlines():
                    if spool.search(line):
                        countryFile.write(spool.sub("SPOOL " + country + "_", line))
                    elif alterSessRepWeb.search(line):
                        countryFile.write(line.replace("REPORTWEB", "REPORTWEB_" + country))
                    elif alterSessBra.search(line):
                        if country == "PA":
                            countryFile.write(line.replace("BRAXTS_CFG", "BRAXTS_AC_CFG"))
                        else:
                            countryFile.write(line.replace("BRAXTS_CFG", "BRAXTS_" + country + "_CFG"))
                    elif alterSessBatch.search(line):
                        if country == "MX":
                            countryFile.write(line)
                        else:
                            countryFile.write(line.replace("BATCHMODULE", "BATCHMODULE_" + country))
                    else:
                        countryFile.write(line)