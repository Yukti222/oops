class Employe:
    def __init__ (self,name,age,proffession):
        self.name= name
        self.age= age
        self.proffession = proffession


class Full_time(Employe):
    def __init__(self,monthly_salary,calculate_salary, name, age, proffession):
        super().__init__(self,name,age,proffession)
        self.monthly_salary = 0.0
        self.calculate_salary = self.monthly_salary * 12


class Part_time(Employe):
    def __init__(self,hourly_salary,hours_worked,name,age,proffession):
        super().__init__(self,name,age,proffession)
        self.hourly_salary = 0.0
        self.hours_worked = 0
        self.calculate_salary = self.hourly_salary * self.hours_worked 

def create_employe():
        name = input("enter the name of the employer: ")
        age = int(input("enter the age of the employer: "))
        proffession = input("enter the proffession of the employer: ")
        timing = input ("enter the timing of the employer (full time/ part-time):")
        if timing == "full time":
            monthly_salary = float (input("enter the monthly salary of the employer: "))
            print (monthly_salary)
        elif timing == "part time":
            hourly_salary = float (input("enter the hourly salary of the employer: "))
            hours_worked = int (input("enter the hours worked by the employer: "))
            print ("total salary= " + str(hourly_salary * hours_worked))



create_employe()