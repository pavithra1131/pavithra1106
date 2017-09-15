from flask import *
app=Flask(__name__)

@app.route("/")
def root():
	return render_template("loginonline.html")
	
@app.route("/login")
def login():
	return render_template("loginonline.html")
	
@app.route("/register")
def register():
	return render_template("register.html")
	
if __name__=='__main__':
	app.run()

