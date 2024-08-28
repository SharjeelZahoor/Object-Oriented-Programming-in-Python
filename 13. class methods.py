# concept of class methods
# if we want to change in class attributes then we made class methods
class Country:
    name = "not given"

    @classmethod
    def giveName(cls,name):
        cls.name = name


country1 = Country()
country1.giveName("Pakistan")
print(Country.name)
# print(c1.name)
#through an error that name country has no arruments


