import json
import urllib.request
from geopy.geocoders import Nominatim
import tkinter as tk

from matplotlib.pyplot import text

class WeatherStats:
    def __init__(self, name):
        self.City = name

    def get_Location(name):
        geolocator = Nominatim(user_agent="MyApp") # Initialize Nominatim API
        l = geolocator.geocode(name)

        return l.latitude, l.longitude

    def get_Data(lat, lon):
        area = urllib.request.urlopen("https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid=05981c208153f8dbbd376121b045ddc4".format(lat,lon))
        data = json.loads(area.read().decode())

        remove = ["dt","id","cod"]
        for i in list(data):
            for r in remove:
                if i == r:
                    del data[i]

class menu:
    def get_input(box):
        string = box.get()
        print(string)
        return

    def table():
        win = tk.Tk()
        win.geometry("700x300")

        #Creating a text box widget
        box = tk.Entry(win, width=15,text="City")
        box.focus_set()
        box.place(x=0,y=0)

        #Create a button for Comment
        comment = tk.Button(win,height=1, width=12, text="Enter", command = lambda: menu.get_input(box))
        comment.place(x=0,y=20)

        win.destroy
        win.mainloop()

def main():
    t = menu()
    t.table()

    # lat, lon = get_Location("Cambridge")
    # get_Data(lat, lon)

    # Delete Unessary jason rows
    # Weather is in a list so might need to do a loop for that
    # OpenWeatherAPI uses KELVIN

if __name__ == "__main__":
    main()