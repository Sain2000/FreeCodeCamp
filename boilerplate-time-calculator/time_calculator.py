def add_time(start, duration, day=None):
    #tuple for the days of the week
    week=("sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday")

    #spliting the strings into hour minutes and am/pm
    
    
    temp=start.split()
    s_hour=int(temp[0].split(":")[0])
    s_minutes=int(temp[0].split(":")[1])
    s_daytime=temp[1]
    
    d_hour=int(duration.split(":")[0])
    d_minutes=int(duration.split(":")[1])

    #transform to 24hs

    if(s_daytime=="PM"):
      s_hour+=12
    
    #calculate total hours and minutes

    t_hour=s_hour+d_hour
    t_minutes=s_minutes+d_minutes
    t_hour+=t_minutes//60
    t_minutes=t_minutes%60

    #hours into days

    t_days=t_hour//24
    t_hour=t_hour%24

    #from 24hs format to AM

    if(t_hour>=12):
        f_daytime=" PM"
        if (t_hour!=12):
            t_hour=t_hour-12
    else:
        if(t_hour==0):
            t_hour+=12
        f_daytime=" AM"
    #create the returning string
    f_hour=str(t_hour)
    if(t_minutes<10):
        f_minutes="0"+str(t_minutes)
    else:
        f_minutes=str(t_minutes)
    res=f_hour+":"+f_minutes+f_daytime
    if(day):
        res+=", "+week[(t_days+week.index(day.lower()))%7].capitalize()
    if(t_days>0):
        if(t_days==1):
            res+=" (next day)"
        else:
            res+=" "+"("+str(t_days)+" days later)"    
    return res
      