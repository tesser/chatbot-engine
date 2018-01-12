import re

class QueryParser(object):
    def __init__(self, query):
        self.query = query
        self.form1 = re.compile("weather in .+", re.IGNORECASE)
        self.form2 = re.compile("what's the weather in .+", re.IGNORECASE)
        self.form3 = re.compile(".+ weather", re.IGNORECASE)

    def location(self):
        if self.form1.match(self.query):
            segs = self.query.split(' ')
            location = segs[-1]
        elif self.form2.match(self.query):
            segs = self.query.split(' ')
            location = segs[-1]
        elif self.form3.match(self.query):
            segs = self.query.split(' ')
            location = segs[0]
        else:
            location = None

        return location
