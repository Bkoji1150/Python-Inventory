
'''

class Emp(object):
    def name_salary(self,name,salary):
        try:
            self.name=name
            self.salary=salary
        except Exception as e:
            print(e)
        return None

    def display(self):
        try:
            print(F"The name is: {self.name}\nThe Salary is {self.salary}")
        except Exception as e:
            print(e)
        return None


def main():
    try:
        emp1=Emp()
        emp1.name_salary('koji', 4000)
        emp2=Emp()
        emp2.name_salary('Better',34000)
        emp1.display()
        emp2.display()
    except Exception as e:
        print(e)
    return None


if __name__ == '__main__':
    main()

'''

### Using __init__


class Emp(object):
    def __init__(self,name,salary):
        try:
            self.name=name
            self.salary=salary
        except Exception as e:
            print(e)
        return

    def display(self):
        try:
            print(F"The name is: {self.name}\nThe Salary is {self.salary}")
        except Exception as e:
            print(e)
        return None


def main():
    try:
        emp1=Emp('Koji',50000)
        emp1.display()
        emp2=Emp('Kelder',1209)
        emp2.display()
    except Exception as e:
        print(e)
    return None


if __name__ == '__main__':
    main()