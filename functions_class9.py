#def warn():
#    print("Warning! Use program at your own risk.")
#a = 3
#print (a)
#warn()
#print("Welcome!")

####Function to warn@@@
def warn():
    print("Warning! Use program at your own risk.")
    ans = input("Do you want to continue? (Y/N")
    if (ans == 'n') or (ans == 'N'):
        quit()

###program to get information
warn()
name = input ("Enter your name:")
warn()
address = input ("Enter your addres:")
warn()
ccn = ("Type in your credit card number:")
warn()
expiration = ("Enter the expiration date for your card:")