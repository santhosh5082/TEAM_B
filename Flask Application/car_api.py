import numpy as np
from flask import Flask, request,render_template
import pickle

#Initialize the flask App
app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

#default page of our web-app
@app.route('/')
def home():
    return render_template('activity.html')

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

    return render_template('activity.html', prediction_text='Condition of tyre is {} , Reason: {}'.format(l[0],l[1]))

if __name__ == "__main__":
    app.run(debug=True)
