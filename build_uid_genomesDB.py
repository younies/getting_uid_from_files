#!/usr/bin/python
"""
this program is going to call every thing and build the genome data base using theri Uids 
"""

import os
import sys
import subprocess
import re
import commands

file_for_all_names = "/export1/project/hondius/newKrakenResearch/Building_genomes_database_tools/all_names.txt"

path_to_genomeDB = "/export1/project/hondius/newKrakenResearch/genomesDatabaseNewUIDs/"

def getGeneID(path):
	first_line = ""
	with open(path, 'r') as f:
    	first_line = f.readline()
	first_line = first_line.split("|")
	return first_line[3].strip()



def runCommanForUID(geneBankID):
	return commands.getstatusoutput("""curl -s "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=""" +geneBankID +"""&rettype=fasta&retmode=xml"  |  grep TSeq_taxid | cut -d '>' -f 2 |  cut -d '<' -f 1 | tr -d "\n" """)


file_for_all_names = open(file_for_all_names, 'r')
all_files = file_for_all_names.split("\n")
file_for_all_names.close()


print "#!/bin/bash"


for aFile in all_files:
	status , output = runCommanForUID(    getGeneID(aFile)   )
	if(status != 0 or not output):
		print ("the uid does not exist for : " + aFile + "   and the gi is " + getGeneID(aFile))
	else:
		runCommanForUID( "cat " + aFile + "  >>  " + path_to_genomeDB + output + ".fa")

