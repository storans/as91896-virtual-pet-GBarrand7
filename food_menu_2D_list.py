# Setting the starting number for the numbered list
number = 1
# 2D list of foods and their weight gain value
foods = [["salmon", 0.4], ["jelly meat", 0.3], ["biscuits", 0.2]]

print("Here are the foods available and how much weight your cat will gain if it eats them:")
# Printing each food and it's corresponding weight gain value from the 2D list in a numbered list
for food in foods:
    print("{}. {} - {}".format(number, food[0], food[1]))
    # Increasing the number for the numbered list
    number += 1
