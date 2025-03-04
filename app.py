from flask import Flask,request,render_template,redirect,url_for,jsonify
import pickle

app=Flask(__name__)

with open("linear_model.pkl",'rb') as file:
    model=pickle.load(file)

@app.route("/",methods=["GET","POST"])
def home():
    if(request.method=="POST"):
        return redirect(url_for("welcome")) 
    return render_template("home.html")

@app.route("/index",methods=["GET"])
def welcome():
    return render_template("index.html")

@app.route("/predict",methods=["post"])
def predict():
    try:  
        age=int(request.form['age'])
        sex=request.form['sex']
        bmi=float(request.form['bmi'])
        children=int(request.form['children'])
        smoker=request.form['smoker']
        region=request.form['region']

        sex=0 if sex.lower()=='male' else 0
        smoker=0 if smoker.lower()=='yes' else 1
        region_map={'southeast':0,'southwest':1,'northeast':2,'northwest':3}
        region=region_map[region]

        res=[[age,sex,bmi,children,smoker,region]]
        prediction=model.predict(res)[0]

        return jsonify({"prediction":prediction})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__=='__main__':
    app.run(debug=True)

