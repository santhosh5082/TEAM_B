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



# <------------------/----------------------------------------------\---------------------->                
# <-------------------- DATA GENERATION AND DATABASE CONNECTIVITY-------------------------->
# <----------------/-------------------------------------------------\--------------------->



# Modules required
import pandas as pd
import random
import pymongo


# << ---------- Database Initialization --------->>


# client creation
client = pymongo.MongoClient('mongodb://127.0.0.1:27017/')

# database creation
db = client['TEAM-B']

# Collection creation
my_collection = db.Dataset

            
# << ---------- Storing DateTimes in Dictionary ------------- >>


# dict to store all dates
date_dict = {}

# creating datetimes 
all_dates = pd.date_range(start="2022/03/01",end='2022/11/16',periods=1000)   # remember!! No.of rows == periods

counter = 1 # -----> counter used as key while inserting

for d in all_dates :
    date_dict[str(counter)] = str(d)
    counter += 1


# << ---------- random sensor values generation ------------ >>


# no.of records
total_rows = 1000

for row_num in range(1, total_rows+1):
    
    # RPM range
    rand_rpm = (random.randint(20, 20000+1)) # units -> rpm
    
    # vibration range
    rand_vibration = (random.randint(1, 5000+1)) # units -> Hz
    
    # Temperature  range
    rand_temperature = (random.randint(-40, 120+1)) # units -> centigrade
    
    # Pressure range
    rand_pressure = (random.randint(14, 130+1)) # units -> psi
    
    # dict of params
    parameters = {'rpm': rand_rpm, 'vibration': rand_vibration, 'temperature': rand_temperature, 'pressure': rand_pressure}
    
    # output var
    reason = ""
    condition = ""
    good = 0
    r = v = t = p = 0
    
    # verifying temperature value with ideal range            
    if parameters['temperature'] < 7 :
        condition = "Bad"
        reason = "Low Temperature"
        rand_value = parameters['temperature']
        t = -1
                
    elif parameters['temperature'] > 90 :
        condition = "Bad"
        reason = "High Temperature"
        rand_value = parameters['temperature']
        t = 1
                
    else :
        if condition == "Bad" :
            pass
        else :
            condition = "Good"
        good += 1
    
    # verifying vibration value with ideal range            
    if parameters['vibration'] > 1000 :
        condition = "Bad"
        reason = "High vibration"
        rand_value = parameters['vibration']
        v = 1
                
    else :
        if condition == "Bad" :
            pass
        else :
            condition = "Good"
        good += 1
        
    # verifying rpm value with ideal range            
    if parameters['rpm'] < 5000 :
        condition = "Bad"
        reason = "Low rpm"
        rand_value = parameters['rpm']
        r = -1
                
    elif parameters['rpm'] > 10000 :
        condition = "Bad"
        reason = "High rpm"
        rand_value = parameters['rpm']
        r = 1
                
    else :
        if condition == "Bad" :
            pass
        else :
            condition = "Good"
        good += 1
        
    # verifying pressure value with ideal range            
    if parameters['pressure'] < 28 :
        condition = "Bad"
        reason = "Low pressure"
        rand_value = parameters['pressure']
        p = -1
                
    elif parameters['pressure'] > 35 :
        condition = "Bad"
        reason = "High pressure"
        rand_value = parameters['pressure']
        p = 1     
                
    else :
        if condition == "Bad" :
            pass
        else :
            condition = "Good"
        good += 1
    
    
    # combinational conditions
    if t+p == 2 or t+v == 2 or r+t == -2 :
        reason = "Tyre Bursting"
        
    if t+p == -2 :
        reason = "Tyre blowout"
    
    if r+t == 2 :
        reason = "RPM and Temperature are high"
        
    if r+v == 2 :
        reason = "Tyre wearout and Engine Failure"
        
    if v+p == 2 :
        reason = "High Pressure and High Vibration"
        
    if t+p+r+v == 4 :
        reason = "Your tyre is completely in bad condition"
    
    if r+t+p == -3 :
        reason = "Due to lower values, tyre is in bad condition"
                
    if good == 4 :
        reason = "All parameters are within optimal ranges"
    
                             
    # << ----------- DATABSE CONNECTIVITY ------------ >>
    

    # data format to insert
    data = {
        "Rpm" : parameters["rpm"],
        "Vibration" : parameters["vibration"],
        "Temperature" : parameters["temperature"],
        "Pressure" : parameters["pressure"],
        "Condition" : condition,
        "Reason" : reason,
        "DateTime" : date_dict[str(row_num)] 
    }
    
    # insert data
    my_collection.insert_one(data)


    # print('Value is {0} , Condition is {1} and Reason is {2}'.format(rand_value, condition, reason))
    print(parameters["rpm"], parameters["vibration"], parameters["temperature"], parameters["pressure"], condition, reason, date_dict[str(row_num)])
    print(row_num)


# << -------------------------- END --------------------------- END ---------------------------- END ------------------------------------------- >>