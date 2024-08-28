# circle class and its two methods and radius is in constructor
# printing area and perimeter
class Circle:
    def __init__(self,rad):
        self.rad = rad

    def Area(self):
        area = (22/7) * (self.rad * self.rad)
        return area
    def Perimeter(self):
        peri = 2 * (22/7) * self.rad
        return peri


r1 = Circle(5)
print(r1.Area())
print(r1.Perimeter())