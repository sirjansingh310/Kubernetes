from flask import Flask, render_template,request, url_for,redirect
app = Flask(__name__)
@app.route('/')
def index():
	return render_template('input.html')
@app.route('/thankyou',methods=['POST'])
def index2():
	if request.method=="POST":
		inp = request.form['input']+'\n'
		fileob = open('database/database.txt','a')
		fileob.write(inp)
		fileob.close()
	return render_template('thankyou.html',text=inp)
if __name__ == '__main__':
	app.run(host='0.0.0.0',port=5555)
