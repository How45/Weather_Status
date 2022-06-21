import json
import urllib.request

def main():
    area = urllib.request.urlopen("https://api.openweathermap.org/data/2.5/weather?lat=52.1951&lon=0.1313&appid=05981c208153f8dbbd376121b045ddc4") # Cambridge
    data = json.loads(area.read().decode())
    print(data)

    # Delete Unessary jason rows
    # Weather is in a list so might need to do a loop for that

if __name__ == "__main__":
    main()
