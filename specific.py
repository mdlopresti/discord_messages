import datetime
import os
from pytz import timezone
from main import main

def message():
    if 'NEXT_DATE' in os.environ:
        print('NEXT_DATE is ' + os.environ['NEXT_DATE'])
        if 'NEXT_TIME' in os.environ:
            print('NEXT_TIME is ' + os.environ['NEXT_TIME'])
            #parsing date from enviroment variable
            next_date_list = os.environ['NEXT_DATE'].split()
            next_date = datetime.datetime.strptime(next_date_list[0] + ' ' + next_date_list[1] + ' ' + next_date_list[2], '%Y %m %d').date()
            
            # calculating the days until the next session
            days_until_session = (next_date - datetime.datetime.now(tz=timezone('US/Eastern')).date()).days
            print(str(days_until_session) + " days until the next session")

            #building message for alert
            if days_until_session == 7:
                os.environ['MESSAGE'] = 'One week until the next session!'
            elif days_until_session == 0:
                os.environ['MESSAGE'] = 'Session today at ' + os.environ['NEXT_TIME']
            else: 
                os.environ['MESSAGE'] = str(days_until_session) + ' days until the next session, which will be on ' + next_date.strftime('%A %B %d, %Y') + ' at ' + os.environ['NEXT_TIME']

            print('MESSAGE will be "' + os.environ['MESSAGE'] + '"')
            #calling main function from other python script
            main()

        else:
            print('NEXT_TIME is a mandatory environment variable and is not set')
    else:
        print('NEXT_DATE is a mandatory environment variable and is not set')

message()
