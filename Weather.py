import json
import urllib.request
from geopy.geocoders import Nominatim
import tkinter as tk

def get_Location(name):
    geolocator = Nominatim(user_agent="MyApp") # Initialize Nominatim API
    l = geolocator.geocode(name)

    return l.latitude, l.longitude

def get_Data(lat, lon):
    area = urllib.request.urlopen("https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid=05981c208153f8dbbd376121b045ddc4".format(lat,lon)) # Cambridge
    data = json.loads(area.read().decode())

    remove = ["dt","id","cod"]
    for i in list(data):
        for r in remove:
            if i == r:
                del data[i]

def get_input(my_text_box):
   value=my_text_box.get("1.0","end-1c")
   print(value)

def table():
    win = tk.Tk()

    # #Creating a text box widget
    # box = tk.Entry(win, width=15)
    # box.place(relx=100,rely=10,anchor="nw")
    # box.pack()

    #Create a button for Comment
    comment = tk.Button(height=1, width=10, text="Comment", command=lambda: get_input(box))
    comment.pack()

    win.mainloop()


def main():
    table()

    lat, lon = get_Location("Cambridge")
    get_Data(lat, lon)

    # Delete Unessary jason rows
    # Weather is in a list so might need to do a loop for that
    # OpenWeatherAPI uses KELVIN

if __name__ == "__main__":
    main()