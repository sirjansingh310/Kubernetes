from flask import Flask, render_template,request, url_for,redirect
import os.path
app = Flask(__name__)
@app.route('/')
def output():
	if os.path.isfile('database/database.txt'):
	    fp = open('database/database.txt','r')
	    contents = fp.read()
	    fp.close()
	    return contents
	return "Database not created!"
	
if __name__ == '__main__':
	app.run(host='0.0.0.0',port=7777)
