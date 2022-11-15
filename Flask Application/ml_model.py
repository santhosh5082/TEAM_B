import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.multioutput import MultiOutputClassifier
import warnings
import pickle

warnings.filterwarnings("ignore")

dataset=pd.read_csv("C:\\Users\\user\\OneDrive\\Documents\\TCS_TEAM_ACTIVITY\\Flask Application\\data.csv")
x=dataset[['Rpm','Vibration','Temperature','Pressure']]
y=dataset[['Condition','Reason']]
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=0)
rf=MultiOutputClassifier(RandomForestClassifier ())
rf.fit(x_train,y_train)
pickle.dump(rf,open('model.pkl','wb'))

'''model=pickle.load(open('model.pkl','rb'))
print(model.predict([[6000,500,82,29]]))'''