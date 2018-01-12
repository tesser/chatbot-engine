import googlemaps

GOOGLE_MAPS_API_KEY = 'AIzaSyD7W7v5psM8TDJwUV2WxsPkoYRtByh07Y0'

class Geocoder(object):
    def __init__(self):
        self.client = googlemaps.Client(key=GOOGLE_MAPS_API_KEY)

    def encode(self, location):
        result = self.client.geocode(location)

        return result[0]['geometry']['location']['lat'], result[0]['geometry']['location']['lng']
