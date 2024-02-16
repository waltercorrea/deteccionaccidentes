# Importing required libraries
#from googleplaces import GooglePlaces, types, lang
#import requests
#import json
import requests

# This is the way to make api requests
# using python requests library

# send_url = 'http://freegeoip.net/json'
# r = requests.get(send_url)https://console.cloud.google.com/apis/library?project=my-tesis-312420
# j = json.loads(r.text)
# print(j)
# lat = j['latitude']
# lon = j['longitude']

# Generate an API key by going to this location
# https://cloud.google.com /maps-platform/places/?apis =
# places in the google developers

# Use your own API key for making api request calls
#API_KEY = 'AIzaSyCxgZPDAQq9vaF12EDGBBK5PNmjA6P6754'
API_KEY = 'AIzaSyCxgZPDAQq9vaF12EDGBBK5PNmjA6P6754'

# Initialising the GooglePlaces constructor
#google_places = GooglePlaces(API_KEY)
base_url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json'
location = '28.4089,77.3178' #Latitud y longitud del lugar de búsqueda
radius = 5000 # Radio en metros
place_types = 'hospital' # Tipo de lugar a buscar
# call the function nearby search with
# the parameters as longitude, latitude,
# radius and type of place which needs to be searched of
# type can be HOSPITAL, CAFE, BAR, CASINO, etc
#query_result = google_places.nearby_search(
		# lat_lng ={'lat': 46.1667, 'lng': -1.15},
		#lat_lng ={'lat': 28.4089, 'lng': 77.3178},
		#radius = 5000,
		# types =[types.TYPE_HOSPITAL] or
		# [types.TYPE_CAFE] or [type.TYPE_BAR]
		# or [type.TYPE_CASINO])
		#types =[types.TYPE_HOSPITAL])
#Parametros para la solicitud 
params = {
    'location': location,
    'radius': radius,
    'type': place_types,
	'key': API_KEY
}

# Realiza la solicitud a la API de Google Places
response = requests.get(base_url, params=params)

# Verifica si la solicitud se completó con éxito
if response.status_code == 200:
    data = response.json()
    if 'results' in data:
        for place in data['results']:
            print(place('name'))
            print("Latitud", place["geometry"]['location']['lat'])
            print("Longitud", place["geometry"]['location']['lng'])
            print()
    else:
        print("No se encontraron resultados.")
else:
	print("Error en la solicitud:", response.status_code)
	print(response.text)

# If any attributions related
# with search results print them
#if query_result.has_attributions:
	#print (query_result.html_attributions)


# Iterate over the search results
#for place in query_result.places:
	# print(type(place))
	# place.get_details()
	#print (place.name)
	#print("Latitude", place.geo_location['lat'])
	#print("Longitude", place.geo_location['lng'])
	#print()
