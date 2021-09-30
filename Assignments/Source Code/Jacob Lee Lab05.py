print("Welcome to My Prime Number Calculator!")
print()
print("Your options are:")
a = print("a) Is my number prime?")
b = print("b) Print all prime numbers less than my number")
c = print("c) Print the two prime numbers that add up to my even number")
print()
user_choice = input("Please enter your choice: ")
user_num = int(input("Please enter your number: "))
#Defining new Function to find prime numbers
def prime(number):
    #Searching for all numbers between 2 and the number
    for i in range(2,number,1):
        #testing the number to see if it is divisible by any other number
        if number % i == 0:
            return False
    return True
#Secondary definition to find the list of prime numbers
def primes(numbers):
  #Same thing as prime(number)
  for i in range(2, user_num):
    #Setting up secondary testing to check for two prime numbers
    for j in range(2,i):
      if(i % j==0):
        break
    else:
      print(i)
def nonprimes(num, isPrime):
  #Initializing the function as True, the value of isPrime[i] will be False if i is Not prime
  isPrime[0] = isPrime[1] = False
  for i in range (2, num+1):
    isPrime[i] = True
  p = 2
  while(p*p <= num):

    #If isPrime[p] is not changed, it is prime
    if(isPrime[p] == True):
      #This updates the multiples of P
      i = p*p
      while(i <= num):
        isPrime[i] = False
        i +=p
    p += 1
#prints prime pair of the sum
def PrimePairs(n):
    #creates the primes using the previous function
    isPrime = [0] * (n+1)
    nonprimes(n, isPrime)
    #Finding all the numbers for the pari
    for i in range(0, n):
     
        if (isPrime[i] and isPrime[n - i]):
         
            print(i,(n - i))
            return
if user_choice == "a":
  if prime(user_num) == True:
    print("Your number is prime")
  else:
      print("Your number is not prime")
elif user_choice == "b":
  primes(user_num)
elif user_choice == "c":
  PrimePairs(user_num)
