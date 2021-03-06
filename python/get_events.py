#!/usr/bin/python2.7
import cgitb; cgitb.enable()
import MySQLdb
import cgi
from helper import connectDb, sendJson, encrypt
import cgitb; cgitb.enable()

try: import simplejson as json
except ImportError: import json

# Connect to database
try:
	cursor, connection = connectDb()
except Exception as e:
	print("Status: 400 Database Connection Error\n")
	print e
	exit(1)

# Get information from database
try:
	cursor.execute("SELECT * from VMS_events")
	return_data = cursor.fetchall()
except Exception as e:
	print("Status: 200 Invalid SQL\n")
	exit(1)

try:
	data = {}
	# Insert data into josn format
	for i in range(len(return_data)):
		event = {}
		event.update({'event_name':return_data[i][1]})
		event.update({'start_date':str(return_data[i][3])})
		event.update({'end_date':str(return_data[i][4])})
		data.update({'event_id: '+str(return_data[i][0]):event})

	print "Content-type: application/json\n"
	print ""
	print sendJson(data)
except Exception as e:
		print("Status: 400 Cannot Get Events\n")
		print e
		exit(1)
