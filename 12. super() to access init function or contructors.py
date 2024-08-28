#concept of super()
class Pakistan:
    def __init__(self, lang):
        self.lang = lang
        #this attribute will be accessed by super
    @staticmethod
    def country():
        return "Pakistan is a country"
    @staticmethod
    def population():
        return "Population is above 250 million"

class City(Pakistan):
    def __init__(self,name,lang):
        self.name = name
        print("It is city of Punjab")
        print("this class of city is inherited from punjab class")
        super().__init__(lang)
        # use of super keyword to access attributes of constructor




city1 = City("Chakwal", "urdu")
print(city1.country())
print(city1.lang)



