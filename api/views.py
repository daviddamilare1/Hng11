from django.shortcuts import render
from django.http import JsonResponse
import requests
import os

def hello(request):
    visitor_name = request.GET.get('visitor_name', 'Guest')
    
    
    client_ip = '102.89.33.134'
    
 
    response = requests.get(f'http://ipinfo.io/{client_ip}/json')
    data = response.json()
    location = data.get('city', 'Unknown')  
    
    
    weather_api_key = os.getenv('OPENWEATHERMAP_API_KEY')
    temperature = "unknown"
    
    if location != 'Unknown':
        weather_response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={location}&units=metric&appid={weather_api_key}')
        weather_data = weather_response.json()
        temperature = weather_data['main']['temp'] if 'main' in weather_data else 'unknown'

    greeting = f"Hello, {visitor_name}! The temperature is {temperature} degrees Celsius in {location}."
    response_data = {
        'client_ip': client_ip,
        'location': location,
        'greeting': greeting,
    }

    return JsonResponse(response_data)























