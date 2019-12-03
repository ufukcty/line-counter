#!/usr/bin/python
# -*- coding: utf-8 -*-

'''

Project 1 - File Operations Project

Parametres configured in settings.txt
Output contain input file count.

@Author Ufuk Cagatay Alkis

'''
import sys
import os
from datetime import datetime

try:
    #config file assignment
	configFile = open("settings.txt")
	# settings file reading
	count = 0
	for i in configFile:
		if count == 0:
			inputFileName = i
		if count == 1:
			outputFileName = i
		count = count + 1
	configFile.close()
except:
	inputFileName = "input.txt"
	outputFileName = datetime.today().strftime('%Y-%m-%d')


# clear spaces in string
inputFileName = inputFileName.strip()
outputFileName = outputFileName.strip()

try:
	#input file open and calculate line count
	inputFile = open(inputFileName)

	lineCount = 0
	for i in inputFile:
		lineCount = lineCount + 1

	inputFile.close()
except:
	print("Input File Not Found")
	# close the program
	sys.exit(0)

# check this output file
count = 1
while True:
	if os.path.isfile(outputFileName) == True:
		outputFileName = datetime.today().strftime('%Y-%m-%d') + "_" + str(count)
	else:
		break
	count = count + 1

# write line count in output
# \n for new line
with open(outputFileName, 'w') as f:
    f.write(str(lineCount) + "\n")



