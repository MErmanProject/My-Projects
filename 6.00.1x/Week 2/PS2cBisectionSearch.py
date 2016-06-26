monthlyIntRate= annualInterestRate/12.0
getpayment=True
ranonce=False
MoMin = balance/12
MoMax = (balance*(1+monthlyIntRate)**12)/12.0
MoPayment = (MoMin+MoMax)/2
NewBal=0

#Create a function to run 12 months of payments, and then create a loop to re-run the function if the Ending Balance is not 0.
def CCPayment(balance, monthlyIntRate, MoPay):
    global NewBal    
    Month = 1 #Month begins at 1
    
    while Month <= 12:
        balance = (balance - MoPay)
        balance = balance + (monthlyIntRate * balance)
        NewBal=balance
        Month += 1
        if (balance < .02) and (balance > -0.02) :
            return MoPayment
        else:
            return False

    while getpayment==True: 
        if CCPayment(balance, monthlyIntRate, MoPayment):
            getpayment=False
            print "Lowest Payment: ", round(CCPayment(balance, monthlyIntRate, MoPayment),2)
        else:
            if NewBal < 0.01: #paid too much! Lower the max payment and rerun function
                if ranonce == True:
                    MoMax=MoPayment
                    MoPayment=(MoMin+MoMax)/2
                ranonce = True
                CCPayment(balance, monthlyIntRate, MoPayment)

            elif NewBal > 0.01: #didn't pay enough! Raise min payment and rerun function
                if ranonce == True:
                    MoMin=MoPayment
                    MoPayment=(MoMin+MoMax)/2
                    
                ranonce = True
                CCPayment(balance, monthlyIntRate, MoPayment)