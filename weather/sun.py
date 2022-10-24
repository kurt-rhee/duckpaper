import os
import json
import requests
from dateutil import tz
from datetime import date, datetime
from timezonefinder import TimezoneFinder

# --- load config object ---
dirname = os.path.dirname(__file__)
config = json.load(
    open(os.path.join(dirname, '../config.json'))
)

# --- get date today ---
today = str(date.today())


def get_sunrise_sunset():

    # --- get timezone from latitude and longitude ---
    tf = TimezoneFinder()
    timezone = tf.timezone_at(lat=config['latitude'], lng=-config['longitude'])

    # --- get timezones ---
    url = f'https://api.sunrise-sunset.org/json?lat={config["latitude"]}&lng={-config["longitude"]}'
    r = requests.get(url)
    sunrise = r.json()['results']['sunrise']
    sunset = r.json()['results']['sunset']

    # --- convert to local time ---
    from_zone = tz.gettz('UTC')
    to_zone = tz.gettz(timezone)

    times = []
    for s in [sunrise, sunset]:
        s = today + ' ' + s
        s = datetime.strptime(s, "%Y-%m-%d %I:%M:%S %p")
        s = s.replace(tzinfo=from_zone)
        s = s.astimezone(to_zone)
        times.append(s)

    sun_times = {
        'sunrise': str(times[0]),
        'sunset': str(times[1])
    }

    return sun_times


if __name__ == '__main__':
    sun_time = get_sunrise_sunset()
