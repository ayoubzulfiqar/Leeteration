class Solution:
    def destCity(self, paths: list[list[str]]) -> str:
        source_cities = set()
        for cityA, cityB in paths:
            source_cities.add(cityA)

        for cityA, cityB in paths:
            if cityB not in source_cities:
                return cityB