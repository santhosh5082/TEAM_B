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

from datetime import datetime, timedelta
import pymongo
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize']=(65,100)


# << ------------- Method to initialise fetching data from DB ------------->>

def fetch_data(s,e):


    # << ------------- Database Initialization ------------->>

    # Mongo Client
    client = pymongo.MongoClient('mongodb://127.0.0.1:27017/')

    # DB
    db = client['TEAM-B']

    # Collection
    collection = db.Dataset

    # << ----------- Converting user input dates from string format to datetime format ----------->>
    
    start = s.split('-')  # start = [a, b, c]
    end = e.split('-')
    
    user_start_date = datetime(int(start[0]), int(start[1]),
                               int(start[2])).date()  # ---> using '.date()' coz, we only need date not 'time'.
    user_end_date = datetime(int(end[0]), int(end[1]), int(end[2])).date()

    # print('User -', user_start_date, user_end_date)

    # Actual Timestamp boundaries of data in DB
    db_start_date = datetime(2022, 3, 1).date()
    db_end_date = datetime(2022, 11, 16).date()

    # << --------------- Verifying every possible Conditions ------------------->>
    if (user_start_date == db_start_date) and (user_end_date == db_end_date):  # U.S = D.S and U.E. = D.E
        
        result = collection.find()
        df=pd.DataFrame(result)
        
        plt.subplot(4, 1, 1)
        plt.plot(df['DateTime'],df['Rpm'])
        plt.tick_params(rotation=90)
        plt.tight_layout(pad=12.0)
        plt.xlabel('Date Range', fontsize=50)
        plt.ylabel('Rpm Values', fontsize=50)
        plt.title('Rpm vs Time', fontsize=70)
        
        plt.subplot(4, 1, 2)
        plt.plot(df['DateTime'], df['Vibration'])
        plt.tick_params(rotation=90)
        plt.tight_layout(pad=12.0)
        plt.xlabel('Date Range', fontsize=50)
        plt.ylabel('Vibration Values', fontsize=50)
        plt.title('Vibration vs Time', fontsize=70)
        
        plt.subplot(4, 1, 3)
        plt.plot(df['DateTime'], df['Temperature'])
        plt.tick_params(rotation=90)
        plt.tight_layout(pad=12.0)
        plt.xlabel('Date Range', fontsize=50)
        plt.ylabel('Temperature Values', fontsize=50)
        plt.title('Temperature vs Time', fontsize=70)
        
        plt.subplot(4, 1, 4)
        plt.plot(df['DateTime'], df['Pressure'])
        plt.tick_params(rotation=90)
        plt.tight_layout(pad=12.0)
        plt.xlabel('Date Range', fontsize=50)
        plt.ylabel('Pressure Values', fontsize=50)
        plt.title('Pressure vs Time', fontsize=70)
        
        #save plot as png
        plt.savefig('C:/Users/user/OneDrive/Documents/TCS_TEAM_ACTIVITY/Flask Application/static/my_graph.png')
        
        plt.close()
        
        return 1
    
    elif (user_start_date == db_start_date) and (user_end_date > db_end_date):  # U.S = D.S and U.E. > D.E
        
        result = collection.find()
        df = pd.DataFrame(result)
        
        plt.subplot(4, 1, 1)
        plt.plot(df['DateTime'],df['Rpm'])
        plt.tick_params(rotation=90)
        plt.tight_layout(pad=12.0)
        plt.xlabel('Date Range', fontsize=50)
        plt.ylabel('Rpm Values', fontsize=50)
        plt.title('Rpm vs Time', fontsize=70)
        
        plt.subplot(4, 1, 2)
        plt.plot(df['DateTime'], df['Vibration'])
        plt.tick_params(rotation=90)
        plt.tight_layout(pad=12.0)
        plt.xlabel('Date Range', fontsize=50)
        plt.ylabel('Vibration Values', fontsize=50)
        plt.title('Vibration vs Time', fontsize=70)
        
        plt.subplot(4, 1, 3)
        plt.plot(df['DateTime'], df['Temperature'])
        plt.tick_params(rotation=90)
        plt.tight_layout(pad=12.0)
        plt.xlabel('Date Range', fontsize=50)
        plt.ylabel('Temperature Values', fontsize=50)
        plt.title('Temperature vs Time', fontsize=70)
        
        plt.subplot(4, 1, 4)
        plt.plot(df['DateTime'], df['Pressure'])
        plt.tick_params(rotation=90)
        plt.tight_layout(pad=12.0)
        plt.xlabel('Date Range', fontsize=50)
        plt.ylabel('Pressure Values', fontsize=50)
        plt.title('Pressure vs Time', fontsize=70)
        
        #save plot as png
        plt.savefig('C:/Users/user/OneDrive/Documents/TCS_TEAM_ACTIVITY/Flask Application/static/my_graph.png')
        
        plt.close()
        
        return 1

    
    elif (user_start_date < db_start_date) and (user_end_date == db_end_date):  # U.S < D.S and U.E. = D.E
        
        result = collection.find()
        df = pd.DataFrame(result)
        
        plt.subplot(4, 1, 1)
        plt.plot(df['DateTime'],df['Rpm'])
        plt.tick_params(rotation=90)
        plt.tight_layout(pad=12.0)
        plt.xlabel('Date Range', fontsize=50)
        plt.ylabel('Rpm Values', fontsize=50)
        plt.title('Rpm vs Time', fontsize=70)
        
        plt.subplot(4, 1, 2)
        plt.plot(df['DateTime'], df['Vibration'])
        plt.tick_params(rotation=90)
        plt.tight_layout(pad=12.0)
        plt.xlabel('Date Range', fontsize=50)
        plt.ylabel('Vibration Values', fontsize=50)
        plt.title('Vibration vs Time', fontsize=70)
        
        plt.subplot(4, 1, 3)
        plt.plot(df['DateTime'], df['Temperature'])
        plt.tick_params(rotation=90)
        plt.tight_layout(pad=12.0)
        plt.xlabel('Date Range', fontsize=50)
        plt.ylabel('Temperature Values', fontsize=50)
        plt.title('Temperature vs Time', fontsize=70)
        
        plt.subplot(4, 1, 4)
        plt.plot(df['DateTime'], df['Pressure'])
        plt.tick_params(rotation=90)
        plt.tight_layout(pad=12.0)
        plt.xlabel('Date Range', fontsize=50)
        plt.ylabel('Pressure Values', fontsize=50)
        plt.title('Pressure vs Time', fontsize=70)
        
        #save plot as png
        plt.savefig('C:/Users/user/OneDrive/Documents/TCS_TEAM_ACTIVITY/Flask Application/static/my_graph.png')
        
        plt.close()
        
        return 1

        
    elif user_start_date < db_start_date and user_end_date > db_end_date:  # U.S < D.S and U.E > D.E
        
        result = collection.find()
        df = pd.DataFrame(result)
        
        plt.subplot(4, 1, 1)
        plt.plot(df['DateTime'],df['Rpm'])
        plt.tick_params(rotation=90)
        plt.tight_layout(pad=12.0)
        plt.xlabel('Date Range', fontsize=50)
        plt.ylabel('Rpm Values', fontsize=50)
        plt.title('Rpm vs Time', fontsize=70)
        
        plt.subplot(4, 1, 2)
        plt.plot(df['DateTime'], df['Vibration'])
        plt.tick_params(rotation=90)
        plt.tight_layout(pad=12.0)
        plt.xlabel('Date Range', fontsize=50)
        plt.ylabel('Vibration Values', fontsize=50)
        plt.title('Vibration vs Time', fontsize=70)
        
        plt.subplot(4, 1, 3)
        plt.plot(df['DateTime'], df['Temperature'])
        plt.tick_params(rotation=90)
        plt.tight_layout(pad=12.0)
        plt.xlabel('Date Range', fontsize=50)
        plt.ylabel('Temperature Values', fontsize=50)
        plt.title('Temperature vs Time', fontsize=70)
        
        plt.subplot(4, 1, 4)
        plt.plot(df['DateTime'], df['Pressure'])
        plt.tick_params(rotation=90)
        plt.tight_layout(pad=12.0)
        plt.xlabel('Date Range', fontsize=50)
        plt.ylabel('Pressure Values', fontsize=50)
        plt.title('Pressure vs Time', fontsize=70)
        
        #save plot as png
        plt.savefig('C:/Users/user/OneDrive/Documents/TCS_TEAM_ACTIVITY/Flask Application/static/my_graph.png')
        
        plt.close()
        
        return 1

    
    elif (user_start_date == db_start_date and user_end_date == db_start_date) or (
            (user_start_date < db_start_date) and (user_end_date == db_start_date)):  # U.S = D.s and U.e = D.S
        
        result = collection.find({"DateTime": "2022-03-01 00:00:00"})
        
        df = pd.DataFrame(result)
        plt.plot(df['DateTime'], df['Rpm'])
        plt.tick_params(rotation=90)
        plt.tight_layout(pad=12.0)
        plt.xlabel('Date Range', fontsize=50)
        plt.ylabel('Rpm Values', fontsize=50)
        plt.title('Rpm generated for given date range', fontsize=70)
        
        plt.plot(df['DateTime'], df['Vibration'])
        plt.tick_params(rotation=90)
        plt.tight_layout(pad=12.0)
        plt.xlabel('Date Range', fontsize=50)
        plt.ylabel('Vibration Values', fontsize=50)
        plt.title('Vibration generated for given date range', fontsize=70)
        
        plt.plot(df['DateTime'], df['Temperature'])
        plt.tick_params(rotation=90)
        plt.tight_layout(pad=12.0)
        plt.xlabel('Date Range', fontsize=50)
        plt.ylabel('Temperature Values', fontsize=50)
        plt.title('Temperature vs Time', fontsize=70)
        
        plt.plot(df['DateTime'], df['Pressure'])
        plt.tick_params(rotation=90)
        plt.tight_layout(pad=12.0)
        plt.xlabel('Date Range', fontsize=50)
        plt.ylabel('Pressure Values', fontsize=50)
        plt.title('Pressure vs Time', fontsize=70)
        
        #save plot as png
        plt.savefig('C:/Users/user/OneDrive/Documents/TCS_TEAM_ACTIVITY/Flask Application/static/my_graph.png')
        
        plt.close()
        
        return 1
    
    elif (user_start_date == db_start_date) and (user_end_date < db_end_date):  # U.S = D.S and U.E. < D.E
        
        new_user_end_date = (user_end_date + (
            timedelta(days=1)))  # adding +1 to user_end_date to include last day rows in fetch.

        # print('new user end date is', new_user_end_date)
        result = collection.find({"DateTime": {"$gte": str(user_start_date), "$lt": str(new_user_end_date)}})
        df = pd.DataFrame(result)
        
        plt.subplot(4, 1, 1)
        plt.plot(df['DateTime'],df['Rpm'])
        plt.tick_params(rotation=90)
        plt.tight_layout(pad=12.0)
        plt.xlabel('Date Range', fontsize=50)
        plt.ylabel('Rpm Values', fontsize=50)
        plt.title('Rpm vs Time', fontsize=70)
        
        plt.subplot(4, 1, 2)
        plt.plot(df['DateTime'], df['Vibration'])
        plt.tick_params(rotation=90)
        plt.tight_layout(pad=12.0)
        plt.xlabel('Date Range', fontsize=50)
        plt.ylabel('Vibration Values', fontsize=50)
        plt.title('Vibration vs Time', fontsize=70)
        
        plt.subplot(4, 1, 3)
        plt.plot(df['DateTime'], df['Temperature'])
        plt.tick_params(rotation=90)
        plt.tight_layout(pad=12.0)
        plt.xlabel('Date Range', fontsize=50)
        plt.ylabel('Temperature Values', fontsize=50)
        plt.title('Temperature vs Time', fontsize=70)
        
        plt.subplot(4, 1, 4)
        plt.plot(df['DateTime'], df['Pressure'])
        plt.tick_params(rotation=90)
        plt.tight_layout(pad=12.0)
        plt.xlabel('Date Range', fontsize=50)
        plt.ylabel('Pressure Values', fontsize=50)
        plt.title('Pressure vs Time', fontsize=70)
        
        #save plot as png
        plt.savefig('C:/Users/user/OneDrive/Documents/TCS_TEAM_ACTIVITY/Flask Application/static/my_graph.png')
        
        plt.close()
        
        return 1

        
    elif (user_start_date > db_start_date) and (user_start_date < db_end_date) and (user_end_date < db_end_date):  # (U.S. > D.S) and (U.S < D.E) and (U.E < D.E)
        
        new_user_end_date = (user_end_date + timedelta(days=1))  # adding +1 to user_end_date to include last day rows in fetch.

        # print('new user end date is', new_user_end_date)
        result = collection.find({"DateTime": {"$gte": str(user_start_date), "$lt": str(new_user_end_date)}})
        df = pd.DataFrame(result)

        plt.subplot(4, 1, 1)
        plt.plot(df['DateTime'],df['Rpm'])
        plt.tick_params(rotation=90)
        plt.tight_layout(pad=12.0)
        plt.xlabel('Date Range', fontsize=50)
        plt.ylabel('Rpm Values', fontsize=50)
        plt.title('Rpm vs Time', fontsize=70)
        
        plt.subplot(4, 1, 2)
        plt.plot(df['DateTime'], df['Vibration'])
        plt.tick_params(rotation=90)
        plt.tight_layout(pad=12.0)
        plt.xlabel('Date Range', fontsize=50)
        plt.ylabel('Vibration Values', fontsize=50)
        plt.title('Vibration vs Time', fontsize=70)
        
        plt.subplot(4, 1, 3)
        plt.plot(df['DateTime'], df['Temperature'])
        plt.tick_params(rotation=90)
        plt.tight_layout(pad=12.0)
        plt.xlabel('Date Range', fontsize=50)
        plt.ylabel('Temperature Values', fontsize=50)
        plt.title('Temperature vs Time', fontsize=70)
        
        plt.subplot(4, 1, 4)
        plt.plot(df['DateTime'], df['Pressure'])
        plt.tick_params(rotation=90)
        plt.tight_layout(pad=12.0)
        plt.xlabel('Date Range', fontsize=50)
        plt.ylabel('Pressure Values', fontsize=50)
        plt.title('Pressure vs Time', fontsize=70)
        
        #save plot as png
        plt.savefig('C:/Users/user/OneDrive/Documents/TCS_TEAM_ACTIVITY/Flask Application/static/my_graph.png')
        
        plt.close()
        
        return 1

    
    elif ((user_start_date > db_start_date) and (user_start_date < db_end_date) and (user_end_date == db_end_date)) or (
            (user_start_date > db_start_date) and (user_start_date < db_end_date) and (
            user_end_date > db_end_date)):  # (U.S. > D.S) and (U.S < D.E) and (U.E = D.E)
        
        result = collection.find(
            {"DateTime": {"$gte": str(user_start_date), "$lt": str(datetime(2022, 11, 17).date())}})
        df = pd.DataFrame(result)
        
        plt.subplot(4, 1, 1)
        plt.plot(df['DateTime'],df['Rpm'])
        plt.tick_params(rotation=90)
        plt.tight_layout(pad=12.0)
        plt.xlabel('Date Range', fontsize=50)
        plt.ylabel('Rpm Values', fontsize=50)
        plt.title('Rpm vs Time', fontsize=70)
        
        plt.subplot(4, 1, 2)
        plt.plot(df['DateTime'], df['Vibration'])
        plt.tick_params(rotation=90)
        plt.tight_layout(pad=12.0)
        plt.xlabel('Date Range', fontsize=50)
        plt.ylabel('Vibration Values', fontsize=50)
        plt.title('Vibration vs Time', fontsize=70)
        
        plt.subplot(4, 1, 3)
        plt.plot(df['DateTime'], df['Temperature'])
        plt.tick_params(rotation=90)
        plt.tight_layout(pad=12.0)
        plt.xlabel('Date Range', fontsize=50)
        plt.ylabel('Temperature Values', fontsize=50)
        plt.title('Temperature vs Time', fontsize=70)
        
        plt.subplot(4, 1, 4)
        plt.plot(df['DateTime'], df['Pressure'])
        plt.tick_params(rotation=90)
        plt.tight_layout(pad=12.0)
        plt.xlabel('Date Range', fontsize=50)
        plt.ylabel('Pressure Values', fontsize=50)
        plt.title('Pressure vs Time', fontsize=70)
        
        #save plot as png
        plt.savefig('C:/Users/user/OneDrive/Documents/TCS_TEAM_ACTIVITY/Flask Application/static/my_graph.png')
        
        plt.close()
        
        return 1
    
    elif (user_start_date == db_end_date and user_end_date == db_end_date) or (
            (user_start_date == db_end_date) and (user_end_date > db_end_date)):  # U.S = D.E and U.E = D.E
        
        result = collection.find({"DateTime": {"$gte": str(db_end_date), "$lt": str(datetime(2022, 11, 17).date())}})
        df = pd.DataFrame(result)
        
        plt.subplot(4, 1, 1)
        plt.plot(df['DateTime'],df['Rpm'])
        plt.tick_params(rotation=90)
        plt.tight_layout(pad=12.0)
        plt.xlabel('Date Range', fontsize=50)
        plt.ylabel('Rpm Values', fontsize=50)
        plt.title('Rpm vs Time', fontsize=70)
        
        plt.subplot(4, 1, 2)
        plt.plot(df['DateTime'], df['Vibration'])
        plt.tick_params(rotation=90)
        plt.tight_layout(pad=12.0)
        plt.xlabel('Date Range', fontsize=50)
        plt.ylabel('Vibration Values', fontsize=50)
        plt.title('Vibration vs Time', fontsize=70)
        
        plt.subplot(4, 1, 3)
        plt.plot(df['DateTime'], df['Temperature'])
        plt.tick_params(rotation=90)
        plt.tight_layout(pad=12.0)
        plt.xlabel('Date Range', fontsize=50)
        plt.ylabel('Temperature Values', fontsize=50)
        plt.title('Temperature vs Time', fontsize=70)
        
        plt.subplot(4, 1, 4)
        plt.plot(df['DateTime'], df['Pressure'])
        plt.tick_params(rotation=90)
        plt.tight_layout(pad=12.0)
        plt.xlabel('Date Range', fontsize=50)
        plt.ylabel('Pressure Values', fontsize=50)
        plt.title('Pressure vs Time', fontsize=70)
        
        #save plot as png
        plt.savefig('C:/Users/user/OneDrive/Documents/TCS_TEAM_ACTIVITY/Flask Application/static/my_graph.png')
        
        plt.close()
        
        return 1

        
    elif (user_start_date < db_start_date) and (user_end_date > db_start_date) and (
            user_end_date < db_end_date):  # (U.S. < D.S) and (U.E > D.S) and (U.E < D.E)
        
        new_user_end_date = (
                    user_end_date + timedelta(days=1))  # adding +1 to user_end_date to include last day rows in fetch.

        # print('new user end date is', new_user_end_date)
        result = collection.find({"DateTime": {"$gte": str(db_start_date), "$lt": str(new_user_end_date)}})
        df = pd.DataFrame(result)
        
        plt.subplot(4, 1, 1)
        plt.plot(df['DateTime'],df['Rpm'])
        plt.tick_params(rotation=90)
        plt.tight_layout(pad=12.0)
        plt.xlabel('Date Range', fontsize=50)
        plt.ylabel('Rpm Values', fontsize=50)
        plt.title('Rpm vs Time', fontsize=70)
        
        plt.subplot(4, 1, 2)
        plt.plot(df['DateTime'], df['Vibration'])
        plt.tick_params(rotation=90)
        plt.tight_layout(pad=12.0)
        plt.xlabel('Date Range', fontsize=50)
        plt.ylabel('Vibration Values', fontsize=50)
        plt.title('Vibration vs Time', fontsize=70)
        
        plt.subplot(4, 1, 3)
        plt.plot(df['DateTime'], df['Temperature'])
        plt.tick_params(rotation=90)
        plt.tight_layout(pad=12.0)
        plt.xlabel('Date Range', fontsize=50)
        plt.ylabel('Temperature Values', fontsize=50)
        plt.title('Temperature vs Time', fontsize=70)
        
        plt.subplot(4, 1, 4)
        plt.plot(df['DateTime'], df['Pressure'])
        plt.tick_params(rotation=90)
        plt.tight_layout(pad=12.0)
        plt.xlabel('Date Range', fontsize=50)
        plt.ylabel('Pressure Values', fontsize=50)
        plt.title('Pressure vs Time', fontsize=50)
        
        #save plot as png
        plt.savefig('C:/Users/user/OneDrive/Documents/TCS_TEAM_ACTIVITY/Flask Application/static/my_graph.png')
        
        plt.close()
        
        return 1
    
    elif user_start_date > user_end_date :
        return 2

    else:
        return 0
    
# fetch_data('2022-03-01', '2022-11-16')

# # ------------------------- END ------------------------------- END ------------------------------- END ------------------------------ >>