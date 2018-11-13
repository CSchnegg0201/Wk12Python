# Week 12 Python Program Connor Schnegg 11/13/2018
counter = 0
totalScore = 0
testScore = int(input("Enter a test score or 999 to exit: "))
while testScore != 999:
    counter += 1
    totalScore += testScore
    testScore = int(input("Enter a test score or 999 to exit: "))
avgTestScore = totalScore / counter
if avgTestScore >= 90:
    letterGrade = "A"
elif avgTestScore >= 80:
    letterGrade = "B"
elif avgTestScore >= 70:
    letterGrade = "C"
elif avgTestScore >= 60:
    letterGrade = "D"
else:
    letterGrade = "F"
print("The average test score is" , avgTestScore , ", which is a letter grade of" , letterGrade)
if letterGrade == "A":
    print("That is an excellent grade, keep it up!")
elif letterGrade == "B":
    print("That is a good grade, keep working hard!")
elif letterGrade == "C":
    print("That is an okay grade, but you can do a lot better.")
elif letterGrade == "D":
    print("You're falling behind, you need to do better.")
else:
    print("This is unacceptable!")
