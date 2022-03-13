from random import randint

attempt_tracker = 1
randbool = True
probability = 50

print("Under the law of the many world's interpretation...")
print("Which posits that there are an infinite number of 'You's..")
print("There exists a version of 'You' which is immortal, one that does not die...")
question_1 = input("Would you like to find out if you are 'The One'?\n")
if question_1 != "yes":
    print("Disappointing...")
else:
    print("Good, this is how it will work...")
    print("Everytime you press the prompt there is a 50% chance of you 'winning'...")
    print("But also a 50% chance of you losing...")
    print("See how many times you survive, that is, if you ever lose...")
    question_2 = input("Ready?\n")
    if question_2 != "yes":
        print("Disappointing...")
    else:
        while randbool is True:
            input("Attempt " + str(attempt_tracker) + ": \n")
            attempt_tracker += 1
            probability = probability / 2
            randbool = bool(randint(0, 1))

    print("YOU DIED! It was a " + str(probability) + "% chance.")
