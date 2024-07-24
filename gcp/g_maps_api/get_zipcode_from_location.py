import googlemaps

# Initialize the Google Maps client with your API key
gmaps = googlemaps.Client(key='YOUR_API_KEY')


def get_postal_code(lat, lng):
    # Reverse geocode the latitude and longitude to get address components
    reverse_geocode_result = gmaps.reverse_geocode((lat, lng))
    for component in reverse_geocode_result[0]['address_components']:
        if 'postal_code' in component['types']:
            return component['long_name']
    return None


def search_businesses_by_postal_code(p_code, business_type):
    # Use the Places API to search for businesses within the specified postal code
    places_result = gmaps.places(query=business_type, location=p_code)
    return places_result


if __name__ == "__main__":
    current_lat = 40.712776
    current_lng = -74.005974

    postal_code = get_postal_code(current_lat, current_lng)
    if postal_code:
        b_type = "restaurant"
        businesses = search_businesses_by_postal_code(postal_code, b_type)
        for business in businesses['results']:
            print(business['name'], business['formatted_address'])
    else:
        print("Postal code not found for the current location.")
