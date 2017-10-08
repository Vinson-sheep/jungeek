#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask,render_template

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
	
if __name__ == '__main__':
    app.run()