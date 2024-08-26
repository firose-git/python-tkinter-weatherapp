# Weather Forecast Application
# Overview 
This is a simple desktop application built using Python's Tkinter library that provides current weather information for a specified city. The application fetches weather data from the OpenWeatherMap API and displays it in a user-friendly interface with a gradient background.

# Features 
Fetches current weather information including temperature, humidity, wind speed, and weather description.
User-friendly interface with a gradient background.
Error handling for missing input, invalid API key, and connection issues.
Responsive input field with default text that clears on click.

# Requirements 
Python 3.x
requests library for making HTTP requests to the OpenWeatherMap API.
Tkinter library (comes pre-installed with Python).

# Code Overview
* get_weather()
This function fetches the weather data for the city entered by the user using the OpenWeatherMap API. It then parses the JSON response and displays the relevant weather details or an error message if something goes wrong.
# UI Elements
Canvas: A gradient background is created using a canvas element in Tkinter.
Text Entry: An entry field where the user can input the city name. The default text is "Enter city name...".
Button: A button labeled "Get Weather" triggers the get_weather() function.
# Error Handling
The application includes error handling for various scenarios, such as:
Invalid API key
Empty city name
Invalid city name
Network issues
Screenshots



