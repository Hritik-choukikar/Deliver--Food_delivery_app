class ResturantManager:
    _instance = None

    def __init__(self):
        self.restaurants = []

    @classmethod
    def get_instance(cls):
        if not cls._instance:
            cls._instance = ResturantManager()
        return cls._instance

    def add_resturant(self, res):
        self.restaurants.append(res)

    def search_by_location(self, loc):
        location = loc.lower()
        return [res for res in self.restaurants if res.res_address == location]
