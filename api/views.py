# myapp/views.py

from django.http import JsonResponse
import requests
import os

def hello(request):
    
    visitor_name = request.GET.get('visitor_name', 'Mark')

    
    client_ip = '102.89.33.134'

    
    location = 'Unknown'
    try:
        response = requests.get(f'http://ipinfo.io/{client_ip}/json')
        data = response.json()
        location = data.get('city', 'Ashburn')  
    except requests.RequestException:
        location = 'Unknown'

    
    temperature = "unknown"

    
    weather_api_key = os.getenv('OPENWEATHERMAP_API_KEY')
    

    if location != 'Unknown' and weather_api_key:
        try:
            weather_response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={location}&units=metric&appid={weather_api_key}')
            weather_data = weather_response.json()
            if weather_data.get('cod') == 200:  
                temperature = weather_data['main'].get('temp', 'unknown')
        except requests.RequestException:
            temperature = 'unknown'

  
    greeting = f"Hello {visitor_name}! the temperature is {temperature} degrees Celsius in {location}"

    
    response_data = {
        'client_ip': client_ip,
        'location': location,
        'greetings': greeting,
    }

    return JsonResponse(response_data)