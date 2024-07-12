#! C:\Users\emily\Documents\WeatherData\weather-data-extraction\myenv\Scripts\python.exe

# pip installing all the needed packages 
import openmeteo_requests
import requests_cache
import pandas as pd
from retry_requests import retry

# Setup the Open-Meteo API client with cache and retry on error
cache_session = requests_cache.CachedSession('.cache', expire_after = -1)
retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
openmeteo = openmeteo_requests.Client(session = retry_session)

#loading in the weather data
df = pd.read_csv('weatherdata2024.csv')
df.Latitude[0]
# i = 0
# for i in range(len(df)):
# 	# print(df.Latitude[i])
# 	# Make sure all required weather variables are listed here
# 	# The order of variables in hourly or daily is important to assign them correctly below
# 	url = "https://archive-api.open-meteo.com/v1/archive"
# 	params = {
# 		"latitude": df.Latitude[i], #looping through the lat and long
# 		"longitude": df.Longitude[i],
# 		"start_date": "2010-01-01",
# 		"end_date": "2010-01-01",
# 		"hourly": ["temperature_2m", "relative_humidity_2m", "dew_point_2m", "apparent_temperature", "precipitation", "rain", "snowfall", "snow_depth", "weather_code", "pressure_msl", "surface_pressure", "cloud_cover", "et0_fao_evapotranspiration", "vapour_pressure_deficit", "wind_speed_10m", "wind_direction_10m", "wind_gusts_10m"],
# 		"timezone": "GMT"
# 	}
# 	responses = openmeteo.weather_api(url, params=params)

# 	# Process first location. Add a for-loop for multiple locations or weather models
# 	response = responses[0]
# 	print(f"Coordinates {response.Latitude()}°N {response.Longitude()}°E")
# 	print(f"Elevation {response.Elevation()} m asl")
# 	print(f"Timezone {response.Timezone()} {response.TimezoneAbbreviation()}")
# 	print(f"Timezone difference to GMT+0 {response.UtcOffsetSeconds()} s")

# 	# Process hourly data. The order of variables needs to be the same as requested.
# 	hourly = response.Hourly()
# 	hourly_temperature_2m = hourly.Variables(0).ValuesAsNumpy()
# 	hourly_relative_humidity_2m = hourly.Variables(1).ValuesAsNumpy()
# 	hourly_dew_point_2m = hourly.Variables(2).ValuesAsNumpy()
# 	hourly_apparent_temperature = hourly.Variables(3).ValuesAsNumpy()
# 	hourly_precipitation = hourly.Variables(4).ValuesAsNumpy()
# 	hourly_rain = hourly.Variables(5).ValuesAsNumpy()
# 	hourly_snowfall = hourly.Variables(6).ValuesAsNumpy()
# 	hourly_snow_depth = hourly.Variables(7).ValuesAsNumpy()
# 	hourly_weather_code = hourly.Variables(8).ValuesAsNumpy()
# 	hourly_pressure_msl = hourly.Variables(9).ValuesAsNumpy()
# 	hourly_surface_pressure = hourly.Variables(10).ValuesAsNumpy()
# 	hourly_cloud_cover = hourly.Variables(11).ValuesAsNumpy()
# 	hourly_et0_fao_evapotranspiration = hourly.Variables(12).ValuesAsNumpy()
# 	hourly_vapour_pressure_deficit = hourly.Variables(13).ValuesAsNumpy()
# 	hourly_wind_speed_10m = hourly.Variables(14).ValuesAsNumpy()
# 	hourly_wind_direction_10m = hourly.Variables(15).ValuesAsNumpy()
# 	hourly_wind_gusts_10m = hourly.Variables(16).ValuesAsNumpy()

# 	hourly_data = {"date": pd.date_range(
# 		start = pd.to_datetime(hourly.Time(), unit = "s", utc = True),
# 		end = pd.to_datetime(hourly.TimeEnd(), unit = "s", utc = True),
# 		freq = pd.Timedelta(seconds = hourly.Interval()),
# 		inclusive = "left"
# 	)}
# 	hourly_data["temperature_2m"] = hourly_temperature_2m
# 	hourly_data["relative_humidity_2m"] = hourly_relative_humidity_2m
# 	hourly_data["dew_point_2m"] = hourly_dew_point_2m
# 	hourly_data["apparent_temperature"] = hourly_apparent_temperature
# 	hourly_data["precipitation"] = hourly_precipitation
# 	hourly_data["rain"] = hourly_rain
# 	hourly_data["snowfall"] = hourly_snowfall
# 	hourly_data["snow_depth"] = hourly_snow_depth
# 	hourly_data["weather_code"] = hourly_weather_code
# 	hourly_data["pressure_msl"] = hourly_pressure_msl
# 	hourly_data["surface_pressure"] = hourly_surface_pressure
# 	hourly_data["cloud_cover"] = hourly_cloud_cover
# 	hourly_data["et0_fao_evapotranspiration"] = hourly_et0_fao_evapotranspiration
# 	hourly_data["vapour_pressure_deficit"] = hourly_vapour_pressure_deficit
# 	hourly_data["wind_speed_10m"] = hourly_wind_speed_10m
# 	hourly_data["wind_direction_10m"] = hourly_wind_direction_10m
# 	hourly_data["wind_gusts_10m"] = hourly_wind_gusts_10m


# hourly_dataframe = pd.DataFrame(data = hourly_data)
# print(hourly_dataframe)


