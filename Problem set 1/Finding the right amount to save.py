starting_salary = int(input('Enter the starting salary:\n> '))
annual_return = 0.04
semi_annual_raise = 0.07
r = 0.04
down_payment = 0.25
total_cost = 1000000
months = 36
to_pay = total_cost*down_payment
high_guess = 10000
epsilon = 100
low_guess = 0
salary = starting_salary
current_savings = 0
count = 0
portion_saved = (high_guess+low_guess)/2

while (high_guess - low_guess) > 0:
    current_savings = 0
    for i in range(36):
        if i % 6 == 0 and i != 0:
            salary += salary * semi_annual_raise
        current_savings += (salary / 12) * (portion_saved) / 10000 + current_savings * r / 12
    if (current_savings < (to_pay-epsilon)):
        low_guess = portion_saved
    elif (current_savings > to_pay+epsilon):
        high_guess = portion_saved
    else:
        break
    portion_saved = (high_guess+low_guess) / 2
    salary = starting_salary
    count += 1

if current_savings < (to_pay-100):
    print('It is impossible to pay within 3 years')
else:
    print(f'Savings rate {portion_saved/10000}')
    print(f'Bisection steps: {count}')