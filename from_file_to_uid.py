#!/usr/bin/python


import os
import sys
import subprocess
import re
import commands



def getGeneID(path):
	first_line = ""
	with open(path, 'r') as f:
		first_line = f.readline()
	first_line = first_line.split("|")
	return first_line[3].strip()


def runCommanForUID(geneBankID):
	return commands.getstatusoutput("""curl -s "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=""" +geneBankID +"""&rettype=fasta&retmode=xml"  |  grep TSeq_taxid | cut -d '>' -f 2 |  cut -d '<' -f 1 | tr -d "\n" """)




if len(sys.argv) < 2:
	print "Usage: ./program_name path to the file"
	exit()

path = sys.argv[1]

genbank_name = getGeneID(path)
status, UID = runCommanForUID(genbank_name)

if(not UID):
	print "the UID is not exist for: " + genbank_name
else:
	print "the geneBank ID is: " + genbank_name + "  and the UID is: " + UID

