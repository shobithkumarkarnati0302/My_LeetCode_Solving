class Solution(object):
    def destCity(self, paths):
        start_cities = set()
        for path in paths:
            start_cities.add(path[0])
            
        for path in paths:
            destination = path[1]
            if destination not in start_cities:
                return destination