from forecastiopy import *

DARK_SKY_API_KEY = '8b4d5ca925446f9db4f7d7d0aac8b40c'

class Forecaster(object):
    def __init__(self, lat, lng):
        self.lat = lat
        self.lng = lng

    def weather_summary(self):
        fio = ForecastIO.ForecastIO(apikey=DARK_SKY_API_KEY,
                units=ForecastIO.ForecastIO.UNITS_SI,
                lang=ForecastIO.ForecastIO.LANG_ENGLISH,
                latitude=self.lat,
                longitude=self.lng)

        curr = FIOCurrently.FIOCurrently(fio)

        if fio.has_currently() is True:
            result = "Currently it's %sF. %s" % (curr.get()['temperature'], curr.get()['summary'])
        else:
            result = None

        return result
