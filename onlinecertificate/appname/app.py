from flask import *
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:kgisl@localhost/onlineaccrediation'
app.config['SECRET_KEY'] = "random string"


db = SQLAlchemy(app)

	
@app.route("/login")
def login():
	return render_template("loginonline.html")
	
@app.route("/register")
def register():
	return render_template("register.html")
	
class register(db.Model):
	id=db.Column('student_id',db.Integer,primary_key=True)
	first_name=db.Column(db.String)
	last_name=db.Column(db.String)
	display_name=db.Column(db.String)
	email_address=db.Column(db.String)
	password=db.Column(db.String)
	confirm_password=db.Column(db.String)
	
	
	def __init__(self,first_name,last_name,display_name,email_address,password,confirm_password):
		self.first_name=first_name
		self.last_name=last_name
		self.display_name=display_name
		self.email_address=email_address
		self.password=password
		self.confirm_password=confirm_password

	@app.route("/register_db",methods=["GET","POST"])
	def register_db():
		if request.method == 'POST':
			if not request.form['first_name'] or not request.form['last_name'] or not request.form['display_name'] or not request.form['email_address'] or not request.form['password'] or not request.form['confirm_password']:
				flash("Error")
			else:
				student=register(request.form['first_name'],request.form['last_name'],request.form['display_name'],request.form['email_address'],request.form['password'],request.form['confirm_password'])
				db.session.add(student)
				db.session.commit()
			return redirect(url_for('register'))
		return render_template("register.html")
	
if __name__=='__main__':
	db.create_all()
	app.run(debug = True)

