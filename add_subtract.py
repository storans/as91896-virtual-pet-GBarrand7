# Program to add or subtract values from the pet's weight

weight = float(input("How much does your pet weigh?"))
add = float(input("How much weight has your pet gained?"))
# Increasing the cat's weight by the specified amount
weight += add
print(weight)
subtract = float(input("How much weight has your pet lost?"))
# Decreasing the cat's weight by a specified amount
weight -= subtract
print(weight)
