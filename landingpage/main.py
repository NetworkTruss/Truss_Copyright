from flask import *
import sqlite3
import re

app = Flask(__name__)


# email verification start
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
def check(email):
    if(re.fullmatch(regex, email)):
    	return True
    else:
    	return False
# email verification stop


@app.route('/')
def home_page():
	return render_template('index.html')

#chaching submission
@app.route('/chaching_values',methods = ['POST', 'GET'])
def chaching_values():
	if request.method == 'POST':
		pricing_3=request.form['pricing_3']
		pricing_6=request.form['pricing_6']
		pricing_12=request.form['pricing_12']

		con = sqlite3.connect("landing_page.sqlite3")
		cur = con.cursor()
		try:
			cur.execute("INSERT into chaching (month_3, month_6, month_12) values (?,?,?)",(pricing_3, pricing_6, pricing_12))
			con.commit()
		except:
			con.rollback()
		return redirect(url_for('home_page'))

#ngo/npo
@app.route('/ngo_npo')
def ngo_npo():
	return render_template('ngo_npo.html')

#registering ngo and npo
@app.route('/ngo_npo_registered',methods = ['POST', 'GET'])
def ngo_npo_registered():
	if request.method == 'POST':
		name=request.form['name']
		e_mail=request.form['email']
		organization=request.form['organization']
		teaching=request.form['teaching']
		reason=request.form['reason']

		if(check(e_mail)):
			con = sqlite3.connect("landing_page.sqlite3")
			cur = con.cursor()
			try:
				cur.execute("INSERT into ngo_npo (name, email, organization, willing_to_teach, reason_to_teach) values (?,?,?,?,?)",(name, e_mail, organization, teaching, reason))
				con.commit()
			except:
				con.rollback()
			return redirect(url_for('home_page'))
		else:
			msg="Invalid Email ID"
			return render_template('ngo_npo.html', msg=msg)

#REGISTER
@app.route('/register')
def register():
	return render_template('register.html')

#after registering
@app.route('/registered',methods = ['POST', 'GET'])
def registered():
	if request.method == 'POST':
		name=request.form['name']
		e_mail=request.form['email']
		city=request.form['city']

		if(check(e_mail)):
			con = sqlite3.connect("landing_page.sqlite3")
			cur = con.cursor()
			try:
				cur.execute("INSERT into registered (name, email, city) values (?,?,?)",(name, e_mail, city))
				con.commit()
			except:
				con.rollback()
			return redirect(url_for('home_page'))
		else:
			msg="Invalid Email ID"
			return render_template('register.html', msg=msg)

if __name__ == '__main__':
	app.run(debug=True)