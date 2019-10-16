# Program to add or subtract values from the pet's weight
# Function to increase or decrease the cat's weight

# Parameters - sign indicates whether the program should add or subtract, amount specifies the amount of weight to be added or subtracted, weight specifies the weight of the pet
def add_subtract(sign, amount, weight):
        if sign == "add":
            weight += amount
            return weight
        elif sign == "subtract":
            weight -= amount
            return weight

# Testing of function
# Getting user input for the amount of weight to add
weight = float(input("How much does your pet weigh?"))
add = float(input("How much weight has your pet gained?"))
# Increasing the cat's weight by the specified amount
weight = add_subtract("add", add, weight)
print(weight)
# Getting user input for the amount of weight to subtract
subtract = float(input("How much weight has your pet lost?"))
# Decreasing the cat's weight by a specified amount
weight = add_subtract("subtract", subtract, weight)
print(weight)
