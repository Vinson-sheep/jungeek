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

app = Flask(__name__)

@app.route('/',methods=['GET'])
def home():
	return render_template('home.html')

@app.route('/login',methods=['GET'])
def login():
	return render_template('login.html')
	
@app.route('/enrol',methods=['GET'])
def preSign():
	return render_template('preSign.html')
	
@app.route('/mascot',methods=['GET'])
def mascot():
	return render_template('mascot.html')

@app.route('/we_are',methods=['GET'])
def we_are():
	return render_template('we_are.html')

@app.route('/data_show',methods=['GET'])
def data_show():
	return render_template('data_show.html')

@app.route('/join_us',methods=['GET'])
def join_us():
	return render_template('join_us.html')

@app.route('/singleday',methods=['GET'])
def singleDay():
	return render_template('singleDay.html')	

# follow two APIs belong a group
# singleDayApiPost Function is for posting form
# as well as posting the data into mysql database
@app.route('/singleday/api',methods=['POST'])	
def singleDayApiPost():
	# use request object to get data
	# a = request.get_data()
	# dict1 = json.loads(a)
	# get data from dict1
	# gender = dict1['gender']
	# question = dict1['question']
	# answer = dict1 ['answer']
	# options = dict1['options']
	# wechat = dict1['wechat']
	gender = urllib.parse.unquote(request.form['gender'])
	question = urllib.parse.unquote(request.form['question'])
	answer = urllib.parse.unquote(request.form['answer'])
	options = urllib.parse.unquote(request.form['options'])
	wechat = urllib.parse.unquote(request.form['wechat'])
	# link to database
	db = pymysql.connect("localhost", username, password, database,use_unicode=True, charset="utf8")
	# get cursor
	cursor = db.cursor()
	# write sql statemens
	sql = '''insert into singleday (time,gender,question,answer,options,wechat)
			values (now(), '%s', '%s', '%s', '%s', '%s') ''' % (gender, question, answer, options, wechat)
	try:
		cursor.execute(sql)
		#when you change database, you should commit
		db.commit()
	except:
		db.rollback()
		return "fail"
	
	db.close()
	return "successful"
	
# With singleDayApiGet Function
# we can get the whole datasingleday of singleday table
@app.route('/singleday/api',methods=['GET'])
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
	try:
		cursor.execute(sql)
		result = cursor.fetchall()
		for row in result:
			b = {}
			b['time'] = row[0]
			b['gender'] = gender_change[row[1]]
			b['question'] = row[2]
			b['answer'] = row[3]
			b['options'] = row[4]
			b['wechat'] = row[5]
			data.append(b)
		# after for circle
		data = json.dumps(data)
		
	except:
		print('error in singleDayApiGet Function')
		
		
	db.close()
	return data
	
# this API is for message-checking
# when it is matched , it will return a boolen true
@app.route('/logincheck/api',methods=['POST'])
def loginCheck():
	# get json data
	username = urllib.parse.unquote(request.form['username'])
	password = urllib.parse.unquote(request.form['password'])
	# define your right message
	right_username = "shiting@jnu.com"
	right_password = "abc123"
	result = ""
	
	if username==right_username and password==right_password:
		result = "true"
	else:
		result = 'false'
		
	return result
	
if __name__ == '__main__':
    app.run()