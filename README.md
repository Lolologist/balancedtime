# balanced-time
Days should be 12 hours, and nights should be 12 hours. With this module you can know what time it is under this obviously-superior method of timekeeping.

#Using balanced-time:
convert_time_to_balanced_time(time=None, zipcode=10010, pretty_print=False)
time can be a datetime or will default to right now, zip is a US ZIP code (though due to interactions with astral's module, some will not work like in Alaska),
pretty_print is what gives you a string that looks nice, otherwise you get an equivalent datetime

clock_conversion accepts zipcode as above, and spits out an hour-by-hour breakdown of your day.
