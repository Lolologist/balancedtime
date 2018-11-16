from uszipcode import SearchEngine
import astral
import datetime
import pytz
from pytz import timezone
import uszipcode

def convert_time_to_balanced_time(zipcode=10010, pretty_print=False):
    #zipcodes to lat/long to astral's location

    search = SearchEngine(simple_zipcode=True) # set simple_zipcode=False to use rich info database
    zipcode_obj = search.by_zipcode(zipcode)
    #the below won't work outside the US, need to reconcile uszipcode's timezone with atral's timezone
    location = astral.Location(('name', 'region', zipcode_obj.lat, zipcode_obj.lng, "US/"+zipcode_obj.timezone, 0))
    now = datetime.datetime.now()
    
    beginning_of_today = datetime.datetime(now.year, now.month, now.day, 0)
    sun = location.sun(date=beginning_of_today, local=True)

    six_am = datetime.datetime(now.year, now.month, now.day, 6)
    six_pm = datetime.datetime(now.year, now.month, now.day, 18)

    todays_seconds = sun['sunset'] - sun['sunrise']
    balanced_seconds = datetime.timedelta(seconds=12*60*60)

    timezone = pytz.timezone(location.timezone)
    time = timezone.localize(time)

    multiplier_how_much_shorter_today_is = balanced_seconds/todays_seconds
    multiplier_how_much_longer_tonight_is = (balanced_seconds/todays_seconds)

    if time >= sun['sunrise'] and time <= sun['sunset']:
        seconds_from_time_to_sunrise = time - sun['sunrise']

        seconds_to_add_to_six_am = seconds_from_time_to_sunrise.total_seconds()*multiplier_how_much_shorter_today_is
        modified_time = six_am + datetime.timedelta(seconds=(seconds_to_add_to_six_am))

    elif time < sun['sunrise']:
        seconds_from_time_to_sunrise = sun['sunrise'] - time

        seconds_to_subtract_from_six_am = seconds_from_time_to_sunrise.total_seconds()/(multiplier_how_much_longer_tonight_is)
        modified_time = six_am - datetime.timedelta(seconds=(seconds_to_subtract_from_six_am))

    elif time > sun['sunset']:
        seconds_from_time_to_sunset = time - sun['sunset']

        seconds_to_add_to_six_pm = seconds_from_time_to_sunset.total_seconds()/(multiplier_how_much_longer_tonight_is)
        modified_time = six_pm + datetime.timedelta(seconds=(seconds_to_add_to_six_pm))
    if pretty_print == False:
        return modified_time 
    else:
        return modified_time.strftime("%I:%M:%S%p")

