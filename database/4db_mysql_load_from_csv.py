#!/usr/bin/env python3
import csv
# import MySQLdb
import pymysql
import sys
from datetime import datetime, date
# MySQLdb python 2 에서만 지원됨.

'''
python 2db_insert_rows.py ./supplier_data_for_mysql_database.csv
'''

# Path to and name of a CSV input file
input_file = sys.argv[1]

# Connect to a MySQL database
con = pymysql.connect(host='localhost', port=3306, database='my_suppliers', user='root', passwd='Qwer12#$')
c = con.cursor()

# Read the CSV file
# Insert the data into the Suppliers table
file_reader = csv.reader(open(input_file, 'r'), delimiter=',')
header = next(file_reader)
for row in file_reader:
	data = []
	for column_index in range(len(header)):
		if column_index < 4:
			data.append(str(row[column_index]).lstrip('$').replace(',', '').strip())
		else:
			a_date = datetime.date(datetime.strptime(str(row[column_index]), '%m/%d/%y'))
			# %Y: year is 2016; %y: year is 15
			a_date = a_date.strftime('%Y-%m-%d')
			data.append(a_date)
	print(data)
	c.execute("""INSERT INTO Suppliers VALUES (%s, %s, %s, %s, %s);""", data)
con.commit()

# Query the Suppliers table
c.execute("SELECT * FROM Suppliers")
rows = c.fetchall()
for row in rows:
	row_list_output = []
	for column_index in range(len(row)):
		row_list_output.append(str(row[column_index]))
	print(row_list_output)
