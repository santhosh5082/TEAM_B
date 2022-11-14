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



# Modules required
from datetime import datetime, timedelta
import pymongo



# << ------------- Database Initialization ------------->>


# Mongo Client
client = pymongo.MongoClient('mongodb://127.0.0.1:27017/')

# DB
db = client['TEAM-B']

# Collection
collection = db.Dataset


# << ----------- Converting user input dates from string format to datetime format ----------->>


start = '2022-11-15'.split('-') # start = [a, b, c]
end = '2022-11-16'.split('-')

user_start_date = datetime(int(start[0]), int(start[1]), int(start[2])).date()   # ---> using '.date()' coz, we only need date not 'time'.
user_end_date = datetime(int(end[0]), int(end[1]), int(end[2])).date()

# print('User -', user_start_date, user_end_date)


# Actual Timestamp boundaries of data in DB
db_start_date = datetime(2022, 3, 1).date()
db_end_date = datetime(2022, 11, 16).date()


# << --------------- Verifying every possible Conditions ------------------->> 


if (user_start_date == db_start_date) and (user_end_date == db_end_date) : # U.S = D.S and U.E. = D.E 
    
    result = collection.find()
    
    count = 0
    for doc in result :
        count += 1
    print(count)
        
        
elif (user_start_date == db_start_date) and (user_end_date > db_end_date) : # U.S = D.S and U.E. > D.E
    
    result = collection.find()
    
    count = 0
    for doc in result :
        count += 1
    print(count)
        
        
elif (user_start_date < db_start_date) and (user_end_date == db_end_date) : # U.S < D.S and U.E. = D.E
    
    result = collection.find()
        
    count = 0
    for doc in result :
        # print(doc)
        count += 1
    print(count)
        
        
elif user_start_date < db_start_date and user_end_date > db_end_date :      # U.S < D.S and U.E > D.E
    
    result = collection.find()
    
    count = 0
    for doc in result :
        # print(doc)
        count += 1
    print(count)


elif (user_start_date == db_start_date and user_end_date == db_start_date) or ((user_start_date < db_start_date) and (user_end_date == db_start_date)) : # U.S = D.s and U.e = D.S
    
    result = collection.find({"DateTime" : "2022-03-01 00:00:00"})
    
    count = 0
    for doc in result :
        # print(doc)
        count += 1
    print(count)


elif (user_start_date == db_start_date) and (user_end_date < db_end_date) : # U.S = D.S and U.E. < D.E

    new_user_end_date = (user_end_date + (timedelta(days=1)))           # adding +1 to user_end_date to include last day rows in fetch.
    
    # print('new user end date is', new_user_end_date)
    
    result = collection.find({"DateTime" : {"$gte" : str(user_start_date), "$lt" : str(new_user_end_date)}})
    
    count = 0
    for doc in result :
        count += 1
    print(count)
    

elif (user_start_date > db_start_date) and (user_start_date < db_end_date) and (user_end_date < db_end_date): # (U.S. > D.S) and (U.S < D.E) and (U.E < D.E)
        
    new_user_end_date = (user_end_date + timedelta(days=1))                      # adding +1 to user_end_date to include last day rows in fetch.
        
    # print('new user end date is', new_user_end_date)
        
    result = collection.find({"DateTime" : {"$gte" : str(user_start_date), "$lt" : str(new_user_end_date)}})
    
    count = 0
    for doc in result :
        count += 1
    print(count)


elif ((user_start_date > db_start_date) and (user_start_date < db_end_date) and (user_end_date == db_end_date)) or ((user_start_date > db_start_date) and (user_start_date < db_end_date) and (user_end_date > db_end_date)) : # (U.S. > D.S) and (U.S < D.E) and (U.E = D.E)
        
    result = collection.find({"DateTime" : {"$gte" : str(user_start_date), "$lt" : str(datetime(2022, 11, 17).date())}})
    
    count = 0
    for doc in result :
        count += 1
    print(count)
        

elif (user_start_date == db_end_date and user_end_date == db_end_date) or ((user_start_date == db_end_date) and (user_end_date > db_end_date)) :   # U.S = D.E and U.E = D.E
    
    result = collection.find({"DateTime" : {"$gte" : str(db_end_date), "$lt" : str(datetime(2022, 11, 17).date())}})
    
    count = 0
    for doc in result :
        count += 1
    print(count)
        

elif (user_start_date < db_start_date) and (user_end_date > db_start_date) and (user_end_date < db_end_date): # (U.S. < D.S) and (U.E > D.S) and (U.E < D.E)
    
    new_user_end_date = (user_end_date + timedelta(days=1))                        # adding +1 to user_end_date to include last day rows in fetch.

    # print('new user end date is', new_user_end_date)
    
    result = collection.find({"DateTime" : {"$gte" : str(db_start_date), "$lt" : str(new_user_end_date)}})
    
    count = 0
    for doc in result :
        count += 1
    print(count)
        

else :
    
    print('OOPS, No data found!')


# # ------------------------- END ------------------------------- END ------------------------------- END ------------------------------ >>