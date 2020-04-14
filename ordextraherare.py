import re

databasen = open("orddatabas.txt", "r")

databasen = databasen.readline()



"""
(^(de\s.[^\s]+)|(het\s.[^\s]+))|(^\w+)
regex för att ta första ordet i dessa utan stopptecken:
dag!			goddag!
de basiswoorden		grundordförråd
het woord		ord
de begroeting		hälsning

"""
#(^(de\s.[^\s]+)|(het\s.[^\s]+))|(^\w+)

dehet = ["de", "het"]
ordet = ""
for i in databasen:
        if i.isspace() and ordet[:2] is not in dehet and len(ordet) !> 3:
               

