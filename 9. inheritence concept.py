
#concept of inheritence
class Car:
    @staticmethod
    def start():
        return "Car started!"
    @staticmethod
    def stop():
        return "Car stopped!"
class Toyota(Car):
    def __init__(self, name, model):
        self.name = name
        self.model = model


c1 = Toyota("Civics", 2018)
print(c1.name)
print(c1.start())
print(c1.stop())
print(c1.model)
