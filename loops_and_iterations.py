#while loop in if-then

#value = 0
#while value <= 0:
#   value = 0
#    print ("The value is:", value)

#value = 3
#while value > 0:
#    print(value)
#    value = -3
#    print(value)
#    value = 7

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

##range starts with the limit number assumes 0 going up 1 each time

#for i in range (1, 20, 3):
#    print (i)

#for i in range (2):
#    print (i)

#for i in range (10, 1, -1):
#    print (i)

##Times tables 0-9
# for i in range(10):
#     for j in range (10):
#         print(i, '*', j, '=', i*j)

# for i in range(1,11):
#     for j in range (10):
#         print(i, '*', j, '=', i*j)

##break
# bad_number = 7
# for i in range (1,10,2):
#     if i == bad_number:
#         print("Whoops! We didn't want that number!")
#         break
#     print(i)
# else:
#     print("We got through all the numbers")

##collats collection
n = int(input("Enter a number: "))
print(n)
count = 0
while n != 1:
    count += 1
    if n % 2 == 0:
        n  = n/2
    else:
        n = 3*n+1
    print(n)

    print("We reached 1 in", count, "steps.")


        






