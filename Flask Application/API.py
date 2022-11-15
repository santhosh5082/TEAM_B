import matplotlib
matplotlib.use('Agg')
import numpy as np
from ml_model import *
from flask import Flask, request, render_template
from Fetch_Code import fetch_data                               #function we used in fetching code
import pickle


#Initialize the flask App
app = Flask(__name__)

# loading our ml model using pickel
model = pickle.load(open('model.pkl', 'rb'))


#default page of our web-app
@app.route('/')
def home1():
    result = 2
    return render_template('index.html', result=result)         # Name of HTML we are taking


#default page of our web-app
@app.route('/ML_prediction')
def home2():
    return render_template('ml.html')


#To use the predict button in our web-app
@app.route('/predict',methods=['POST','GET'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    l=[]
    l.append(prediction[0][0])
    l.append(prediction[0][1])

    #output = round(prediction[0], 2)

    return render_template('ml.html', prediction_text='Condition of tyre is {} , Reason: {}'.format(l[0],l[1]))


#To use the predict button in our web-app
@app.route('/senddate', methods=['GET', 'POST'])
def senddate():                                             #function name that is used in HTML
    '''
    For rendering results on HTML GUI
    '''
    start_date = request.form['startdate']
    end_date = request.form['enddate']
    
    result = fetch_data(start_date,end_date)

    return render_template('index.html', result=result) #our HTML Page and need to do modifications if required


if __name__ == "__main__":
    app.run(debug=True, threaded=True)
