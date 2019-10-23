# Function to check if the cat has died or is near death
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
    weight = float(input("How much does your pet weigh?"))

    death_checker(weight, 3.5, 4.5, "You pet has died from starvation", "Your pet has died from obesity", "Make sure to feed your cat soon!", "Make sure to exercise your cat soon", 0.3)
