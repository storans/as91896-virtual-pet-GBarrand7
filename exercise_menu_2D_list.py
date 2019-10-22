# 2D list of exercises and their weight loss value
exercises = [["chase a mouse", 0.4], ["climb a tree", 0.3], ["scratch a post", 0.2]]

# Setting the starting number for the numbered list
number = 1

print("Here are the exercises available and how much weight your cat will lose if it does them:")
# Printing each food and it's corresponding weight gain value from the 2D list in a numbered list
for exercise in exercises:
    print("{}. {} - {}".format(number, exercise[0], exercise[1]))
    # Increasing the number for the numbered list
    number += 1
