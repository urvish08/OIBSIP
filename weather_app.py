import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import requests
from datetime import datetime

# Your OpenWeatherMap API key
API_KEY = '2c013ecce27fb12c3862a43d4e26a820'

# Function to get weather data for a city
def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    return response.json()

# Function to display weather data
def display_weather():
    city = city_entry.get()
    if city:
        weather_data = get_weather(city)
        if weather_data['cod'] == 200:
            result = (
                f"Weather in {city}:\n"
                f"Temperature: {weather_data['main']['temp']}°C\n"
                f"Weather: {weather_data['weather'][0]['description']}\n"
                f"Humidity: {weather_data['main']['humidity']}%\n"
                f"Wind Speed: {weather_data['wind']['speed']} m/s"
            )
            result_label.config(text=result)
            last_updated_label.config(text=f"Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        else:
            messagebox.showerror("Error", f"Could not retrieve weather data for {city}")
    else:
        messagebox.showwarning("Input Error", "Please enter a city name.")

# Function to clear input and output fields
def clear_fields():
    city_entry.delete(0, tk.END)
    result_label.config(text="")
    last_updated_label.config(text="")

# Set up the main application window
root = tk.Tk()
root.title("Weather App")
root.geometry("600x400")

# Load the background image
background_image = Image.open("background.jpg")
background_photo = ImageTk.PhotoImage(background_image)

# Create a canvas to hold the background image
canvas = tk.Canvas(root, width=600, height=400)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=background_photo, anchor="nw")

# Create a title label
title_label = tk.Label(root, text="Weather App", font=("Helvetica", 18, "bold"), bg="#ADD8E6")
title_label_window = canvas.create_window(300, 50, anchor="center", window=title_label)

# Create an entry for city name
city_entry = tk.Entry(root, font=("Helvetica", 12))
city_entry_window = canvas.create_window(300, 120, anchor="center", window=city_entry)
city_entry.insert(0, "Enter city name")

# Create a button to get the weather
get_weather_button = tk.Button(root, text="Get Weather", command=display_weather, font=("Helvetica", 12), bg="#4682B4", fg="white")
get_weather_button_window = canvas.create_window(300, 170, anchor="center", window=get_weather_button)

# Create a label to display the weather result
result_label = tk.Label(root, text="", font=("Helvetica", 12), bg="#ADD8E6")
result_label_window = canvas.create_window(300, 240, anchor="center", window=result_label)

# Create a label to display the last updated time
last_updated_label = tk.Label(root, text="", font=("Helvetica", 10), bg="#ADD8E6")
last_updated_label_window = canvas.create_window(300, 290, anchor="center", window=last_updated_label)

# Create a button to clear input and output fields
clear_button = tk.Button(root, text="Clear", command=clear_fields, font=("Helvetica", 12), bg="#4682B4", fg="white")
clear_button_window = canvas.create_window(300, 340, anchor="center", window=clear_button)

# Start the Tkinter main loop
root.mainloop()
