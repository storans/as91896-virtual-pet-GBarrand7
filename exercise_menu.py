# Dictionary of possible exercises
EXERCISE={"chase a mouse": 0.4, "climb a tree": 0.3, "scratch a post": 0.2}
# Starting value for numbered list
number = 1
print("Here are the exercises your cat can do and how much weight it will lose if it does them: ")
for activity, amount in EXERCISE.items():
    print("{}. {} - {}".format(number, activity, amount))
    number += 1
