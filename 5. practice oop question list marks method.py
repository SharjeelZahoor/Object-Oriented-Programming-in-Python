class Student:
    def __init__(self,name, marks):
        self.name = name
        self.marks = marks

    def avg(self):
        total = sum(self.marks)
        avg = total/len(self.marks)
        print(f"{self.name}! your average marks are : {avg} ")


s1=Student("Ali",[91,90,92])
s1.avg()

