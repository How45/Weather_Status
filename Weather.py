import json
import urllib.request
from geopy.geocoders import Nominatim
import tkinter as tk

#/------------------------/ WeatherStats Class /------------------------/
class WeatherStats:
    def __init__(self, name, country):
        self.area = name
        self.country = country

    def get_Location(self):
        return self.lanti, self.long

    def form_Data(self):
        geolocator = Nominatim(user_agent="MyApp") # Initialize Nominatim API
        a = self.area,self.country
        print(a)

        l = geolocator.geocode(a)
        print("Found?")

        self.long = l.longitude
        self.lanti = l.latitude

        area = urllib.request.urlopen("https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid=05981c208153f8dbbd376121b045ddc4".format(self.lanti,self.long))
        data = json.loads(area.read().decode())
        print(data)

        remove = ["dt","id","cod"]
        for i in list(data):
            for r in remove:
                if i == r:
                    del data[i]

        # Setup self_Stuff

#/------------------------/ UI Function /------------------------/
def toUiTwo(area,country, ui1): # This will need to change scence
    name = area.get()
    area = country.get()
    ui1.destroy()

    wStats = WeatherStats(name,area)
    UI2(wStats)

def toUiOne(ui2):
    ui2.destroy()
    UI1()

#/------------------------/ UI /------------------------/
def UI2(wStats): # Main Change
    #Class setup
    wStats.form_Data()

    print(wStats.get_Location())

    #UI2 Start
    ui2 = tk.Tk()
    ui2.geometry("700x300")
    ui2.title("UI2 Window")

    w = tk.Canvas(ui2, width=250, height=200)
    w.create_rectangle(0, 0, 100, 100, fill="blue", outline = 'blue')
    w.pack

    backwards = tk.Button(ui2,height=1, width=12, text="Go Back", command = lambda: toUiOne(ui2))
    backwards.place(x=0,y=0)

    ui2.mainloop()

def UI1():
    #UI1 Start
    ui1 = tk.Tk()
    ui1.geometry("700x300")
    ui1.title("UI1 Window")

    #text
    Enter = tk.Label(ui1,text="Enter Location:")
    Enter.place(x=0,y=0)

    #textBox - place
    box_area = tk.Entry(ui1, width=15)
    box_area.insert(0,"Area...")
    box_area.focus_set()
    box_area.place(x=85,y=0)

    #textBox - country
    box_county = tk.Entry(ui1, width=15)
    box_county.insert(0,"Country...")
    box_county.focus_set()
    box_county.place(x=183,y=0)

    #button
    comment = tk.Button(ui1,height=1, width=12, text="Enter", command = lambda: toUiTwo(box_area,box_county,ui1))
    comment.place(x=85,y=22)

    ui1.mainloop()

#/------------------------/ Main /------------------------/
def main():
    UI1()

    # Weather is in a list so might need to do a loop for that
    # OpenWeatherAPI uses KELVIN

if __name__ == "__main__":
    main()