#!/usr/bin/env python3
import csv
import sys
'''
python 2csv_reader_parsing_and_write.py supplier_data.csv ./output_files/1output.csv
'''
input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file, 'r', newline='') as csv_in_file:
	with open(output_file, 'w', newline='') as csv_out_file:
		filereader = csv.reader(csv_in_file, delimiter=',')
		filewriter = csv.writer(csv_out_file, delimiter=',')
		for row_list in filereader:
			print(row_list)
			filewriter.writerow(row_list)