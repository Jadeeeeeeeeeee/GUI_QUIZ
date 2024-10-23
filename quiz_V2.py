import random
import time
#globals and questions lists
score = 0
#global and quesitons lists
country = [
    "France", "Jamaica", "Italy", "Slovakia", "Japan", "Malaysia", "Croatia", 
  "Indonesia", "Greece", "Switzerland"]

right_answer = [
    "Paris", "Kingston", "Rome", "Bratislava", "Tokyo", "Kuala lumpur",
    "Zagreb", "Jakarta", "Athens", "Bern"
]
option_1 = [
    "Berlin", "Madrid", "Manila", "Dubai", "Seoul", "Wellington", "Sydney", "Canberra",
    "Manama", "Gaborone"
]
option_2 = [
    "San Jose", "Djibouti", "London", "Reykjavik", "Dublin", "Tripoli", "Monaco",
    "Moscow", "Victoria", "Damascus"
]


#define a function to generate a question
def generate_question(country, right_answer, option_1, option_2):
    global score
    time.sleep(0.5)
    print("\nWhat is the capital of", country)
    random_sequence = random.randint(0, 2)
    #seperate print statements for readability
    if (random_sequence == 0):
        print("A.", option_1)
        print("B.", option_2)
        print("C.", right_answer, "\nAnswer:")
        answer = input().lower()
        if answer == "c":
            score += 1
            print("Correct!")
            print("Score:", score)
        else:
            print("Score:", score)
            print("Incorrect!")

    elif (random_sequence == 1):
        print("A.", option_1)
        print("B.", right_answer)
        print("C.", option_2, "\nAnswer:")
        answer = input().lower()
        if answer == "b":
            print("Correct!")
            score += 1
            print("Score:", score)
        else:
            print("Score:", score)
            print("incorrect!")

    elif (random_sequence == 2):
        print("A.", right_answer)
        print("B.", option_2)
        print("C.", option_1, "\nAnswer:")
        answer = input().lower()
        if answer == "a":
            print("Correct!")
            score += 1
            print("Score:", score)
        else:
            print("Incorrect!")
            print("Score:", score)


for i in range(0, 10):
    generate_question(country[i], right_answer[i], option_1[i], option_2[i])


