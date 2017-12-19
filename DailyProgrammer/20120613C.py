"""
One of the sites where daily weather forecasts are shown is here [http://weather.noaa.gov/pub/data/forecasts]

Get the forecast of any asked city and also try to be more innovative in your answers

It seems the number of users giving challenges have been reduced. Since my final exams are going on and its kinda
difficult to think of all the challenges, I kindly request you all to suggest us interesting challenges at
/r/dailyprogrammer_ideas .. Thank you!
"""

import requests
import apikeys_20120613C as keys
import json


def get_coordinated(address):
    gmap_url = ('https://maps.googleapis.com/maps/api/geocode/json?address={}&key={}'
                .format(address, keys.gmaps_api))

    loc_data = requests.get(gmap_url)
    loc_data = loc_data.content.decode('utf-8')
    loc_data = json.loads(loc_data)

    print('Location: {}'.format(loc_data['results'][0]['formatted_address']))
    latitude = loc_data['results'][0]['geometry']['location']['lat']
    longitude = loc_data['results'][0]['geometry']['location']['lng']

    return latitude, longitude


def get_weather(latitude, longitude):
    weather_url = 'https://api.weather.gov/points/{},{}'.format(latitude, longitude)
    weather_first = requests.get(weather_url)
    weather_first = weather_first.content.decode('utf-8')
    weather_first = json.loads(weather_first)

    weather_second = requests.get(weather_first['properties']['forecast'])
    weather_second = weather_second.content.decode('utf-8')
    weather_second = json.loads(weather_second)

    return weather_second['properties']['periods']


def print_weather(forecast):
    for line in forecast:
        print(line['name'])
        print('    Temperature: {} F'.format(line['temperature']))
        print('    Wind: {} {}'.format(line['windSpeed'], line['windDirection']))
        print('    Forecast: {}'.format(line['detailedForecast']))
        print('')


def main():
    # location = input('enter location: ')
    location = '98052'
    latitude, longitude = get_coordinated(location)

    print('({}, {})'.format(latitude, longitude))
    print('\n')

    forecast = get_weather(latitude, longitude)
    print_weather(forecast)


if __name__ == "__main__":
    main()
