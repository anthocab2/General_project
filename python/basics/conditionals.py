"""
conditionals.py

This program simulates an employee access checker.
It practices conditional statements, comparison operators,
logical decision-making, user input, and formatted output.
"""

employee_name = input("Employee name: ")
employee_age = int(input("Employee age: "))
years_in_company = int(input("Years in company: "))
department = input("Department: ")
has_id_card = input("Has ID card? yes/no: ").lower()

if employee_age < 18:
    status = "Access denied: employee must be at least 18 years old."
elif has_id_card != "yes":
    status = "Access denied: ID card required."
elif years_in_company >= 3:
    status = "Access granted: senior employee access."
else:
    status = "Access granted: standard employee access."

print("\nAccess Result")
print("-------------")
print(f"Employee: {employee_name}")
print(f"Department: {department}")
print(f"Status: {status}")
