#concept of multi level inheritence
# city is inherited from punjab and punjab is inherted from pakistan
class Pakistan:
    @staticmethod
    def country():
        return "Pakistan is a country"
    @staticmethod
    def population():
        return "Population is above 250 million"


class Punjab(Pakistan):
    @staticmethod
    def province():
        return "Punjab is a province inherited from Pakistan class"


class City(Punjab):
    def __init__(self,name):
        self.name = name
        print("It is city of Punjab")
        print("this class of city is inherited from punjab class")




city1 = City("Chakwal")
print(city1.province())
print(city1.country())



