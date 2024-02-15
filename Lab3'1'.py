employee_salaries = {}

while True:
    name = input("Enter employee name (or 'no' to stop): ")
    
    if name.lower() == 'no':
        break
    
    salary = float(input("Enter {}'s salary: ".format(name)))
    
    employee_salaries[name] = salary

print("Employee salaries recorded successfully.")
print("Employee Salaries:", employee_salaries)
