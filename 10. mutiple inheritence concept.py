#concept of multiple inheritence
# Toyota and Suzuki classes are inherited from car class
class Car:
    @staticmethod
    def start():
        return "Car started!"
    @staticmethod
    def stop():
        return "Car stopped!"
class Toyota(Car):
    def __init__(self, name, model):
        self.name = names
        self.model = model
class Suzuki(Car):
    def __init__(self, name, model, type):
        self.name = name
        self.model = model
        self.type = type


car1 = Toyota("Civics", 2022)
print(car1.name)
print(car1.start())
print(car1.stop())
print(car1.model)
print("**************")
car2 = Suzuki("Bolan", 2018, "8 seater")
print(car2.name)
print(car2.start())
print(car2.stop())
print(car2.model)
print(car2.type)