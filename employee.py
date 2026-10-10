class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary
        
    def __str__(self):
        return "Employee Name: {0}, Position: {1}, Salary:{2}, ".format(self.name, self.position, "xxx")
    
    
e1 = Employee("Alex", "Software Engineer", 95000)
print(e1)