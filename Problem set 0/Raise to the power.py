import math
def raise_():
    user_input1 = int(input('Please enter a number:\n> '))
    user_input2 = int(input('Please enter a number to be raised to:\n> '))
    a = user_input1**user_input2
    b = math.log2(user_input1)

    return a, b

print(raise_())
