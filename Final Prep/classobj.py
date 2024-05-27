class Person:
    name = "This is name"
    # def __init__(mar,name):
    #     mar.name = name
    def info(self):
        return f"Hello this is {self.name} ."
    
obj1 = Person()
print(obj1.info())
print(obj1.name)