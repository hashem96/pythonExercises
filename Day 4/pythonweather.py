import requests

key = "b96fa53e730f427a904104902202110"

class dotdict(dict):
    def __getattr__(self, name):
        return self[name]

user_city = input("Please enter your city : \n")
user_date = input("Please enter the date (YY-MM-DD):\n")
url = (f'http://api.weatherapi.com/v1/history.json?key={key}&q={user_city}&dt={user_date}')

r = requests.get(url)

data = r.json()

forecast_data = dotdict(dotdict(dotdict(dotdict(dotdict(data).forecast).forecastday[0]).day).condition).text

print("\n")
print("*****")
print(f" => Weather in {user_city} will be {forecast_data} in {user_date}")
print("*****")


