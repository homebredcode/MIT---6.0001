annual_salary = int(input('Please enter your starting annual salary:\n> '))
portion_saved = float(input('Please enter the portion of your salary to be saved:\n> '))
total_cost = int(input('Please enter the total cost of your dream home: \n> '))
semi_annual_raise = float(input('Please enter the semi-annual raise, as a decimal:\n> '))

#Initializing values
portion_down_payment = 0.25
r = 0.04
current_savings = 0
to_pay = total_cost*portion_down_payment
months = 0

while current_savings < to_pay:
    current_savings += (annual_salary/12)*portion_saved
    current_savings += (current_savings*r)/12
    months += 1
    if months % 6 == 0:
        annual_salary += annual_salary*semi_annual_raise
print(f'number of months: {months}')