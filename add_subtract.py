# Program to add or subtract values from the pet's weight
# Function to increase or decrease the cat's weight

# Parameters - amount specifies the amount of weight to be added or subtracted, weight specifies the weight of the pet
# Function to increase the pet's weight
def add(amount, weight):
    weight += amount
    return weight

# Function to decrease the pet's weight
def subtract(amount, weight):
    weight -= amount
    return weight

# Testing of function
# Getting user input for the amount that their cat weighs
weight = float(input("How much does your pet weigh?"))
# Getting user input for the amount of weight to add
increase = float(input("How much weight has your pet gained?"))
# Increasing the cat's weight by the specified amount
weight = add(increase, weight)
print(weight)
# Getting user input for the amount of weight to subtract
decrease = float(input("How much weight has your pet lost?"))
# Decreasing the cat's weight by a specified amount
weight = subtract(decrease, weight)
print(weight)
