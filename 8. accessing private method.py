class Account:
    #this method is private
    def __world(self):
        print("how are you")
    #we use this method to access private world() method
    def hello(self):
       self.__world()


a1 = Account()
print(a1. hello())