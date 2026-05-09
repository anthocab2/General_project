"""
employee_information.py

This program collects basic employee information
using user input and displays the data in a clean format.

The program also calculates the employee's annual salary
based on the monthly salary entered by the user.

Topics practiced:
- Variables
- User Input
- Data Types
- Type Conversion
- Formatted Strings (f-strings)
- Basic Calculations
"""

name_employee = input("Employee name: ")
age_employee = input("Employee age: ")
position_employee = input("Position: ")
salary_employee = int(input("Salary: "))
remote_worker_employee = input("Remote worker (yes/no): ")
year_in_company = int(input("Years in company: "))


print("\nEmploye Information")
print("-------------------")
print(f"Name: {name_employee}")
print(f"Age: {age_employee}")
print(f"Position: {position_employee}")
print(f"Salary: {salary_employee}")
print(f"Anual salary: {salary_employee}")
print(f"Remote Worker: {remote_worker_employee}")
print(f"Years in company: {year_in_company}")
print(f"Annual salary: {salary_employee * 12}")

