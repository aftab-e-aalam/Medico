from flask import Flask,render_template,url_for
import pandas as pd 



app=Flask(__name__)

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

@app.route("/login")
def login():
    return render_template("login.html")






if __name__=="__main__":
    app.run(debug=True)