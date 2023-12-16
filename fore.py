import tkinter as tk
from tkinter import messagebox
import requests

def get_weather():
    api_key = '1873fd1f311ee0a5d5c2ef6637eb3c5c'  # Replace with your OpenWeatherMap API key
    city = city_entry.get()

    if not city:
        messagebox.showerror('Error', 'Please enter a city')
        return

    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    
    try:
        response = requests.get(url)
        weather_data = response.json()

        if 'cod' in weather_data and weather_data['cod'] == 401:
            messagebox.showerror('Error', 'Invalid API key. Please check your API key.')
        elif 'weather' in weather_data and 'main' in weather_data:
            main_info = weather_data['weather'][0]['main']
            description = weather_data['weather'][0]['description']
            temperature = weather_data['main']['temp']
            humidity = weather_data['main']['humidity']
            wind_speed = weather_data['wind']['speed']

            result = f'Weather: {main_info}\nDescription: {description}\nTemperature: {temperature}°C\nHumidity: {humidity}%\nWind Speed: {wind_speed} m/s'

            messagebox.showinfo('Weather Forecast', result)
        else:
            messagebox.showerror('Error', 'Invalid API response. Check the city name.')

    except requests.exceptions.RequestException:
        messagebox.showerror('Error', 'Failed to connect to the server')

# Create the main window
window = tk.Tk()
window.title('Weather Forecast')

# Create a canvas with gradient background
canvas = tk.Canvas(window, width=300, height=200)
canvas.pack()

# Define the gradient colors
start_color = '#4E65FF'  # Blue
end_color = '#92EFFD'    # Ocean

# Create the gradient background
for i in range(200):
    position = i / 200
    r = int((1 - position) * int(start_color[1:3], 16) + position * int(end_color[1:3], 16))
    g = int((1 - position) * int(start_color[3:5], 16) + position * int(end_color[3:5], 16))
    b = int((1 - position) * int(start_color[5:7], 16) + position * int(end_color[5:7], 16))
    color = f'#{r:02x}{g:02x}{b:02x}'
    canvas.create_line(0, i, 300, i, fill=color)

# Create labels and entry fields
canvas.create_text(150, 50, text='Current Weather Forecast', font=('Times', 12, 'bold'), fill='#e8d031')

def clear_text(event):
    city_entry.delete(0, tk.END)  # Clear the default text when clicked

city_entry = tk.Entry(window, width=30, bg='#e8eaed', fg='black')
city_entry.insert(0, "Enter city name...")  # Set the default text
city_entry.bind("<Button-1>", clear_text)  # Bind the click event to clear the text
city_entry_window = canvas.create_window(150, 100, anchor='center', window=city_entry)

get_weather_button = tk.Button(window, text='Get Weather', command=get_weather, bg='#d1d0cb', fg='#000501')
get_weather_button_window = canvas.create_window(150, 150, anchor='center', window=get_weather_button)

# Run the application
window.mainloop()
def new_func(get_weather_button):
    get_weather_button

new_func(get_weather_button)