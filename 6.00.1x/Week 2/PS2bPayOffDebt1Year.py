monthlyIntRate= annualInterestRate/12
getpayment=True
MoPayment = 0

#Create a function to run 12 months of payments, and then create a loop to re-run the function if the Ending Balance is not 0.
def CCPayment(balance, monthlyIntRate, MoPay):
    
    Month = 1 #Month begins at 1

    while Month <= 12:
        balance = (balance - MoPay)
        balance = balance + (monthlyIntRate * balance)
        Month += 1
        if balance <= 0:
            return MoPayment
        else:
            return False

    while getpayment==True: 
        if CCPayment(balance, monthlyIntRate, MoPayment):
            getpayment=False
            print "Lowest Payment: ", CCPayment(balance, monthlyIntRate, MoPayment)
        else:
            MoPayment += 10
            CCPayment(balance, monthlyIntRate, MoPayment)
    

   
