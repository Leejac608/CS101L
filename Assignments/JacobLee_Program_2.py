''' 
Jacob Lee 
Comp-Sci 101 
TuTh 1:00 - 2:15
Program 2 
Created 09/13/2022
Due Date 09/25/2022


Algorithm 
    1: import the random module to allow for random facts
    2: create a data set to represent and hold all the facts/lies
    3: display the name of program and fact/truth
    4: create a while loop to keep user playing and to create variables
    5: create another while loop to keep track of how many guesses the user has
    6: ask user for their guess
    7: read in input and search to find if it is truth or false, if truth reward with a point and display, if false decrease points and display
    8: make error handling statements to make sure the user cannot input anything other than desired inputs
    9: print out the results 
    10: ask if they would play again and repeat
'''
import random 

#Facts about myself
'''
data = [{
    "msg" : "I have a cat",
    "type" : "truth"
  }, {
    "msg" : "My name is John",
    "type" : "lie"
  }, {
    "msg" : "I like coding",
    "type" : "truth"
  },]

#Displaying the Game name 
print("Welcome To TWO TRUTH AND A LIE\n")

while True:
  selected = []
  
  correct = 0
  incorrect = 0
  i = 1
  while i < 3:
    #select random integer from 1 to 3
    selectedNumber = random.randint(1, 3)

    #check already selected or not
    while selectedNumber in selected:
      selectedNumber = random.randint(1, 3)
  
    selected.append(selectedNumber)
  
    #Showing my fact
    print("Truth or Lie??\n")
    print(data[selectedNumber - 1]["msg"])

    #prompt the user to guess
    user_input = input("1 - Truth \n2 - Lie\n")

    #verify input of user
    if user_input == '1':
      if data[selectedNumber - 1]["type"] == "truth":
        correct += 1
        i += 1
        print("Your choice is correct\n")
      elif data[selectedNumber - 1]["type"] == "lie":
        incorrect += 1
        i += 1
        print("Your choice is incorrect\n")
    elif user_input == '2':
      if data[selectedNumber - 1]["type"] == "lie":
        correct += 1
        i += 1
        print("Your choice is correct\n")
      elif data[selectedNumber - 1]["type"] == "truth":
        incorrect += 1
        i += 1
        print("Your choice is incorrect\n")
    else:
        print("Invalid input")
        print("Please try again")
        continue
        

    #display correct and incorrect choice
  print("Number of correct choice :", correct)
  print("Number of incorrect choice :", incorrect)

  #prompt the user to check that user want to play it again
  temp = input("\nWant to play again (Y/y) (N/n) : ")
  if temp in ["Y", "y", "Yes", "yes"]:
    continue
  else:
    break
'''
S = [1,2,4,5,2,4]
for i in S:
    for j in S:
        if i < j:
            print("yay")
        elif i > j:
            print("No")
    