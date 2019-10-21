# Dictionary of possible exercises
EXERCISE={"chase a mouse": 0.4, "climb a tree": 0.3, "scratch a post": 0.2}
# Starting value for numbered list
number = 1
print("Here are the exercises your cat can do and how much weight it will lose if it does them: ")
for activity, amount in EXERCISE.items():
    print("{}. {} - {}".format(number, activity, amount))
    number += 1

# Loop for testing purposes
for i in range(3):
    exercise_choice = int(input("Please enter the corresponding number to the exercise you would like your pet to do >> "))
    if exercise_choice == 1:
        print("You cat has chased a mouse and has lost {}kg".format(EXERCISE["chase a mouse"]))
    elif exercise_choice == 2:
        print("You cat has climbed a tree and has gained {}kg".format(EXERCISE["climb a tree"]))
    elif exercise_choice == 3:
        print("You cat has scratched a post and has gained {}kg".format(EXERCISE["scratch a post"]))
