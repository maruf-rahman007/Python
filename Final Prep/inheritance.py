class Person:
    def __init__(self,name):
        self.name = name
    def getName(self):
        return self.name

class Student(Person):
    def __init__(self, name,id):
        super().__init__(name)
        self.id = id
    def getStudentInfo(self):
        return f"This is {self.getName()} and Id is {self.id}"
class Admin(Person):
    def __init__(self, name):
        super().__init__(name)
        self.results = {}
    def addResult(self,studentId,result):
        self.results[studentId] = result
    def showResult(self):
        print(self.results)


obj = Student("Maruf","222-15-6212")
print(obj.getStudentInfo())
obj1 = Admin("Admin")
obj1.addResult("222-15-6212",{'Math':4.00,'English':3.75})
obj1.addResult("222-15-6213",{'CS':4.00,'EM':3.75})
obj1.showResult()