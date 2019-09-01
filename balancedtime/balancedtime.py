from uszipcode import SearchEngine
import astral
from datetime import datetime, timedelta
import pytz
from pytz import timezone
import uszipcode


def convert_time_to_balanced_time(time=None, zipcode=10010, pretty_print=False):
    #zipcodes to lat/long to astral's location
    search = SearchEngine(simple_zipcode=True) # set simple_zipcode=False to use rich info database
    zipcode_obj = search.by_zipcode(zipcode)
    #the below won't work outside the US, need to reconcile uszipcode's timezone with atral's timezone
    location = astral.Location(('name', 'region', zipcode_obj.lat, zipcode_obj.lng, "US/"+zipcode_obj.timezone, 0))
    if time is None:
        now = datetime.now()
    else:
        now = time
        
    timezone = pytz.timezone(location.timezone)
    time = timezone.localize(now)
    #print(time)
    
    beginning_of_today = datetime(time.year, time.month, time.day)
    sun = location.sun(date=beginning_of_today, local=True)
    #print(sun)
    #print()
    
    beginning_of_yesterday = datetime(time.year, time.month, time.day) - timedelta(days=1)
    sun_yesterday = location.sun(date=beginning_of_yesterday, local=True)
    
    beginning_of_tomorrow = datetime(time.year, time.month, time.day) + timedelta(days=1)
    sun_tomorrow = location.sun(date=beginning_of_tomorrow, local=True)

    six_am = datetime(time.year, time.month, time.day, 6)
    six_pm = datetime(time.year, time.month, time.day, 18)

    todays_seconds = sun['sunset'] - sun['sunrise']
    #print("todays seconds: "+str(todays_seconds.total_seconds())+" or "+str(todays_seconds)+" hours.")
    
    last_nights_seconds = sun['sunrise'] - sun_yesterday['sunset']
    #print("last night's seconds: "+str(last_nights_seconds.total_seconds())+" or "+str(last_nights_seconds)+" hours.")
    
    tonights_seconds = sun_tomorrow['sunrise'] - sun['sunset']
    #print("tonight's seconds: "+str(tonights_seconds.total_seconds())+" or "+str(tonights_seconds)+" hours.")
    
    seconds_from_time_to_next_sunrise = sun['sunrise'] - time #use sun, not sun_tomorrow, because pre-dawn is same day
    #print("seconds_from_time_to_sunrise"+str(seconds_from_time_to_next_sunrise.total_seconds()))
    seconds_from_sunrise_to_time = time - sun['sunrise'] #same-day
    #print("seconds_from_sunrise_to_time"+str(seconds_from_sunrise_to_time.total_seconds()))
    seconds_from_sunset_until_time = time - sun['sunset']  #same-day, at night after sunset
    #print("seconds_from_sunset_to_time"+str(seconds_from_sunset_until_time.total_seconds()))
    
    balanced_seconds = timedelta(seconds=12*60*60)
    
    multiplier_how_much_shorter_today_is = balanced_seconds / todays_seconds
    #print("today's shortness multiplier, each second moves at x"+str(multiplier_how_much_shorter_today_is))
    
    multiplier_how_much_longer_tonight_is = (balanced_seconds / tonights_seconds)
    #print("tonight's multiplier: , each second moves at x"+str(multiplier_how_much_longer_tonight_is))
    
    multiplier_how_much_longer_last_night_was = (balanced_seconds / last_nights_seconds)
    #print("last night's multiplier: , each second moves at x"+str(multiplier_how_much_longer_last_night_was))

    if time >= sun['sunrise'] and time <= sun['sunset']:
        seconds_to_add_to_six_am = seconds_from_sunrise_to_time.total_seconds()*multiplier_how_much_shorter_today_is
        #print("seconds to add to today's 6 AM: "+str(seconds_to_add_to_six_am)+", or "+str(seconds_to_add_to_six_am/60/60)+" hours.")
        modified_time = six_am + timedelta(seconds=(seconds_to_add_to_six_am))

    elif time < sun['sunrise']: 
        seconds_to_subtract_from_this_six_am = seconds_from_time_to_next_sunrise.total_seconds()*(multiplier_how_much_longer_last_night_was)
        #print("seconds to subtract from this 6 am: "+str(seconds_to_subtract_from_this_six_am)+", or "+str(seconds_to_subtract_from_this_six_am/60/60)+" hours.")
        modified_time = six_am - timedelta(seconds=(seconds_to_subtract_from_this_six_am))
        

    elif time > sun['sunset']:        
        seconds_to_add_to_tonights_six_pm = seconds_from_sunset_until_time.total_seconds()*multiplier_how_much_longer_tonight_is
        #print("seconds to add to tonight's 6 PM: "+str(seconds_to_add_to_tonights_six_pm)+", or "+str(seconds_to_add_to_tonights_six_pm/60/60)+" hours.")
        modified_time = six_pm + timedelta(seconds=(seconds_to_add_to_tonights_six_pm))
    if pretty_print == False:
        return modified_time 
    else:
        return modified_time.strftime("%I:%M:%S %p")
    
    
def clock_conversion(zipcode=10010):
    search = SearchEngine(simple_zipcode=True) # set simple_zipcode=False to use rich info database
    zipcode_obj = search.by_zipcode(zipcode)
    today = datetime.utcnow()
    print("balanced calendar for "+zipcode_obj.post_office_city+", "+today.strftime("%Y/%m/%d"))
    print("  old   :  balanced")
    hour = 0
    
    while hour <= 23:
        time_to_show = convert_time_to_balanced_time(time=datetime(today.year, today.month, today.day,hour,0,0), pretty_print=True, zipcode=zipcode)
        if hour == 0:
            print("12:00 AM = "+time_to_show)
        elif hour < 10:
            print(str(hour)+":00 AM  = "+time_to_show)
        elif hour < 12:
            print(str(hour)+":00 AM = "+time_to_show)
        elif hour == 12:
            print("12:00 PM = "+time_to_show)
        elif hour < 22:
            print(str(hour-12)+":00 PM  = "+time_to_show)
        else:
            print(str(hour-12)+":00 PM = "+time_to_show)
        hour +=1    


# Turn this module into a package.
__path__ = []  # required for PEP 302 and PEP 451
__package__ = __name__  # see PEP 366 @ReservedAssignment
if globals().get("__spec__") is not None:
    __spec__.submodule_search_locations = []  # PEP 451 @UndefinedVariable