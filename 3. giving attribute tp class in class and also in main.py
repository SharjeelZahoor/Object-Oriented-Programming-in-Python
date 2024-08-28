# defining class
class Student:
    uni_name = "Virtual University"
    def __init__(self,name,subject):
        self.name = name
        self.subject = subject
        print("new student added to database")



student1 = Student("Ali","Computer Science")
print(student1.name, student1.subject)
print(student1.uni_name)
student2 = Student("Ahmed","Human Resource Management")
print(student2.name, student2.subject)
print(student2.uni_name)
