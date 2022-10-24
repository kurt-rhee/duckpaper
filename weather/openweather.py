import requests
from utils import get_environment_variable


def get_weather(config):

    url = f"""
    https://api.openweathermap.org/data/2.5/weather?
    lat={config['latitude']}&
    lon={config['longitude']}&
    appid={get_environment_variable('openweather_key')}
    """
    print(url)

    r = requests.get(url)
    return r


if __name__ == '__main__':
    import json
    config = json.load(open('../config.json'))
    r = get_weather(config)
    print(r.json())
