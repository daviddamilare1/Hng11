import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def temperature(request):
    visitor_name = request.GET.get('visitor_name', 'Mark')

    # Extract client's IP address
    client_ip = request.META.get('HTTP_X_FORWARDED_FOR', request.META.get('REMOTE_ADDR')).split(',')[0]

    location = 'Unknown Location'
    temperature = 'Unknown'

    if client_ip:
        try:
            # Fetch location based on IP
            ip_info_response = requests.get(f'http://ipinfo.io/{client_ip}/json')
            ip_info_response.raise_for_status()
            ip_info_data = ip_info_response.json()
            location = ip_info_data.get('city', location)

            # Fetch temperature for the location
            weather_api_key = 'def5a426fe74ee7e6749406e70be6c91'  # Replace with your OpenWeatherMap API key
            weather_response = requests.get(
                f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={weather_api_key}&units=metric'
            )
            weather_response.raise_for_status()
            weather_data = weather_response.json()
            temperature = weather_data.get('main', {}).get('temp', temperature)
        except requests.RequestException as e:
            print(f'Error fetching data: {e}')

    # Construct response data
    response_data = {
        'client_ip': client_ip,
        'location': location,
        'greeting': f'Hello, {visitor_name}, the temperature is {temperature} degrees Celsius in {location}'
    }

    return Response(response_data)




































# import requests
# from rest_framework.decorators import api_view
# from rest_framework.response import Response

# @api_view(['GET'])
# def hello(request):
#     visitor_name = request.GET.get('visitor_name', 'Mark')

#     # Get client's external IP address from request headers
#     x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
#     if x_forwarded_for:
#         client_ip = x_forwarded_for.split(',')[0]
#         print(client_ip)
#     else:
#         client_ip = request.META.get('REMOTE_ADDR')
#         print('error')

#     # Fetch location based on IP
#     if client_ip:
#         try:
#             ip_info_response = requests.get(f'http://ipinfo.io/{client_ip}')
#             ip_info_response.raise_for_status()  # Check for HTTP errors
#             ip_info_data = ip_info_response.json()
#             location = ip_info_data.get('city', 'Unknown Location')
#             print(f'IP Info response: {ip_info_data}')  # Debug print entire response
#         except requests.RequestException as e:
#             print(f'Error fetching IP info: {e}')  # Debug print error
#             location = 'Unknown Location'

#         # Fetch temperature for the location
#         if location != 'Unknown Location':
#             try:
#                 weather_response = requests.get(
#                     f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid=43e769b33eb4f77f65c367a2670055cc&units=metric'
#                 )
#                 weather_response.raise_for_status()  # Check for HTTP errors
#                 weather_data = weather_response.json()
#                 temperature = weather_data.get('main', {}).get('temp', 'Unknown')
#                 print(f'Weather response: {weather_data}')  # Debug print entire response
#             except requests.RequestException as e:
#                 print(f'Error fetching weather data: {e}')  # Debug print error
#                 temperature = 'Unknown'
#         else:
#             temperature = 'Unknown'
#     else:
#         location = 'Unknown Location'
#         temperature = 'Unknown'

#     # Construct response data
#     response_data = {
#         'client_ip': client_ip,
#         'location': location,
#         'greeting': f'Hello, {visitor_name}, the temperature is {temperature} degrees Celsius in {location}'
#     }

#     print(f'Response data: {response_data}')  # Debug print response data

#     return Response(response_data)
