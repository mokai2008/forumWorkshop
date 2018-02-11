class ATM : 
    
    def __init__(self, balance, bank_name) :
        self.balance = balance
        self.bank_name = bank_name

    def withdraw(self,request) :
       
        print "==" *10
        print "Welcome to " + self.bank_name          
        print "current balance is " + str(self.balance)
        print "==" *10

        if request > self.balance :
            print "You don't have enough money"

        elif request <= 0 :
            print  str(self.balance - request)
            
        else :
            self.balance -= request

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
            
        return self.balance

balance1 = 5000
balance2 = 1000
		
atm1 = ATM(balance1, "Smart Bank")
atm2 = ATM(balance2, "Baraka Bank")

atm1.withdraw(277)
atm1.withdraw(800)

atm2.withdraw(900)
atm2.withdraw(2000)