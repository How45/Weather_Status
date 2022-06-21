import json
import urllib.request

def main():
    PortsmouthWeather = urllib.request.urlopen("https://api.openweathermap.org/data/2.5/weather?lat=50.8036831&lon=-1.075614&appid=05981c208153f8dbbd376121b045ddc4")
    data = json.loads(PortsmouthWeather.read().decode())
    print(data)

    # Delete Unessary jason rows
    # Weather is in a list so might need to do a loop for that

if __name__ == "__main__":
    main()
