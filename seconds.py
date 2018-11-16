from astral import *
import datetime
import pytz
from pytz import timezone

def convert_time_to_balanced_time(time):
    now = datetime.datetime.utcnow()
    six_am = datetime.datetime(now.year, now.month, now.day, 6)
    six_pm = datetime.datetime(now.year, now.month, now.day, 18)
    
    a = Astral()
    geo = a.geocoder
    city = geo["San Francisco"]
    now = datetime.datetime.utcnow()
    beginning_of_today = datetime.datetime(now.year, now.month, now.day, 0)
    sun = city.sun(date=beginning_of_today, local=True)
    #timezone stuff
    pacific = timezone('America/Los_Angeles')
    try:
        time = pacific.localize(time)
    except: #might pass in something already localized
        pass
    
    todays_seconds = sun['sunset'] - sun['sunrise']
    balanced_seconds = datetime.timedelta(seconds=12*60*60)

    
    if time >= sun['sunrise'] and time <= sun['sunset']:
        seconds_from_time_to_sunrise = time - sun['sunrise']

        multiplier_how_much_shorter_today_is = balanced_seconds/todays_seconds

        seconds_to_add_to_six_am = seconds_from_time_to_sunrise.total_seconds()*multiplier_how_much_shorter_today_is
        modified_time = six_am + datetime.timedelta(seconds=(seconds_to_add_to_six_am))
    
    elif time < sun['sunrise']:
        seconds_from_time_to_sunrise = sun['sunrise'] - time
        
        multiplier_how_much_longer_tonight_is = (balanced_seconds/todays_seconds)
        

        seconds_to_subtract_from_six_am = seconds_from_time_to_sunrise.total_seconds()/(multiplier_how_much_longer_tonight_is)
        modified_time = six_am - datetime.timedelta(seconds=(seconds_to_subtract_from_six_am))
    
    elif time > sun['sunset']:
        seconds_from_time_to_sunset = time - sun['sunset']
        
        multiplier_how_much_longer_tonight_is = (balanced_seconds/todays_seconds)

        seconds_to_add_to_six_pm = seconds_from_time_to_sunset.total_seconds()/(multiplier_how_much_longer_tonight_is)
        modified_time = six_pm + datetime.timedelta(seconds=(seconds_to_add_to_six_pm))
    return modified_time


def main():
    a = Astral()
    geo = a.geocoder
    city = geo["San Francisco"]
    now = datetime.datetime.utcnow()
    beginning_of_today = datetime.datetime(now.year, now.month, now.day, 0)
    sun = city.sun(date=beginning_of_today, local=True)

    current_adjusted_time = convert_time_to_balanced_time(datetime.datetime.now())
    print("Given 12 hours of daylight and 12 hours of dark, the time is now:")
    print(current_adjusted_time.strftime("%I:%M:%S%p"))
    
if __name__ == "__main__":
    main()
