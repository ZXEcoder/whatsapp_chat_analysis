from datetime import datetime
import re
import pandas as pd
def preprocess(data):
    d = r'(\d{1,2}/\d{1,2}/\d{2}),\s(\d{1,2}:\d{2})\s(AM|PM|am|pm)?\s-\s(.+)'
    mess=re.findall(d, data)[1:]
   
    parsed_data=[]
    for entry in mess:
        dt, ti, apm, missg = entry
        date_time_str=f"{dt} {ti} {apm}"
        date_time_obj=datetime.strptime(date_time_str,"%d/%m/%y %I:%M %p")

        if ': ' in missg:
            phone,text=missg.split(': ',1)

        else:
            phone, text= None,missg

        parsed_entry={
            'date_time':date_time_obj,
            'phone':phone,
            'message':text,
            
            }
        parsed_data.append(parsed_entry)
    datte=[]
    Phon=[]
    Mesage=[]
    for entry in parsed_data:
        datte.append(entry['date_time'])
        Phon.append(entry['phone'])
        Mesage.append(entry['message'])   
    df1=pd.DataFrame({'DATE/TIME':datte,'user':Phon,'message':Mesage})
    df1['year']=df1['DATE/TIME'].dt.year
    df1['month']=df1['DATE/TIME'].dt.month_name()
    df1['day']=df1['DATE/TIME'].dt.day
    df1['hour']=df1['DATE/TIME'].dt.hour
    df1['minute']=df1['DATE/TIME'].dt.minute

    df1['only_date'] = df1['DATE/TIME'].dt.date
    
    df1['month_num'] = df1['DATE/TIME'].dt.month
   
    df1['day_name'] = df1['DATE/TIME'].dt.day_name()


    period = []
    for hour in df1[['day_name', 'hour']]['hour']:
        if hour == 23:
            period.append(str(hour) + "-" + str('00'))
        elif hour == 0:
            period.append(str('00') + "-" + str(hour + 1))
        else:
            period.append(str(hour) + "-" + str(hour + 1))

    df1['period'] = period
   
    return df1