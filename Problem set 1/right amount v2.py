#User input
annual_salary = int(input('Please enter the starting salary\n> '))

#Initializing values
r = 0.04
portion_down_payment = 0.25
total_cost = 1000000
cost_down_payment = total_cost*portion_down_payment
current_savings = 0
semi_annual_raise = 0.07
counter = 1
epsilon = 100
high_guess = 10000
low_guess = 0
monthly_salary = annual_salary/12
bisection = 1
portion_saved = (high_guess + low_guess) / 2

#Executing
while (high_guess-low_guess) > 0:
    for i in range(1,37):
        if counter % 6 == 0:
            current_savings += current_savings*semi_annual_raise
        current_savings += monthly_salary*((portion_saved)/10000)
        current_savings += monthly_salary*r
        counter += 1
    if current_savings > (cost_down_payment+epsilon):
        high_guess = portion_saved
        print('high guess = portion saved')
    elif current_savings < (cost_down_payment-epsilon):
        low_guess = portion_saved
        print('low guess = portion saved')
    else:
        break
    bisection += 1
    current_savings = 0
    portion_saved = (high_guess + low_guess) / 2
    if portion_saved >= 10000:
        break
portion_saved = portion_saved/10000

if current_savings < (cost_down_payment-epsilon):
    print('It is impossible to pay down in 3 years')
else:
    print(f'Best savings rate {portion_saved}')
    print(f'Steps in bisection: {bisection}')


