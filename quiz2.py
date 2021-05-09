def verifyAnswer(answer:str, correctAnswer:str, correctOption:str, score:int):
    if answer == correctOption or answer == correctAnswer.lower():
        score+=1
        print("Correct!")
        print("Score: ", score)
        print("\n")
    else: 
        print("Incorrect! The answer is ", correctAnswer, ".")
        print("Score: ", score)
        print("\n")

score = 0



answer1 = input("What is the capital city of Germany? \na. Dresden\nb. Berlin \nc. Frankfurt\nAsnwer: ").lower()
if answer1 == "b" or answer1 == "berlin":
    score += 1
    print("Correct!")
    print("Score: ", score)
    print("\n")
else: 
    print("Incorrect! The answer is Berlin.")
    print("Score: ", score)
    print("\n")


answer2 = input("What is the capital city of France? \na. Amsterdam\nb. Paris \nc. Rome\nAsnwer: ").lower()
score = verifyAnswer(answer2, "b", "Paris", score)

answer3 = input("What is the capital city of Japan? \na. Hong Kong\nb. Tokyo \nc. Taiwan\nAsnwer: ").lower()
if answer3 == "b" or answer3 == "tokyo":
    score += 1
    print("Correct!")
    print("Score: ", score)
    print("\n")
else: 
    print("Incorrect! The answer is Tokyo.")
    print("Score: ", score)
    print("\n")

if score <= 1:
    print("Your total score is:", score, " Sorry, that's bad")
elif score == 2:
    print("Your total score is:", score, " You went ok.")
else:
    print("Your total score is:", score, " Your are awesome!")



        


