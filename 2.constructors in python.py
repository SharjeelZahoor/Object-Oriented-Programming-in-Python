
# defining class
class Student:
    def __init__(self,name,subject):
        self.name = name
        self.subject = subject
        print("new student added to database")


student1 = Student("Ali","Computer Science")
print(student1.name)
print(student1.subject)
student2 = Student("Ahmed","Human Asset")
print(student2.name)
print(student2.subject)