import json
import urllib.request
from geopy.geocoders import Nominatim
import tkinter as tk


#/------------------------/ WeatherStats Class /------------------------/
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

#/------------------------/ UI Function /------------------------/
def toUiTwo(box, ui1): # This will need to change scence
    name = box.get()
    ui1.destroy()

    wStats = WeatherStats(name)
    UI2(wStats)

def UI2(wStats):
    #Class setup
    wStats.form_Data()
    print(wStats.get_Location())

    #UI2 Start
    ui2 = tk.Tk()
    ui2.geometry("700x300")
    ui2.title("UI2 Window")

    ui2.mainloop()

def UI1():
    #UI1 Start
    ui1 = tk.Tk()
    ui1.geometry("700x300")
    ui1.title("UI1 Window")

    #textBox
    box = tk.Entry(ui1, width=15,text="City")
    box.focus_set()
    box.place(x=0,y=0)

    #button
    comment = tk.Button(ui1,height=1, width=12, text="Enter", command = lambda: toUiTwo(box,ui1))
    comment.place(x=0,y=20)

    ui1.mainloop()

#/------------------------/ Main /------------------------/
def main():
    UI1()

    # Weather is in a list so might need to do a loop for that
    # OpenWeatherAPI uses KELVIN

if __name__ == "__main__":
    main()