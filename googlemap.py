# importing googlemaps module 
import googlemaps 

# Requires API key 
gmaps = googlemaps.Client(key='your api key') 

# Requires cities name 
my_dist = gmaps.distance_matrix('dungarpur','jaipur')['rows'][0]['elements'][0] 

# Printing the result 
print(my_dist) 

