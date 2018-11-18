.. balanced-time documentation master file, created by
   sphinx-quickstart on Fri Nov 16 18:55:43 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

balancedtime
=========================================
|pypi_ver|

.. |pypi_ver| image:: https://img.shields.io/pypi/v/balancedtime.svg
    :target: https://pypi.org/project/balancedtime/

Using balancedtime
-------------------
balancedtime has two methods, one to get the current or specified time in a given location, and one to output a handy clock conversion for today in a given location.

convert_time_to_balanced_time(time=None, zipcode=10010, pretty_print=False)
the 'time' argument can be a datetime.datetime object.
'zipcode' can be a contiguous US ZIP code

pretty_print will output a datetime.datetime object if False, and a text representation of the time (in a 12 hour format with AM/PM) if True.

.. note::

   zipcode currently excludes leading 0 ZIPs (mostly in the Northeast.) and all ZIP codes not part of the contiguous United States. This is expected to be fixed in subsequent releases.


Examples
========

The following examples demonstrate the functionality available in the module

convert_time_to_balanced_time
-----------------------------

::

    >>> import balancedtime
    >>> balanced_time.convert_time_to_balanced_time(time=datetime.datetime(2018,5,3,6,30),zipcode=10010,pretty_print=True) #time in NYC on May 3, 2018, at 6:30 AM
    '06:32:06 AM'
    >>> balanced_time.convert_time_to_balanced_time(time=datetime.datetime(2018,5,3,6,30),zipcode=10010,pretty_print=False) #same, but return a datetime.datetime object
    datetime.datetime(2018, 5, 3, 6, 32, 6, 185567)
    
    


clock_conversion
----------------

::

    >>> clock_conversion(zipcode=10010)
    
    balanced calendar for New York, NY, 2018/11/18
      old   :  balanced
    12:00 AM = 12:15:50 AM
    1:00 AM  = 01:06:44 AM
    2:00 AM  = 01:57:38 AM
    3:00 AM  = 02:48:32 AM
    4:00 AM  = 03:39:26 AM
    5:00 AM  = 04:30:20 AM
    6:00 AM  = 05:21:14 AM
    7:00 AM  = 06:17:27 AM
    8:00 AM  = 07:30:36 AM
    9:00 AM  = 08:43:46 AM
    10:00 AM = 09:56:55 AM
    11:00 AM = 11:10:04 AM
    12:00 PM = 12:23:14 PM
    1:00 PM  = 01:36:23 PM
    2:00 PM  = 02:49:32 PM
    3:00 PM  = 04:02:42 PM
    4:00 PM  = 05:15:51 PM
    5:00 PM  = 06:20:08 PM
    6:00 PM  = 07:10:55 PM
    7:00 PM  = 08:01:42 PM
    8:00 PM  = 08:52:29 PM
    9:00 PM  = 09:43:17 PM
    10:00 PM = 10:34:04 PM
    11:00 PM = 11:24:51 PM

Installation
------------

Install balanced_time by running:

    pip install balancedtime


Contribute
----------

- Issue Tracker: https://github.com/Lolologist/balancedtime/issues
- Source Code: https://github.com/Lolologist/balancedtime

Version History
===============

======== =======================================================================
Version  Description
======== =======================================================================
0.1b     First release
======== =======================================================================

