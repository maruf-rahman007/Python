class Student:
    def __init__(self,name,id,email,cgpa):
        self.name = name
        self.id = id
        self.email = email
        self.cgpa = cgpa
    

class Undergraduate(Student):
    def __init__(self, name, id, email, cgpa,courses):
        super().__init__(name, id, email, cgpa)
        self.courses = courses
    
    def calculate_waiver(self):
        if super().cgpa >= 3.50:
            print("Getting 20% waiver!") 
        else:
            print("No waiver!")
    
    def course_taken(self):
        print("All the taken courses are : ")
        print(self.courses)
        
    def calculate_fees(self):
        if super().cgpa >= 3.50:
            print("Total fees are :" ,45000 - (45000*0.20)) 
        else:
            print("Total fees are :",45000)


class Graduate(Student):
    def __init__(self, name, id, email, cgpa,advaisor):
        super().__init__(name, id, email, cgpa)
        self.advaisor = advaisor
    
    def calculate_waiver(self):
        if super().cgpa >= 3.75:
            print("Getting 25% waiver!") 
        else:
            print("No waiver!")
    
    def getAdvaisorName(self):
        print("The advaisor name is :"+ self.advaisor)
        
    def calculate_fees(self):
        if super().cgpa >= 3.75:
            print("Total fees are :" ,45000 - (45000*0.25)) 
        else:
            print("Total fees are :",45000)

        