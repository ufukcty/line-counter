#!/usr/bin/python
# -*- coding: utf-8 -*-

'''

Project - Line Counter Project

Parametres configured in settings.txt
Output contain input file count.

@Author Ufuk Cagatay Alkis

'''
import sys
import os
from datetime import datetime
from settings import Output_file, Input_file


time_format = datetime.today().strftime('%Y-%m-%d')

def config_file_parser():
	input_file_name = Input_file
	if input_file_name is None:
		input_file_name = "input.txt"
	output_file_name = Output_file
	if output_file_name is None:
		output_file_name = time_format

	# clear spaces in string
	input_file_name = input_file_name.strip()
	output_file_name = output_file_name.strip()

	return input_file_name, output_file_name


if __name__ == '__main__':

	input_file_name, output_file_name = config_file_parser()

	try:
		#input file open and calculate line count
		input_file = open(input_file_name)

		line_count = 0
		for i in input_file:
			line_count = line_count + 1

		input_file.close()
	except Exception as ex:
		print("Input File Not Found")
		# close the program
		sys.exit(0)

	# check this output file
	count = 1
	while True:
		if os.path.isfile(output_file_name) == True:
			output_file_name = time_format + "_" + str(count)
		else:
			break
		count = count + 1

	# write line count in output
	# \n for new line
	with open(output_file_name, 'w') as f:
	    f.write(str(line_count) + "\n")

	sys.stdout.write("Success!\n")
