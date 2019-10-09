SUPER_AGE = 65
keep_going = ""

while keep_going == "":
    age = int(input("How old are you?"))
    if age >= SUPER_AGE:
        print("Yes super")
    else:
        print("NO SUPER FOR YOU!!")

    keep_going = input("If you want to continue press <enter> otherwise press any other letter to quit")

print("Thanks for telling us your personal details we will now sell them ;)")
