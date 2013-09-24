#!/usr/bin/env python

"""
Constants for the PyOWM library:

  * OWM web API and PyOWM library versions
  * OWM web API endpoints
  * Keywords for weather status filtering
  
"""

# Version numbers
PYOWM_VERSION = '0.1'
OWM_API_VERSION = '2.5'

# OpenWeatherMap API URLs
ROOT_API_URL = 'http://api.openweathermap.org/data/2.5'
ICONS_BASE_URL = 'http://openweathermap.org/img/w'
OBSERVATION_URL = ROOT_API_URL+'/weather'
FIND_OBSERVATIONS_URL = ROOT_API_URL+'/find'
THREE_HOURS_FORECAST_URL = ROOT_API_URL+'/forecast'
DAILY_FORECAST_URL = ROOT_API_URL+'/forecast/daily'

# Weather status keywords
RAIN_KEYWORDS = ['rain','drizzle']
SUN_KEYWORDS = ['clear']
CLOUDS_KEYWORDS = ['clouds']
FOG_KEYWORDS =['fog','haze','mist']
SNOW_KEYWORDS =['snow','sleet']