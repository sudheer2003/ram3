from flask import Flask,render_template,request
from args import *
import numpy as np
import pickle
with open('Model.pkl','rb')as mod:

    model=pickle.load(mod)
with open('Scaler.pkl','rb')as mod:
    scaler=pickle.load(mod)
app=Flask(__name__)
@app.route('/',methods=['GET','POST'])
def index():
    
    if request.method=='POST':
        bedrooms=request.form['bedrooms']
        bathrooms=request.form['bedrooms']
        sft=request.form['sft']
        location=request.form['location']
        status=request.form['status']
        property_type=request.form['property type']
        direction=request.form['direction']
        input_array=np.array([[bedrooms,bathrooms,sft,location,status,property_type,direction]])
        prediction=model.predict(scaler.transform(input_array))[0]
        return render_template('index.html',location_mapping=location_mapping, status_mapping=status_mapping,property_type_mapping=property_type_mapping,direction_mapping=direction_mapping,prediction=prediction)

        
    else:
       return render_template('index.html',location_mapping=location_mapping, status_mapping=status_mapping,property_type_mapping=property_type_mapping,direction_mapping=direction_mapping)

@app.route('/second')
def second():
    return 'I am in Secod page'
@app.route('/third')
def third():
    return 'I am i third page'
if __name__=='__main__':

    #app.run(use_reloader=True,debug=True)
    app.run()
