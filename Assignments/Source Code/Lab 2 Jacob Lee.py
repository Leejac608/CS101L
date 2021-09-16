########################################################################
## CS 101 Lab
## Program #2
## Jacob Lee
## Jllw4v@umsystem.edu
print("**** Welcome to the LAB grade calculator! ****")
print("")
## Input's are the beginning of the program, initially it was just the inputs in order to get the users information for grades
name = input("Who are we calculating grades for? ==> ")
print("")

lab_grade = int(input("Enter labs grade? ==> "))
if lab_grade > 100:
  print("The lab value should have been 100 or less. It has been changed to 100.")
  lab_grade = 100
elif lab_grade < 0:
  print("The lab value should have been zero or greater. It has been changed to zero.")
print("")

exam_grade = int(input("Enter the EXAMS grade? ==> "))
if exam_grade < 0:
  print("The exam value should have been zero or greater. It has been changed to zero.")
  exam_grade = 0
elif exam_grade > 100:
  print("The exam value should have been 100 or less. It has been changed to 100.")
  exam_grade = 100
print("")

attendance_grade = int(input("Enter the Attendance grade? ==> "))
print("")
# The calculations were the easiest part it was simple to multiply them by the user input stored by various variables, plus the algorithm for creating the grades were given.
lab_weight = float(lab_grade) * .7
exams_weight = float(exam_grade) * .2
attendance_weight = float(attendance_grade) *.1
weighted_grade = lab_weight + exams_weight + attendance_weight
#The if statements were simple enough, as long as the grade is above x it would spit out an answer
print("The weighted grade for", name,"is ", weighted_grade)
if weighted_grade >= 90.0:
  print(name, "has a letter grade of A")
elif weighted_grade >= 80.0:
   print(name, "has a letter grade of B")
elif weighted_grade >= 70.0:
   print(name, "has a letter grade of C")
elif weighted_grade >= 60.0:
   print(name, "has a letter grade of D")
else:
   print(name, "has a letter grade of F")
print("")
print("**** Thanks for using the Lab grade calculator ****")
