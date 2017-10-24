#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask,render_template,request
import pymysql
import json

import urllib
from urllib import parse

# database message
database = "jnugeek"
username = "root"
password = "abc123"

def singleDayApiGet():
	# initialize data object
	data = []
	# make an dict for value changing
	gender_change = {
		"female" : "女",
		"male" : "男",
		"both" : "both"
	}
	# connect to mysql database
	db = pymysql.connect('localhost', username, password, database,use_unicode=True, charset="utf8")
	# get cursor
	cursor = db.cursor()
	# write mysql statements
	sql = '''select time,gender,question,answer,options,wechat from singleday
			order by time desc'''

	cursor.execute(sql)
	result = cursor.fetchall()
	for row in result:
		b = {}
		b['time'] = row[0].strftime("%Y-%m-%d %H:%M:%S")
		b['gender'] = gender_change[row[1]]
		b['question'] = row[2]
		b['answer'] = row[3]
		b['options'] = row[4]
		b['wechat'] = row[5]
		data.append(b)
	# after for circle
	data = json.dumps(data)
	print(data)
	db.close()
	return data
	
singleDayApiGet();