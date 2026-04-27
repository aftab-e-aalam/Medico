from flask import Flask,render_template,url_for,redirect,request,session,flash
import pandas as pd 
from models import User,db
from Email import Email


app=Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SECRET_KEY']="!@#!@#"

db.init_app(app)

with app.app_context():
    db.create_all()


#------------Routing---------------
@app.route("/")
def home():
    df=pd.read_csv("final_data.csv").nlargest(4,"Experience")
    topDoctors=df.to_dict(orient="records")
    
    topHospitals=pd.read_csv("data.csv").sort_values(by="Rating",ascending=False).head(4)
    topHospitals=topHospitals.to_dict(orient="records")
    
    
    
    return render_template("index.html",topDoctors=topDoctors,topHospitals=topHospitals)
    

@app.route("/hospitals")
def hospitals():
    df=pd.read_csv("data.csv")
    hospitals=df.to_dict(orient="records")
    return render_template("hospitals.html",hospitals=hospitals)


@app.route("/doctors")
def doctors():
    df =pd.read_csv("final_data.csv")
    doctors_data=df.to_dict(orient="records")
    
    return render_template("doctors.html",doctors=doctors_data)

@app.route("/treatment")
def treatment():
    return render_template("treatment.html")



@app.route("/register",methods=["GET","POST"])
def register():
    if request.method=='POST':
        name=request.form['name']
        email=request.form['email']
        password=request.form['password']
        
        user=User.query.filter_by(email=email).first()

        if user:
            message="Email already exist!"
            return render_template("register.html",message=message)
        
        user=User(name=name,email=email,password=password)
        db.session.add(user)
        db.session.commit()
        
        Email().sendemail(name=name,email=email)
        

        return redirect(url_for("login"))
    
    
    return render_template("register.html")

@app.route("/login",methods=["GET","POST"])
def login():
    if request.method=='POST':
        email=request.form["email"]
        password=request.form["password"]
        
        user=User.query.filter_by(email=email,password=password).first()
        
        if user:
            session["email"]=user.email
            return redirect(url_for("home"))
        else :
            message="Wrong credentials try again"
            return render_template("login.html",message=message)
        

    return render_template("login.html")




if __name__=="__main__":
    app.run(debug=True)