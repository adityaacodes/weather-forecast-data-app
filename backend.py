import requests

api_key = "6dcb1a20e5ba79127b0088b074358bb2"


def get_data(place, forecast_days):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={api_key}"
    response = requests.get(url)
    contents = response.json()
    data = contents['list']
    nr_values = 8 * forecast_days
    filtered_data = data[:nr_values]
    return filtered_data


if __name__ == "__main__":
    print(get_data(place='Tokyo', forecast_days=1))
