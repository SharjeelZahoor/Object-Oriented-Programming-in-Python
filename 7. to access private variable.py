class Account:
    def __init__(self, name, pw):
        self.name = name
        self.__pw = pw
        #to make it private i used __ before pw

    def showpass(self):
        print(self.__pw)


acc1 = Account("Ali", 1234)
print(acc1.name)
# print(acc1.__pw)
# through an error because i already made it private by __.
print(acc1.showpass())