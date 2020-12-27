from flask import Flask, render_template, request
import requests
import pickle
import numpy as np

app = Flask(__name__,template_folder='Templates',static_folder='Static')
model = pickle.load(open('rf_clf_trained_model.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')

@app.route("/", methods=['POST'])
def predict():
    inputs = []
    if request.method == 'POST':
     inputs.append(request.form['Gender'])
     inputs.append(request.form['Married'])
     inputs.append(request.form['Education'])
     inputs.append(request.form['Employee'])
     inputs.append(request.form['Area'])
    
     if inputs[0]=='Male':
         g=1
     elif inputs[0]=='Female':
         g=0
     if inputs[1]=='Yes':
         mr=1
     elif inputs[1]=='No':
         mr=0
     if inputs[2]=='Graduate':
         edu=0
     elif inputs[2]=='Not-Graduate':
         edu=1
     if inputs[3]=='Yes':
         emp=1
     elif inputs[3]=='No':
         emp=0
     if inputs[4]=='Rural':
         area=0
     elif inputs[4]=='Semi-Urban':
         area=1
     elif inputs[4]=='Urban':
         area=2
     
    final_inputs = [np.array((g,mr,edu,emp,area))]
    prediction = model.predict(final_inputs)
    if(prediction[0] == 1):
            return render_template('index.html', predicted_result="Approved")
    if(prediction[0] == 0):
        return render_template('index.html', predicted_result="Not Approved")
    else:
        return render_template('index.html')
    

if __name__=="__main__":
    app.run(debug=True)

