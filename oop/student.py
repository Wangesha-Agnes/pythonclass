class Student:
    school = "Akirachix"
    
    def __init__(self,first_name,last_name,age,country,code):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.country = country
        self.code = code
        
    
    def greet_student(self):
        greeting = f"Hello {self.first_name}, welcome to {self.school}.Your code is {self.code}."
        return greeting
       
    def year_of_birth(self):
        return f"Hello {self.first_name}, you were born in {2024-self.age}"
    
    def full_name(self):
        return f"Hello your full name is {self.first_name} {self.last_name}"
    
    