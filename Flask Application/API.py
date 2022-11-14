import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from flask import Flask, request, render_template
from Fetch_Code import fetch_data         #function we used in fetching code


#Initialize the flask App
app = Flask(__name__)
# app.config["TEMPLATES_AUTO_RELOAD"] = True


#default page of our web-app
@app.route('/')
def home():
    return render_template('index.html')# Name of HTML we are taking


#To use the predict button in our web-app
@app.route('/senddate', methods=['GET', 'POST'])
def senddate(): #function name that is used in HTML
    '''
    For rendering results on HTML GUI
    '''
    start_date = request.form['startdate']
    end_date = request.form['enddate']
    
    result = fetch_data(start_date,end_date)

    return render_template('index.html', result=result) #our HTML Page and need to do modifications if required

if __name__ == "__main__":
    app.run(debug=True)