import time
print(time.ctime())


name = input("Enter your name:")
address = input("Enter your address:")
age = int(input("Enter your age:" ))

if age <= 100:
    print("valid")
else:
    print("invalid")
    while age in age:
        print(age)
        print("invalid")

gender = input("Gender: M/F ").upper()
if gender == "M":
    print("Male")
    if gender == "Female":
        print ("Female")  
elif gender == "F":
    print("Female")
else: "updated files"

print("invalid")


status = input("status: S/M/D/W/").upper()


if status == "S":
    print("Single")
elif status == "M":
    print("Married")
elif status == "D":
    print("divorce")
elif status == "W":
    print ("widow")
else:
    print("invalid")

a = input(' ').upper()

while a:
    if a  == 'Y':
        print("\n \n")
        break
    else:

        print("\n ok!!!!")
        exit()



print()
print("age:" , (age))
print("Name:" ,(name))
print("address:" ,(address))
print("Gender:" ,(gender))
print("status:" ,(status))
print()


print("\n*************************************************************************************\n")
print("\n                           INTRODUCTION                                              \n")
print("\n quizgame a type of game where players are guessed each question is multiple choices.\n")
print()
print("\n*************************************************************************************\n")
print()
print()




#question
question  = ["1.)what symbol is used in python to assign values to a variable?: ", 
            "2.)Programmer, like anyone else can make mistakes.These can be snytax or loggical errors?: ", 
            "3.)What is the process of analyzing and removing causes of failures in the software?: ", 
            "4.)A set of attributes that bear on the effort needed to make any changes to existing software?: ", 
            "5.)Python is an example of a ? ", 
            "6.)the number of word we give to a variable ? ",
            "7.)What is the word (command) used to display and text on the scrren? ", 
            "8.)What is a variable?  ", 
            "9.)What is function is used to output a message in python", 
            "10.)How would you print a text string? "]

                
#option            
options =  ((' ',"A.equal = \nB.Plus + \nC.Forward slash / \nD.Asterick *\n"), #
            (' ',"A.Programming error \nB.Logic errors \nC.looping issues \nD.Program misunderstood \n"),
            (' ',"A.Bebugging \nB.Failure \nC.Validation \nD.Debugging \n"),
            (' ',"A.Portability \nB.Maintainability \nC.Reliability \nD.Continuos testing \n"),
            (' ',"A.Text-basedprogramming language  \nB.a foreign language \nC.language written in java script \nD.Visual-based programming language \n"),
            (' ',"A.Value  \nB.Bug \nC.Information \nD.text \n"),
            (' ',"A.Print  \nB.Input \nC.Output \nD.Command \n"),
            (' ',"A box(memory location)where stre values \nB.type of grapics  \nC.data type \nD.type of memory \n"),
            (' ',"A.print \nB.input = name  \nC.name = input  \nD.name=input \n"),
            (' ',"A.output  ""hello!" "" 'B.print("hello!")' "  ""C.print(hello!) " "D.output(hello!) "))


#answer
answers = ("A", "A", "D", "B", "A", "A", "A", "A", "A", "B")

#gueses
guesses = []

#question
question_num = 0

score = []

#invalid entry

invalidvalid_entry = set ('EFGHIJKLMNOPQRSTUVWXWZ')


for quiz in question:

    print("=====================")
    print(quiz)

    for option in options[question_num]:

        
        print(option)
    guess = input("Enter (A , B, C, D): ").upper()
    

    while guess == '':
        print("")
        print(quiz)
        print(option)    
        guess = input("Enter (A , B, C, D): ").upper()

    while guess in invalidvalid_entry:
        print("")
        print(quiz)
        print(option)
        print("invalid")    
        guess = input("Enter (A , B, C, D): ").upper()    

    if guess == answers[question_num]:
        score.append(guess)
        print("CORRECT")
        
    elif guess != answers[question_num]:
        print("INCORECT")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1 




print("===========")
print("  Result   ")
print("===========")


print("answers: ", end="")
for answer in answers:
    print(answer, end= " ")
print()

percentage = (len(score) * 100) / 10

print(f'You have {percentage:.2f}% passing rate.')

if percentage > 50:
    print('Congrats! You Passed!')
else:
    print('Sorry you failed !')



  

