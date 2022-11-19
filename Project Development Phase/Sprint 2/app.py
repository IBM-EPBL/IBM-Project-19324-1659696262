from flask import Flask,render_template,request,redirect, session, flash, url_for
import database

db = database.Database()

app = Flask(__name__)
app.secret_key = "a very secret  key"

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/register",methods = ['GET',"POST"])
def register():
    
    if request.method == 'POST':

        fname = request.form['fname']
        lname = request.form['lname']
        email = request.form['email_id']
        pwd = request.form['password']
        cpwd = request.form['confirm_pwd']

        if pwd != cpwd:    
            return render_template('register.html',usr_error = "Password does not match!")

        else:
            
            result = db.view(email)
            
            if result:
                return render_template('register.html',usr_error = "Email Id already Exists!")
            user_id = db.length_view() + 1
            db.insert(user_id,fname,lname,email,pwd)
            return redirect(url_for("login"))
    else:
        return render_template('register.html')

@app.route("/login",methods = ['GET',"POST"])
def login():
    if request.method == 'POST':

        email = request.form['email_id']
        pwd = request.form['password']
        result = db.lg_view(email)

        if not result:
            return render_template('login.html',usr_error = "Email id does'nt exists!")
            
        if pwd != result[1]:
            return render_template('login.html',usr_error = "Password doesn't match")
        else:
            session['loggedin'] = True
            session['username'] = email
            return redirect(url_for("dashboard"))
    else:
        return render_template('login.html')

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/wallet",methods = ['GET',"POST"])
def wallet():
    
    email = session['username']
    if request.method == 'POST':
        
        user_id = db.uid_view(email)   
        expense_name = request.form['exp_name']
        amount = request.form['exp_amt']
        date = request.form['exp_date']

        db.wallet_insert(user_id,amount,expense_name,date)
        return render_template('Wallet.html')
    else:
        return render_template('Wallet.html')

@app.route("/logout")
def logout():
    session.pop('loggedin', None)
    session.pop('username', None)
    flash("You have successfully logged out, please log in again!")
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.debug = True
    app.run()
