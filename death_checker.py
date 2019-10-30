# Function to check if the cat has died or is near death
# Parameters:
# Weight - weight of pet
# Low - lowest possible weight
# High - highest possible weight
# Too_low - message if the cat's weight is too low
# Too_high - message if the cat's weight is too high
# Near_low - message is the cat's weight is near being too low
# Near_high - message is the cat's weight is near being too high
# Boundary - range above the lowest weight or below the highest weight that if the cat's weight is in it is near being too low or high
def death_checker(weight, low, high, too_low, too_high, near_low, near_high, boundary):
    # If cat's weight is below the lowest weight
    if weight < low:
        print(too_low)
    # If cat's weight is above the highest weight
    elif weight > high:
        print(too_high)
    # If cat's weight is between the lowest weight and a weight near the lowest weight (e.g 3.5 - 3.8)
    elif low <= weight <= (low + boundary):
        print(near_low)
    # If cat's weight is below the highest weight and a weight near the highest weight (e.g 4.2 - 4.5
    elif high >= weight >= (high - boundary):
        print(near_high)
    # If the cat is in a healthy weight range
    else:
        print("Your pet weighs {}kg".format(weight))

# Loop for testing all possible types of input
for i in range(5):
    # Getting the weight of the pet from the user
    weight = float(input("How much does your pet weigh?"))
    # Using death checker to check if the entered weight is too high, too low, near the highest weight, near the lowest weight or fine and providing an appropriate feedback message
    death_checker(weight, 3.5, 4.5, "You pet has died from starvation", "Your pet has died from obesity", "Make sure to feed your cat soon!", "Make sure to exercise your cat soon", 0.3)

