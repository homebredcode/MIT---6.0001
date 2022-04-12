#User input
annual_salary = int(input('Please enter your annual salary\n> '))
portion_saved = float(input('Please enter the percent of your salary to be saved, as a decimal\n> '))
total_cost = int(input('Please enter the cost of your dream home\n> '))
semi_annual_raise = float(input('Enter your semi annual raise:\n> '))
#Initializing
portion_down_payment = total_cost*0.25
current_savings = 0
r = 0.04
monthly_salary = annual_salary/12
months = 1
counter = 1

#Executing
while current_savings < portion_down_payment:
    if counter % 6 == 0:
        monthly_salary += monthly_salary*semi_annual_raise
    current_savings += monthly_salary*portion_saved
    current_savings += ((current_savings*r)/12)
    months += 1
    counter += 1

print(f'number of months {months}')





