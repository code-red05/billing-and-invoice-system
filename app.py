from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_
import flask_excel
import pyexcel
import pyexcel_xlsx

app = Flask(__name__)
flask_excel.init_excel(app)
app.secret_key = "key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///wai_ngo.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#app.permanent_session_lifetime = timedelta(minutes = 10)

db = SQLAlchemy(app, session_options={"expire_on_commit": False})

#class admins(db.Model):
#	_id = db.Column("id", db.Integer, primary_key = True)
#	name = db.Column("name", db.String(100))
#	password = db.Column("password", db.String(100))
#	question = db.Column("question", db.String(500))
#	answer = db.Column("answer", db.String(500))
#
#	def __init__(self, name, password, question, answer):
#		self.name = name
#		self.password = password
#		self.question = question
#		self.answer = answer

class users(db.Model):
	_id = db.Column("id", db.Integer, primary_key = True)
	name = db.Column("name", db.String(100))
	password = db.Column("password", db.String(100))
	question = db.Column("question", db.String(500))
	answer = db.Column("answer", db.String(500))
	admin = db.Column("admin", db.String(3))

	def __init__(self, name, password, question, answer, admin):
		self.name = name
		self.password = password
		self.question = question
		self.answer = answer
		self.admin = admin

class reciept(db.Model):
	_id = db.Column("RecieptNo", db.Integer, primary_key = True)
	issued_name = db.Column("IssuedBy", db.String(100))
	date = db.Column("Date", db.String(10))
	don_name = db.Column("DonorName", db.String(100))
	onbehalf = db.Column("OnBehalfOf", db.String(500))
	company = db.Column("CompanyName", db.String(400))
	address = db.Column("Address", db.String(300))
	mobile_no = db.Column("MobileNo", db.String(15))
	landline_no = db.Column("LandlineNo", db.String(20))
	email_id = db.Column("EmailID", db.String(100))
	don_purp = db.Column("DonationPurpose", db.String(100), nullable = False)
	amt = db.Column("Amount", db.Integer, nullable = False)
	amt_words = db.Column("AmtInWords", db.String(200), nullable = False)
	don_meth = db.Column("DonationMethod", db.String(100), nullable = False)
	ref_no = db.Column("PaymentRefNo", db.String(30))
	pay_date = db.Column("PaymentDate", db.String(10))
	bank = db.Column("BankName", db.String(100))
	cancelled = db.Column("Cancelled", db.String(1))
	cancelled_by = db.Column(db.String(100))
	comments = db.Column("Comments", db.String(200))

	def __init__(self, issued_name, date, don_name, onbehalf, company, address, mobile_no, landline_no, email_id, don_purp, amt, amt_words, don_meth, ref_no, pay_date, bank):
		self.issued_name = issued_name
		self.date = date
		self.don_name = don_name
		self.onbehalf = onbehalf
		self.company = company
		self.address = address
		self.mobile_no = mobile_no
		self.landline_no = landline_no
		self.email_id = email_id
		self.don_purp = don_purp
		self.amt = amt
		self.amt_words = amt_words
		self.don_meth = don_meth
		self.ref_no = ref_no
		self.pay_date = pay_date
		self.bank = bank
		self.cancelled = "N"
		self.cancelled_by = ""
		self.comments = ""

class reciept_2(db.Model):
	_id = db.Column("RecieptNo", db.Integer, primary_key = True)
	issued_name = db.Column("IssuedBy", db.String(100))
	date = db.Column("Date", db.String(10))
	don_name = db.Column("DonorName", db.String(100))
	onbehalf = db.Column("OnBehalfOf", db.String(500))
	company = db.Column("CompanyName", db.String(400))
	address = db.Column("Address", db.String(300))
	mobile_no = db.Column("MobileNo", db.String(15))
	landline_no = db.Column("LandlineNo", db.String(20))
	email_id = db.Column("EmailID", db.String(100))
	item_1 = db.Column(db.String(500))
	weight_1 = db.Column(db.String(100))
	price_1 = db.Column(db.Integer)
	item_2 = db.Column(db.String(500))
	weight_2 = db.Column(db.String(100))
	price_2 = db.Column(db.Integer)
	item_3 = db.Column(db.String(500))
	weight_3 = db.Column(db.String(100))
	price_3 = db.Column(db.Integer)
	item_4 = db.Column(db.String(500))
	weight_4 = db.Column(db.String(100))
	price_4 = db.Column(db.Integer)
	item_5 = db.Column(db.String(500))
	weight_5 = db.Column(db.String(100))
	price_5 = db.Column(db.Integer)
	cancelled = db.Column("Cancelled", db.String(1))
	cancelled_by = db.Column(db.String(100))
	comments = db.Column("Comments", db.String(200))

	def __init__(self, issued_name, date, don_name, onbehalf, company, address, mobile_no, landline_no, email_id, item_1, weight_1, price_1, item_2, weight_2, price_2, item_3, weight_3, price_3, item_4, weight_4, price_4, item_5, weight_5, price_5):
		self.issued_name = issued_name
		self.date = date
		self.don_name = don_name
		self.onbehalf = onbehalf
		self.company = company
		self.address = address
		self.mobile_no = mobile_no
		self.landline_no = landline_no
		self.email_id = email_id
		self.item_1 = item_1
		self.weight_1 = weight_1
		self.price_1 = price_1
		self.item_2 = item_2
		self.weight_2 = weight_2
		self.price_2 = price_2
		self.item_3 = item_3
		self.weight_3 = weight_3
		self.price_3 = price_3
		self.item_4 = item_4
		self.weight_4 = weight_4
		self.price_4 = price_4
		self.item_5 = item_5
		self.weight_5 = weight_5
		self.price_5 = price_5
		self.cancelled = "N"
		self.cancelled_by = ""
		self.comments = ""

class festive_dates(db.Model):
	_id = db.Column("id", db.Integer, primary_key = True)
	from_date = db.Column(db.String(50))
	to_date = db.Column(db.String(50))

@app.route('/')
def home():
    return redirect(url_for("login"))

@app.route('/view')
def view():
	return render_template("view.html", values = users.query.all())

@app.route('/login', methods = ["POST", "GET"])
def login():
	if request.method == "POST":
		#session.permanent = False
		user = request.form["nm"]
		password = request.form["pwd"]
		found_user = users.query.filter_by(name = user).all()
		if found_user:
			for i in found_user:
				if i.password == password:
					session["user"] = user
					session["admin"] = i.admin
					session["print_reciept_type"] = "0"
					session["report_type"] = "0"
					flash("Login Successful!")
					return redirect(url_for("new_reciept"))	
			flash("Incorrect Password! Please try again")
			return redirect(url_for("login"))
		else:
			flash("Username does not exist! Please try again")
			return redirect(url_for("login"))
	else:
		if "user" in session:
			flash("Already logged in!")
			return redirect(url_for("new_reciept"))
		else:
			return render_template("login.html")

#@app.route('/admin_login', methods = ["POST", "GET"])
#def admin_login():
#	if request.method == "POST":
#		session.permanent = True
#		user = request.form["nm"]
#		password = request.form["pwd"]
#		found_user = admins.query.filter_by(name = user).all()
#		if found_user:
#			for i in found_user:
#				if i.password == password:
#					session["user"] = user
#					session["password"] = password
#					session["admin"] = "Yes"
#					flash("Login Successful!")
#					return redirect(url_for("new_reciept"))	
#			flash("Incorrect Password! Please try again")
#			return redirect(url_for("admin_login"))
#		else:
#			flash("Username does not exist! Please try again")
#			return redirect(url_for("admin_login"))
#	else:
#		if "user" in session:
#			flash("Already logged in!")
#			return redirect(url_for("new_reciept"))
#		else:
#			return render_template("admin_login.html")



@app.route('/register', methods =["POST", "GET"])
def register():
	if session["admin"] == "Yes":	
		if request.method == "POST":
			#session.permanent = True
			user = request.form["name"]
			password1 = request.form["pwd1"]
			password2 = request.form["pwd2"]
			question = request.form["question"]
			answer = request.form["answer"]
			usr_type = request.form["usr_type"]
			found_user = None
			if password1 == password2:
				found_user = users.query.filter_by(name = user).filter_by(password = password1).first()
				if found_user:
					flash("User already exists!")
					return redirect(url_for("register"))
				else:
					usr = None
					if usr_type == "admin":
						usr = users(user,password1,question,answer,"Yes")
					else:
						usr = users(user,password1,question,answer,"No")
					db.session.add(usr)
					db.session.commit()
					flash("New Login Id successfully created!")
					return render_template("register.html", name = session["user"]) 
					
			else:
				flash("Passwords do not match! Please try again.")
				return render_template("register.html", name = session["user"]) 
		else:
			return render_template("register.html", name = session["user"]) 
	else:
		flash("You do not have admin rights!")
		return render_template("reciept.html", name = session["user"])

forgot_user = None
@app.route('/forgot_pwd', methods = ["POST", "GET"])
def forgot():
	global forgot_user
	if request.method == "POST":
		fname = request.form["fname"]
		if fname == "1":
			uname = request.form["uname"]
			forgot_user = db.session.query(users).filter_by(name = uname).first()
			if forgot_user:
				return render_template("forgot.html", form = 2, question = forgot_user.question)
			else:
				flash("Username does not exist!")
				return render_template("forgot.html", form = 1)
		elif fname == "2":
			answer = request.form["ans"]
			if forgot_user.answer == answer:
				return render_template("forgot.html", form = 3)
			else:
				flash("Incorrect Answer!")
				return render_template("forgot.html", form = 2, question = forgot_user.question)
		elif fname == "3":
			pwd1 = request.form["pwd1"]
			pwd2 = request.form["pwd2"]
			if pwd1 == pwd2:
				forgot_user.password = pwd1
				db.session.add(forgot_user)
				db.session.commit()
				flash("Password Successfully Changed!")
				return redirect(url_for('login'))
			else:
				flash("Passwords Do Not Match! Try Again")
				return render_template("forgot.html", form = 3)
	else:
		forgot_user = None
		return render_template("forgot.html", form = 1)


#@app.route('/user', methods = ["POST", "GET"])
#def user():
#	email = None
#	if "user" in  session:
#		user = session["user"]
#
#		if request.method == "POST":
#			email = request.form["email"]
#			session["email"] = email
#
#			found_user = users.query.filter_by(name = user).filter_by(password = session["password"]).first()
#			found_user.email = email
#			db.session.commit()
#
#			flash("Email was saved!")
#		else:
#			if "email" in session:
#				email = session["email"]
#		
#		return render_template("user.html", user = user)
#	else:
#		flash("You are not logged in!")
#		return redirect(url_for("login"))

temp_reciept = None
@app.route('/reciept', methods = ["POST", "GET"])
def new_reciept():
	global temp_reciept
	date = None
	onbehalf = ""
	company = ""
	address = None
	country = ""
	mobile_no = None
	std = None
	landline_no = None
	email_id = None
	don_purp = None
	amt = None
	amt_words = None
	don_meth = None
	ref_no = None
	pay_date = None
	bank = None

	don_name = ""
	othernames = None
	full_mobile = None
	full_landline = None

	otherdon = None
	othermeth = None

	if "user" in session:
		user = session["user"]
		#session["item1"] = session["item2"] = session["item3"] = session["item4"] = session["item5"] = ""

		if request.method == "POST":
			#session["date"] = 
			date = request.form["date"]
			indicomp = request.form["indicomp"]
			if indicomp == "individual":

				#session["don_name"] = 
				don_name = request.form["name"]
				#session["company"] = ""

				if request.form.get("behalfcheck"):
					#session["onbehalf"] = 
					onbehalf = request.form["onbehalf"]
				#else:
					#session["onbehalf"] = ""

			else:
				#session["company"] = 
				company = request.form["company"]
				#session["don_name"] = session["onbehalf"] = ""
			address = request.form["address"]
			country = request.form["country"]
			mobile_no = request.form["mobile_no"]
			std = request.form["std"]
			landline_no = request.form["landline_no"]
			email_id = request.form["email"]
			#session["don_purp"] = 
			don_purp = request.form["donation_purp"]
			#session["amt"] = 
			amt = request.form["amt"]
			session["amt_words"] = amt_words = request.form["amt_words"]
			#session["don_meth"] = 
			don_meth = request.form["donation_meth"]

			if not don_meth=="रोख":
				#session["ref_no"] = 
				ref_no = request.form["payno"]
				#session["paydate"] = 
				pay_date = request.form["paydate"]
				#session["bank"] = 
				bank = request.form["bank"]
			else:
				#session["ref_no"] = 
				ref_no = ""
				#session["paydate"] = 
				pay_date = ""
				#session["bank"] = 
				bank = ""

			if (country and mobile_no):
				full_mobile = country + mobile_no
			else:
				full_mobile = ""

			if (std and landline_no):
				full_landline = std + landline_no
			else:
				full_landline = ""
			
			if don_purp == "Other":
				otherdon = request.form["otherdon"]
				#session["don_purp"] = 
				don_purp = "Other: " + otherdon

			if don_meth == "Other":
				othermeth = request.form["otherpay"]
				#session["don_meth"] = 
				don_meth = "Other: " + othermeth

			temp_reciept = reciept(user,date,don_name,onbehalf,company,address,full_mobile,full_landline,email_id,don_purp,amt,amt_words,don_meth,ref_no,pay_date,bank)
			
			db.session.add(temp_reciept)
			db.session.commit()
			session["print_reciept_type"] = "1"
			#session['billno'] = temp_reciept._id
			
			return redirect(url_for("new_reciept"))

		else:
			return render_template("reciept.html",admin = session["admin"], name = user)
	else:
		flash("You are not logged in!")
		return redirect(url_for("login"))

@app.route('/print_reciept')
def print_reciept():
	global temp_reciept
	fest_date = festive_dates.query.first()
	if "user" in session:
		if not temp_reciept == None:
			if session["print_reciept_type"] == "1":
				return render_template("print_reciept.html", reciept_type = session["print_reciept_type"], date = temp_reciept.date, billno = temp_reciept._id, don_name = temp_reciept.don_name, onbehalf = temp_reciept.onbehalf, company = temp_reciept.company, don_purp = temp_reciept.don_purp, amt = temp_reciept.amt, don_meth = temp_reciept.don_meth, ref_no = temp_reciept.ref_no, pay_date = temp_reciept.pay_date, bank = temp_reciept.bank, item1 = ["","",""], item2 = ["","",""], item3 = ["","",""], item4 = ["","",""], item5 = ["","",""], user = session["user"], from_date = fest_date.from_date, to_date = fest_date.to_date, amt_words = session["amt_words"])

			elif session["print_reciept_type"] == "2":
				return render_template("print_reciept.html", reciept_type = session["print_reciept_type"], date = temp_reciept.date, billno = temp_reciept._id, don_name = temp_reciept.don_name, onbehalf = temp_reciept.onbehalf, company = temp_reciept.company, don_purp = "", amt = "", don_meth = "", ref_no = "", pay_date = "", bank = "", item1 = [temp_reciept.item_1,temp_reciept.weight_1,temp_reciept.price_1], item2 = [temp_reciept.item_2,temp_reciept.weight_2,temp_reciept.price_2], item3 = [temp_reciept.item_3,temp_reciept.weight_3,temp_reciept.price_3], item4 = [temp_reciept.item_4,temp_reciept.weight_4,temp_reciept.price_4], item5 = [temp_reciept.item_5,temp_reciept.weight_5,temp_reciept.price_5], user = session["user"], from_date = fest_date.from_date, to_date = fest_date.to_date, amt_words = "")
			else:
				return redirect(url_for("new_reciept"))
		else:
			flash("Generate a reciept before printing!")
			return redirect(url_for("new_reciept"))
	else:
		flash("You are not logged in!")
		return redirect(url_for("login"))

@app.route('/temp')
def temp():
	if "user" in session:
		return render_template("temp.html");
	else:
		flash("You are not logged in!")
		return redirect(url_for("login"))

@app.route('/reciept2', methods = ["POST", "GET"])
def new_reciept2():
	global temp_reciept
	date = None
	don_name = ""
	onbehalf = ""
	company = ""
	address = ""
	country = ""
	mobile_no = None
	std = None
	landline_no = None
	email_id = None
	item1 = ["","",0]
	item2 = ["","",0]
	item3 = ["","",0]
	item4 = ["","",0]
	item5 = ["","",0]

	if "user" in session:
		user = session["user"]
		session["don_purp"] = session["don_meth"] = session["amt"] = session["amt_words"] = session["ref_no"] = session["paydate"] = session["bank"] = ""

		if request.method == "POST":
			
			session["date"] = date = request.form["date"]
			indicomp = request.form["indicomp"]
			if indicomp == "individual":

				session["don_name"] = don_name = request.form["name"]
				session["company"] = ""

				if request.form.get("behalfcheck"):
					session["onbehalf"] = onbehalf = request.form["onbehalf"]
				else:
					session["onbehalf"] = onbehalf = ""

			else:
				session["company"] = company = request.form["company"]
				session["don_name"] = session["onbehalf"] = ""
			address = request.form["address"]
			country = request.form["country"]
			mobile_no = request.form["mobile_no"]
			std = request.form["std"]
			landline_no = request.form["landline_no"]
			email_id = request.form["email"]

			if (country and mobile_no):
				full_mobile = country + mobile_no
			else:
				full_mobile = ""

			if (std and landline_no):
				full_landline = std + landline_no
			else:
				full_landline = ""

			item1[0] = request.form["item1"]
			if item1[0] == "ईतर":
				item1[0] = request.form["other1"] 
			item1[1] = request.form["weight1"]
			item1[2] = request.form["price1"]
			if item1[2] == "":
				item1[2] = 0
			session["item1"] = item1

			item2[0] = request.form["item2"]
			if item2[0] == "ईतर":
				item2[0] = request.form["other2"]
			item2[1] = request.form["weight2"]
			item2[2] = request.form["price2"]
			if item2[2] == "":
				item2[2] = 0
			session["item2"] = item2

			item3[0] = request.form["item3"]
			if item3[0] == "ईतर":
				item3[0] = request.form["other3"]
			item3[1] = request.form["weight3"]
			item3[2] = request.form["price3"]
			if item3[2] == "":
				item3[2] = 0
			session["item3"] = item3
			
			item4[0] = request.form["item4"]
			if item4[0] == "ईतर":
				item4[0] = request.form["other4"]
			item4[1] = request.form["weight4"]
			item4[2] = request.form["price4"]
			if item4[2] == "":
				item4[2] = 0
			session["item4"] = item4
			
			item5[0] = request.form["item5"]
			if item5[0] == "ईतर":
				item5[0] = request.form["other5"]
			item5[1] = request.form["weight5"]
			item5[2] = request.form["price5"]
			if item5[2] == "":
				item5[2] = 0
			session["item5"] = item5

			temp_reciept = reciept_2(user,date,don_name,onbehalf,company,address,full_mobile,full_landline,email_id,item1[0],item1[1],item1[2],item2[0],item2[1],item2[2],item3[0],item3[1],item3[2],item4[0],item4[1],item4[2],item5[0],item5[1],item5[2])
			db.session.add(temp_reciept)
			db.session.commit()
			session["print_reciept_type"] = "2"
			#session["billno"] = temp_reciept._id
			#session["total"] = item1[3] + item2[3] + item3[3]

			return redirect(url_for("new_reciept2"))

		else:
			return render_template("reciept2.html", admin = session["admin"], name = user)
	else:
		flash("You are not logged in!")
		return redirect(url_for("login"))

@app.route('/cancel_reciept')
def cancel_reciept():
	if "user" in session:
		if session["admin"] == "Yes":
			#if request.method == "POST":
			#	
			#	comments = request.form["comments"]
			#	
			#	if find_reciept:
			#		find_reciept.cancelled = "Y"
			#		find_reciept.cancelled_by = session["user"]
			#		find_reciept.comments = comments
			#		db.session.commit()
			#		flash("successfully Cancelled!")
			#		return render_template("cancel_reciept.html")
			#	else:
			#		flash("Reciept Not Found! Try Again")
			#		return render_template("cancel_reciept.html")
			#else:
			return render_template("cancel_reciept.html", found = "No", name = session["user"])
		else:
			flash("You do not have admin rights!")
			return redirect(url_for("new_reciept"))
	else:
		flash("You are not logged in!")
		return redirect(url_for("login"))

@app.route('/find_reciept', methods = ["POST", "GET"])
def find_reciept():
	
	if request.method == "POST":
		reciept_type = request.form["reciept_type"]
		reciept_no = request.form["reciept_no"]
		if reciept_type == "1":
			find = reciept.query.filter_by(cancelled = "N").filter_by(_id = reciept_no).first()
			if find:
				return render_template("cancel_reciept.html", type = reciept_type, name = session["user"], found = "Yes", reciept_type = "1", date = find.date, reciept_no = reciept_no, don_name= find.don_name, company = find.company, onbehalf = find.onbehalf, address= find.address, mobile_no = find.mobile_no, landline_no = find.landline_no, email_id = find.email_id, don_purp = find.don_purp, amt = find.amt, amt_words = find.amt_words, don_meth = find.don_meth, ref_no = find.ref_no, pay_date = find.pay_date, bank = find.bank)
			else:
				flash("Reciept Not Found!")
				return render_template("cancel_reciept.html", reciept_type = reciept_type, reciept_no = reciept_no, name = session["user"], found = "No")
		elif reciept_type == "2":
			find = reciept_2.query.filter_by(cancelled = "N").filter_by(_id = reciept_no).first()
			if find:
				item1 = [find.item_1,find.weight_1,find.price_1]
				item2 = [find.item_2,find.weight_2,find.price_2]
				item3 = [find.item_3,find.weight_3,find.price_3]
				item4 = [find.item_4,find.weight_4,find.price_4]
				item5 = [find.item_5,find.weight_5,find.price_5]
				return render_template("cancel_reciept.html", type = reciept_type, name = session["user"], found = "Yes", reciept_type = "2", date = find.date, reciept_no = reciept_no, don_name= find.don_name, company = find.company, onbehalf = find.onbehalf, address= find.address, mobile_no = find.mobile_no, landline_no = find.landline_no, email_id = find.email_id, item1 = item1, item2 = item2, item3 = item3, item4 = item4, item5 = item5)
			else:
				flash("Reciept Not Found!")
				return render_template("cancel_reciept.html", reciept_type = reciept_type, reciept_no = reciept_no, name = session["user"], found = "No")
		else:
			flash("Reciept type does not exist!")
			return redirect(url_for("cancel_reciept"))
		
	else:
		return redirect(url_for("cancel_reciept"))

@app.route('/cancel', methods = ["POST", "GET"])
def cancel():
	
	if request.method == "POST":
		reciept_type = request.form["type"]
		reciept_no = request.form["recino"]
		temp = reciept.query.first()
		if reciept_type == "1":
			temp = reciept.query.filter_by(cancelled = "N").filter_by(_id = reciept_no).first()
		else:
			temp = reciept_2.query.filter_by(cancelled = "N").filter_by(_id = reciept_no).first()
		temp.cancelled = "Y"
		comments = request.form["comments"]
		temp.cancelled_by = session["user"]
		temp.comments = comments
		db.session.commit()
		flash("Cancelled successfully")
		return redirect(url_for("cancel_reciept"))
	else:
		return redirect(url_for("cancel_reciept"))

@app.route('/date_change', methods = ["POST", "GET"])
def date_change():
	if "user" in session:
		date = festive_dates.query.first()
		if request.method == "POST":
		 	start = request.form["start_date"]
		 	end = request.form["end_date"]
		 	
		 	date.from_date = start
		 	date.to_date = end

		 	db.session.commit()
		 	flash("Dates Updated successfully!")
		 	return redirect(url_for("date_change"))

		else:
			return render_template("festive_date.html",admin = session["admin"], name = session["user"], start = date.from_date, end = date.to_date)
	else:
		flash("You are not logged in!")
		return redirect(url_for("login"))

Query = None
@app.route('/report', methods = ["POST", "GET"])
def report():
	global Query
	column_names = []
	user_list = users.query.all()
	meth_list = ["रोख","चेक","डी डी","आर टी जी एस","एन ई एफ टी","आय एम पी एस","मनी ऑर्डर"]
	if "user" in session:
		if request.method == "POST":
			if request.form["formname"] == "find":
				if request.form["type"] == "1":
					main = request.form["filter"]
					amount = None
					issued_name = meth = None
					Query = db.session.query(reciept._id.label('Reciept_No'), reciept.issued_name.label('Issued_By'), reciept.date.label('Date'), reciept.don_name.label('Donor_Name'), reciept.company.label('Company'), reciept.onbehalf.label('On_Behalf_Of'), reciept.don_purp.label('Donation_Purpose'), reciept.don_meth.label('Donation_Method'), reciept.amt.label('Amount'), reciept.cancelled.label('cancelled'), reciept.cancelled_by.label('Cancelled_by'), reciept.comments.label('Comments'))

					date1 = request.form["date1"]
					date2 = request.form["date2"]
					if date1 == "" and date2 == "":
						Query = Query
					elif date2 == "":
						Query = Query.filter_by(date = date1)
					else:
						Query = Query.filter(reciept.date.between(date1, date2))

					if main == "amt":
						amount = request.form["amt"]
						if amount == "":
							amount = 0
						else:
							amount = int(amount)
						Query = Query.filter_by(cancelled = "N").filter(amount <= reciept.amt).all()
					elif main == "all":
						Query = Query.filter_by(cancelled = "N").all()
					elif main == "user":
						issued_name = request.form["spec_user"]
						Query = Query.filter_by(cancelled = "N").filter_by(issued_name = issued_name).all()
					elif main == "don_meth":
						meth = request.form["donation_meth"]
						Query = Query.filter_by(cancelled = "N").filter_by(don_meth = meth).all()
					elif main == "cancelled":
						Query = Query.filter_by(cancelled = "Y").all()


					total = 0
					kayam = 0
					dendgi = 0
					mahaprasad = 0
					jahirat = 0
					malvikri = 0
					for x in Query:
						total += x.Amount
						if x.Donation_Purpose == "जाहिरात":
							jahirat += x.Amount
						elif x.Donation_Purpose == "कायमनिधी":
							kayam += x.Amount
						elif x.Donation_Purpose == "देणगी":
							dendgi += x.Amount
						elif x.Donation_Purpose == "महाप्रसाद":
							mahaprasad += x.Amount
						elif x.Donation_Purpose == "माल विक्री":
							malvikri += x.Amount

					session["report_type"] = "1"
					
					return render_template("report.html", admin = session["admin"], name = session["user"], type = "1", main = main, amt = amount, spec = issued_name, meth = meth, date1 = date1, date2 = date2, user_list = user_list, pay_list = meth_list, rec = Query, total = total, kayam = kayam, dendgi = dendgi, mahaprasad = mahaprasad, jahirat = jahirat, malvikri = malvikri)

				elif request.form["type"] == "2":
					main = request.form["filter"]
					amount = None
					issued_name = None
					Query = db.session.query(reciept_2._id.label('Reciept_No'), reciept_2.issued_name.label('Issued_By'), reciept_2.date.label('Date'), reciept_2.don_name.label('Donor_Name'), reciept_2.company.label('Company'), reciept_2.onbehalf.label('On_Behalf_Of'), reciept_2.item_1.label('Item_1'), reciept_2.weight_1.label('Quantity_1'), reciept_2.price_1.label('Price_1'), reciept_2.item_2.label('Item_2'), reciept_2.weight_2.label('Quantity_2'), reciept_2.price_2.label('Price_2'), reciept_2.item_3.label('Item_3'), reciept_2.weight_3.label('Quantity_3'), reciept_2.price_3.label('Price_3'), reciept_2.item_4.label('Item_4'), reciept_2.weight_4.label('Quantity_4'), reciept_2.price_4.label('Price_4'), reciept_2.item_5.label('Item_5'), reciept_2.weight_5.label('Quantity_5'), reciept_2.price_5.label('Price_5'), reciept_2.cancelled.label('cancelled'), reciept_2.cancelled_by.label('Cancelled_by'), reciept_2.comments.label('Comments'))
					date1 = request.form["date1"]
					date2 = request.form["date2"]

					if date1 == "" and date2 == "":
						Query = Query
					elif date2 == "":
						Query = Query.filter_by(date = date1)
					else:
						Query = Query.filter(reciept_2.date.between(date1, date2))

					if main == "amt":
						amount = request.form["amt"]
						if amount == "":
							amount = 0
						else:
							amount = int(amount)
						Query = Query.filter_by(cancelled = "N").filter((reciept_2.price_1 + reciept_2.price_2 + reciept_2.price_3 + reciept_2.price_4 + reciept_2.price_5) >= amount).all()
						#Query = Query.filter_by(cancelled = "N").filter(or_((amount <= reciept_2.price_1), (amount <= reciept_2.price_2), (amount <= reciept_2.price_3), (amount <= reciept_2.price_4), (amount <= reciept_2.price_5))).all()
					elif main == "all":
						Query = Query.filter_by(cancelled = "N").all()
					elif main == "user":
						issued_name = request.form["spec_user"]
						Query = Query.filter_by(cancelled = "N").filter_by(issued_name = issued_name).all()
					elif main == "cancelled":
						Query = Query.filter_by(cancelled = "Y").all()

					saree1 = saree2 = saree3 = saree4 = 0
					for x in Query:
						q = []
						if not x.Item_1 == "":
							q.append(int(x.Quantity_1))
						else:
							q.append(0)

						if not x.Item_2 == "":
							q.append(int(x.Quantity_2))
						else:
							q.append(0)

						if not x.Item_3 == "":
							q.append(int(x.Quantity_3))
						else:
							q.append(0)

						if not x.Item_4 == "":
							q.append(int(x.Quantity_4))
						else:
							q.append(0)

						if not x.Item_5 == "":
							q.append(int(x.Quantity_5))
						else:
							q.append(0)

						if x.Item_1 == "६ वारी साडी":
							saree1 += q[0]
						elif x.Item_1 == "९ वारी साडी":
							saree2 += q[0]
						elif x.Item_1 == "पैठणी":
							saree3 += q[0]
						elif x.Item_1 == "शालू":
							saree4 += q[0]

						if x.Item_2 == "६ वारी साडी":
							saree1 += q[1]
						elif x.Item_2 == "९ वारी साडी":
							saree2 += q[1]
						elif x.Item_2 == "पैठणी":
							saree3 += q[1]
						elif x.Item_2 == "शालू":
							saree4 += q[1]

						if x.Item_3 == "६ वारी साडी":
							saree1 += q[2]
						elif x.Item_3 == "९ वारी साडी":
							saree2 += q[2]
						elif x.Item_3 == "पैठणी":
							saree3 += q[2]
						elif x.Item_3 == "शालू":
							saree4 += q[2]

						if x.Item_4 == "६ वारी साडी":
							saree1 += q[3]
						elif x.Item_4 == "९ वारी साडी":
							saree2 += q[3]
						elif x.Item_4 == "पैठणी":
							saree3 += q[3]
						elif x.Item_4 == "शालू":
							saree4 += q[3]

						if x.Item_5 == "६ वारी साडी":
							saree1 += q[4]
						elif x.Item_5 == "९ वारी साडी":
							saree2 += q[4]
						elif x.Item_5 == "पैठणी":
							saree3 += q[4]
						elif x.Item_5 == "शालू":
							saree4 += q[4]

					session["report_type"] = "2"

					return render_template("report.html", admin = session["admin"], name = session["user"], type = "2", main = main, amt = amount, spec = issued_name, date1 = date1, date2 = date2, user_list = user_list, rec = Query, saree1 = saree1, saree2 = saree2, saree3 = saree3, saree4 = saree4)

			elif request.form["formname"] == "download":
				if not Query == None:

					if request.form["rectype"] == "1":
					
						if Query[0].cancelled == "N":
							column_names = ['Reciept_No','Issued_By','Date','Donor_Name','Company','On_Behalf_Of','Donation_Purpose','Donation_Method','Amount']
						else:
							column_names = ['Reciept_No','Issued_By','Date','Donor_Name','Company','Donation_Purpose','Amount','Cancelled_by','Comments']
						return flask_excel.make_response_from_query_sets(Query, column_names, "xlsx", file_name = "report")
					
					elif request.form["rectype"] == "2":

						if Query[0].cancelled == "N":
							column_names = ['Reciept_No','Issued_By','Date','Donor_Name','Company','On_Behalf_Of','Item_1','Quantity_1','Price_1','Item_2','Quantity_2','Price_2','Item_3','Quantity_3','Price_3','Item_4','Quantity_4','Price_4','Item_5','Quantity_5','Price_5']
						else:
							column_names = ['Reciept_No','Issued_By','Date','Donor_Name','Company','Item_1','Quantity_1','Price_1','Item_2','Quantity_2','Price_2','Item_3','Quantity_3','Price_3','Item_4','Quantity_4','Price_4','Item_5','Quantity_5','Price_5','Cancelled_by','Comments']
						return flask_excel.make_response_from_query_sets(Query, column_names, "xlsx", file_name = "report")

					else:
						return redirect(url_for("report"))

				else:
					return redirect(url_for("report"))

			#elif request.form["formname"] == "print":
			#	if not Query == None:
			#		rectype = request.form["rectype"]
			#		if rectype == "1":
			#			return redirect(url_for("print_report",type = rectype))
			#		elif rectype == "2":
			#	else:
			else:
				return redirect(url_for("report"))

		else:
			#Query = None
			#session["report_type"] = "0"
			return render_template("report.html", admin = session["admin"], name = session["user"], type="1", user_list = user_list, pay_list = meth_list, rec = None)
	else:
		flash("You are not logged in!")
		return redirect(url_for("login"))


@app.route('/print_report')
def print_report():
	#rectype = request.args.get('type', None)
	if "user" in session:
		if (not Query == None) and (not session["report_type"] == 0):
			return render_template("print_report.html", type = session["report_type"], rec = Query)
		else:
			flash("Please generate report before printing")
			return redirect(url_for("report"))
	else:
		flash("You are not logged in!")
		return redirect(url_for("login"))


@app.route('/logout')
def logout():
	flash("You have been logged out!", "info")
	#session.pop("user", None)
	#session.pop("email", None)
	session.clear()
	return redirect(url_for("login"))



if __name__ == '__main__':
	db.create_all()
	app.run(debug = True)