class Myclass:
    def __init__(self,name,age,result):
        self.name = name
        self._age = age
        self.__result = result
    def showinfo(self):
        print("Name is",self.name,"Age is",self._age,"and results are ",self.__result)
    def get_result(self):
        return self.__result
obj = Myclass("Maruf",23,"Good")
print(obj.name)
print(obj._age)
print(obj.get_result())
obj.showinfo()