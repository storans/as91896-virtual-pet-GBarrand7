FOODS = {"salmon": 0.4, "jelly meat": 0.3, "biscuits": 0.2}
# Starting number for numbered list
number = 1
print("Here are the foods available and how much weight your cat will gain if it eats them:")
for food, amount in FOODS.items():
    print("{}. {} - {}".format(number, food, amount))
    number += 1

