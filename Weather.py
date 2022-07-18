import json
import urllib.request
from geopy.geocoders import Nominatim
import tkinter as tk
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF, renderPM
from PIL import Image, ImageTk

#/------------------------/ WeatherStats Class /------------------------/
class WeatherStats:
    def __init__(self, name, country):
        self.area = name
        self.country = country

    def form_Data(self):
        geolocator = Nominatim(user_agent="MyApp") # Initialize Nominatim API
        place = self.area, self.country


        l = geolocator.geocode(place)
        # print("Found?")

        self.lon = l.longitude
        self.lan = l.latitude

        #area = urllib.request.urlopen("https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&units=metric&appid=17c432120e10afde68589219f4b8c71d".format(self.lan,self.lon))
        area = urllib.request.urlopen("https://api.openweathermap.org/data/2.5/weather?lat=52.1951&lon=0.1313&units=metric&appid=17c432120e10afde68589219f4b8c71d")
        data = json.loads(area.read().decode())

        remove = ["dt","id","cod"]
        for i in list(data):
            for r in remove:
                if i == r:
                    del data[i]

        for keys in data:
            if keys == "weather":
                for li in data[keys]: # This is a key: list(key,value)
                    for key, value in li.items():
                        if key == "main":
                            self.main = value
                        elif key == "description":
                            self.description = value
            if keys == "main":
                for key, value in data[keys].items():
                    if key == "temp":
                        self.temp = value
                    elif key == "feels_like":
                        self.feel = value
                    elif key == "temp_min":
                        self.min = value
                    elif key == "temp_max":
                        self.max = value
                    elif key == "pressure":
                        self.pressure = value
                    elif key == "humidity":
                        self.humidity = value
        # Setup self_Stuff

    def get_Location(self):
        return self.lan, self.lon

    def get_temp(self):
        return self.temp, self.feel, self.min, self.max

    def get_pressure(self):
        return self.pressure

    def get_humidity(self):
        return self.humidity

def toUiTwo(area,country, ui1): # This will need to change scence
    name = area.get()
    area = country.get()
    ui1.destroy()

    wStats = WeatherStats(name,area)
    wStats.form_Data()

    UI2(wStats)

#/------------------------/ Helper Function /------------------------/
def toUiOne(ui2):
    ui2.destroy()
    UI1()

def posMouse(event):
    x, y = event.x, event.y
    print('{}, {}'.format(x, y))
#/------------------------/ UI /------------------------/
def UI2(s): # Main Change

    # Class setup
    temp, feel, min, max = s.get_temp()

    #UI2 Start
    ui2 = tk.Tk()
    ui2.geometry("700x300")
    ui2.title("UI2 Window")
    ui2.configure(background="black")

    buttonBackg = tk.Frame(ui2,height=283, width=105, borderwidth = 1, bg = "#2B2E25")
    buttonBackg.place(x=589, y=10)
    # /---/
    visualsBackg = tk.Frame(ui2,height=283, width=500, borderwidth = 1, background = "#2B2E25")
    visualsBackg.place(x=10, y=10)

    #button1
    button1 = tk.Button(buttonBackg,height=1, width=12, text="button1") # Hight is 1 = 19, width 10 = 79
    button1.place(x=5, y=5)

    #button2
    button2 = tk.Button(buttonBackg,height=1, width=12, text="button2")
    button2.place(x=5, y=42)

    backwards = tk.Button(buttonBackg,height=1, width=12, text="Go Back", command = lambda: toUiOne(ui2))
    backwards.place(x=5, y=252)
    # Max x 5 y 190 (+37)

    from PIL import Image,ImageTk
    frame = tk.Frame(visualsBackg, height = 0, width = 0)
    frame.place(x=0,y=0)

    icon = (Image.open("Icons\\001lighticons-01.png"))
    rez_img = icon.resize((200,200), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(rez_img)
    label = tk.Label(frame, image = img,bg="#2B2E25")
    label.pack()

    # ui2.bind('<Motion>', posMouse)
    ui2.mainloop()


def UI1():
    #UI1 Start
    ui1 = tk.Tk()
    ui1.geometry("700x300")
    ui1.title("UI1 Window")
    ui1.resizable(width=False, height=False)

    #text
    Enter = tk.Label(ui1, text="Enter Location:")
    Enter.place(x=315, y=274)

    #textBox - place
    box_area = tk.Entry(ui1, width=15)
    box_area.insert(0, "Area...")
    box_area.focus_set()
    box_area.place(x=403, y=276)
    box_area.bind("<Button-1>", lambda a: box_area.delete(0, tk.END))

    #textBox - country
    box_county = tk.Entry(ui1, width=15)
    box_county.insert(0, "Country...")
    box_county.focus_set()
    box_county.place(x=504, y=276)
    box_county.bind("<Button-1>", lambda a: box_county.delete(0, tk.END))

    #button
    comment = tk.Button(ui1,height=1, width=12, text="Enter", command = lambda: toUiTwo(box_area,box_county,ui1))
    comment.place(x=605, y=273)

    # ui1.bind('<Motion>', posMouse)
    ui1.mainloop()

#/------------------------/ Main /------------------------/
def main():
    UI1()

    # Weather is in a list so might need to do a loop for that
    # OpenWeatherAPI uses KELVIN

if __name__ == "__main__":
    main()