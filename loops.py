#if value <= 0:
#    value = int(input ("Enter a positive value!"))

#while value <= 0:
#    value = int(input ("Enter a positive value!"))
#    print("You entered", value)

# Ctrl+C stops infinite loops

#while True:
#   print("Always look on the bright side of life!")

#a = 0
#while a < 3:
#    print(a)
#    a = a+1

#value = 10
#while value > 0:
#    print(value)
#    value -= 1

#num_people = int(input("How many people are there? "))
#i = 0
#total_age = 0.0
#while (i < num_people):
#    age = float(input("Enter the age of person" +str(i+1)+ ": "))
#    total_age = total_age + age
#    i = i+1
#average_age = total_age / num_people
#print("The average age was", average_age)

#While loops vs for loops
#i=0
#while i < :
#i = i+1
#IS THE SAME AS
#for i in range(0, n, 1):

#for i in range (0, 7, 1):
#    print (i)

#for i in range (1, 7, 2):
#    print (i)

#for i in range (5, 1, -1):
#    print (i)

#while value <= 0:
#    value = int(input ("Enter a positive value!"))
#else:
#    print ("You entered", value)

#times tables
#for i in range(10):
#    for j in range(10):
#        print(i, '*', j, '=', i*j)

#possible pairs of a given number of people
#numpeople = input("How many people are there?")
#for i in range(1, numpeople+1):
#    for j in range(i+1, numpeople+1):
#        print(i, j)

#bad_number = 7
#for i in range(1,10,2):
#    if i == bad_number:
#        print("Whoops! We didn't want that number!")
#        break
#    print(i)
#else:
#    print("We got through all the numbers")

#Collatz Conjecture (3n+1)
n = int(input("Enter a number: "))
print(n)

count = 0
while n != 1:
    count += 1
    if n % 2 == 0:
        n = n/2
    else:
        n = 3*n+1
    print(n)

    print("We reached 1 in", count, "steps.")






