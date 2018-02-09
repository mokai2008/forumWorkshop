def withdraw(balance , request):
    print "current balance is " + str(balance)
    remainder = balance
    if request > balance :
        print "You don't have enough money"
    elif request <= 0 :
        return  str(500 - request)
        
    else :
          remainder = balance - request
          while request > 0:

            if request >= 100:
                request -= 100
                print("give 100")

            elif request >= 50:
                request -= 50
                print("give 50")

            elif request >= 10:
                request -= 10
                print("give 10")

            elif request >= 5:
                request -= 5
                print("give 5")

            elif request < 5:
                print("give " + str(request))
                request = 0
    return remainder

balance = withdraw(500,300)
balance = withdraw(balance , 150)
balance = withdraw(balance,100)