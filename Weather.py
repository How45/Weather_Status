import json
import urllib.request
from geopy.geocoders import Nominatim
import tkinter as tk

from matplotlib.pyplot import text

class WeatherStats:
    def __init__(self, name):
        self.City = name

    def get_Location(self):
        return self.long, self.lanti

    def form_Data(self):
        geolocator = Nominatim(user_agent="MyApp") # Initialize Nominatim API
        l = geolocator.geocode(self.City)

        self.long = l.longitude
        self.lanti = l.latitude

        area = urllib.request.urlopen("https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid=05981c208153f8dbbd376121b045ddc4".format(self.lanti,self.long))
        data = json.loads(area.read().decode())

        remove = ["dt","id","cod"]
        for i in list(data):
            for r in remove:
                if i == r:
                    del data[i]

def toUiTwo(box, win): # This will need to change scence
    name = box.get()
    win.destroy()

    wStats = WeatherStats(name)
    UI2(wStats)

def UI2(wStats):
    print("Show UI 2")

    wStats.form_Data()
    print(wStats.get_Location())

def UI1():
    win = tk.Tk()
    win.geometry("700x300")

    #Creating a text box widget
    box = tk.Entry(win, width=15,text="City")
    box.focus_set()
    box.place(x=0,y=0)

    #Create a button for Comment
    comment = tk.Button(win,height=1, width=12, text="Enter", command = lambda: toUiTwo(box,win))
    comment.place(x=0,y=20)

    win.mainloop()

def main():
    UI1()

    # lat, lon = get_Location("Cambridge")
    # get_Data(lat, lon)

    # Delete Unessary jason rows
    # Weather is in a list so might need to do a loop for that
    # OpenWeatherAPI uses KELVIN

if __name__ == "__main__":
    main()