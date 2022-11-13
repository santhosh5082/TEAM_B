from flask import Flask, request, render_template
from Fetch_Code import fetch_data         #function we used in fetching code


#Initialize the flask App
app = Flask(__name__)


#default page of our web-app
@app.route('/')
def home():
    return render_template('index222.html')# Name of HTML we are taking


#To use the predict button in our web-app
@app.route('/senddate/', methods=['POST'])
def senddate(): #function name that is used in HTML
    '''
    For rendering results on HTML GUI
    '''
    a = [str(i) for i in request.form.values()] #date as string values
    fetch_data(a[0],a[1]) #Taking as parameters for our function x
    return render_template('index.html') #our HTML Page and need to do modifications if required


if __name__ == "__main__":
    app.run(debug=True)