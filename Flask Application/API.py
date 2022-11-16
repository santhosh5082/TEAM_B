#----------->>
#          -------------->>
#                       ---------->>
#                              --------->>
#                                  --------------->>
#  DON'T PLAY WITH THIS CODE !!!!!!!!!!! ------------->>>>>
#                                  --------------->>
#                              --------->>
#                       ---------->>
#         --------------->>
#----------->>


# << ------------------- Modules required -------------------->>
import matplotlib
matplotlib.use('Agg')
import numpy as np
from ml_model import *
from flask import Flask, request, render_template
from Fetch_Code import fetch_data                               #function we used in fetching code
import pickle


# << ------------------- Initialising the flask App -------------------->>
app = Flask(__name__)


# << ------------------- Graph Functionality Page - Start -------------------->>

# default page of our web-app
@app.route('/')
def home1():
    result = 3
    return render_template('index.html', result=result)         # Name of HTML we are taking


# Adding Functionality for 'Get-Data' button to recieve and send appropriate data
@app.route('/get-graph-data', methods=['GET', 'POST'])
def senddate():                                             #function name that is used in HTML
    '''
    For rendering results on HTML GUI
    '''
    start_date = request.form['startdate']
    end_date = request.form['enddate']
    
    result = fetch_data(start_date,end_date)

    return render_template('index.html', result=result)

# << ------------------- Graph Functionality Page - End -------------------->>



# << ------------------- ML Prediction Functionality Page - Start -------------------->>

# loading our ml model using pickel
model = pickle.load(open('model.pkl', 'rb'))


# Another default page of our ML prediction
@app.route('/ml')
def home2():
    flag = 0
    return render_template('ml.html', flag=flag)


# Adding Functionality for 'GET TYRE CONDITION' button to receive and send appropriate data
@app.route('/prediction',methods=['POST','GET'])
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
    condition = l[0]
    reason = l[1]
    
    flag = 1

    return render_template('ml.html', condition=condition, reason=reason, flag=flag)

# << ------------------- ML Prediction Functionality Page - Start -------------------->>


if __name__ == "__main__":
    app.run(debug=True, threaded=True)


# # ------------------------- END ------------------------------- END ------------------------------- END ------------------------------ >>