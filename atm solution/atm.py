money = 500
request = int(raw_input("You have $500 : Enter the amount of money to withdraw $"))
def withdraw(x):
    if x > 500 :
        print "You don't have enough money"
    else :
        while x > 99 :
            print "give 100"
            x = x -100
        while x > 49 :
            print "give 50"
            x = x -50
        while x > 9 :
            print "give 10"
            x = x -10
        while x > 4 :
            print "give 5"
            x = x -5
        while x > 0 :
            print "give " + str(x)
            x = 0
        return "You have got all of your money requested"

print withdraw(request)