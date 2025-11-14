
import requests #Lets you send HTTP requests to web APIs (to get weather data).
from tkinter import * #Tkinter is a standard GUI library for Python, used to create graphical user interfaces.
from tkinter import scrolledtext #Provides a scrollable text widget for output area.

# Function to get weather details
def get_weather(city): #Starts a function that fetches weather for a specific city.
    api_key = "dc27c8d2539943072490651c8a3838bc"  #API key for OpenWeatherMap.
    #Constructs the API request URL using the city name and your API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=dc27c8d2539943072490651c8a3838bc"
    response = requests.get(url) #Sends the request to OpenWeatherMap’s server
    if response.status_code == 200: #Checks if the request was successful (status code 200 means OK)
        data = response.json() #Parses the JSON response into a Python dictionary
        city_name = data['name'] #Gets the city’s name from the response.
        country = data['sys']['country'] #Gets the country code from the response.
        temp_kelvin = data['main']['temp'] #Gets the temperature in Kelvin from the response.
        temp_celsius = temp_kelvin - 273.15 #Converts temperature to Celsius
        weather_desc = data['weather'][0]['main'] #Gets a brief description of the weather (like Clear, Rain, etc.)
        return f"City: {city_name}, {country}\nTemperature: {temp_celsius:.2f} °C\nWeather: {weather_desc}" #Returns a formatted string with city, country, temperature, and weather.
    else:
        return "City not found." #If the request was not successful, returns an error message.

# Function to display weather in the GUI
def show_weather():
    #When “Get Weather” button is clicked: Gets city name entered by the user.
    city = city_text.get()
    weather = get_weather(city) #Calls get_weather function to fetch weather details.
    print(weather)   # This prints the result of the weather request
    # Sets color for success (green) or error (red) in output area
    if "not found" in weather:
        output_text.tag_config("error", foreground="red") #Configures error text color
        output_text.insert(END, weather + "\n", "error") #Inserts error message in output area
    else:
        output_text.tag_config("success", foreground="green") #Configures success text color
        output_text.insert(END, weather + "\n", "success") #Inserts weather info in output area

# Set up the Tkinter window
app = Tk() #Creates the main application window.
app.title("Weather App") #Sets the window’s title to "Weather App".
app.geometry("320x300") #Sets the window size to 320x300 pixels for added space.
app.configure(bg="#aaccee") #Sets light blue background for better visual style.
app.eval('tk::PlaceWindow . center') #Centers the window on the screen.

# Add an app title label at the top
title_label = Label(app, text="Weather App", font=("Helvetica", 16, "bold"), bg="#aaccee") #Title label with larger font and background
title_label.pack(pady=8) #Packs the title label with padding.

#GUI Entry Field for City Name
city_text = StringVar() #StringVar() is a Tkinter variable class that holds a string value.
city_entry = Entry(app, textvariable=city_text, font=("Helvetica", 12)) #Adds a text entry box with specified font
city_entry.pack(pady=10) #Packs the box onto window, with vertical padding
city_entry.insert(0, "Enter city name") #Shows placeholder text in the entry field
city_entry.bind("<FocusIn>", lambda e: city_entry.delete(0, END)) #Clears placeholder text when entry field gets focus

get_weather_btn = Button(app, text="Get Weather", command=show_weather, bg="#2266aa", fg="#fff", font=("Helvetica", 12, "bold")) #Adds styled button labeled “Get Weather”
get_weather_btn.pack(pady=5) #Packs it onto window, below entry box.

output_text = scrolledtext.ScrolledText(app, width=36, height=7, font=("Helvetica", 12)) #Creates a scrollable text output area
output_text.pack(pady=10) #Packs the output area with padding

app.mainloop() #Starts the Tkinter event loop, which waits for user interaction