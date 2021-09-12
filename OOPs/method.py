## Method in OPPS 

class emp:
    def get_name_age_salary(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
        return None
    def display_details(self):
        print(f'The name is: {self.name}\nThe age is: {self.age}\nThe salary is: {self.salary}')
        return None

emp1=emp()
emp2=emp()

emp1.get_name_age_salary('John', 35, 45000)

print(dir(emp1))


