money = 500
request = int(raw_input("You have $500 : Enter the amount of money to withdraw $"))
def withdraw(x):
    if x > 500 :
        print "You don't have enough money"
    if x <= 0 :
        return  str(500 - x)
        
    else :
         while x > 0:

            if x >= 100:
                x -= 100
                print("give 100")

            elif x >= 50:
                x -= 50
                print("give 50")

            elif x >= 10:
                x -= 10
                print("give 10")

            elif x >= 5:
                x -= 5
                print("give 5")

            elif x < 5:
                print("give " + str(request))
                x = 0
    return "You have got all of your money requested"

withdraw(request)
print "The amount available in your account is " + str(money - request)