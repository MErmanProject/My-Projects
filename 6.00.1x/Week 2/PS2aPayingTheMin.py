Month =1
MoIntRate=annualInterestRate/12
TotalPaid = 0 

while (Month < 13):
    print "Month: " +str(Month)

    MinMoPay=(balance*monthlyPaymentRate)
    MoUnpaidBal=(balance-MinMoPay)
    balance=MoUnpaidBal+(MoIntRate*MoUnpaidBal)
    TotalPaid +=MinMoPay
    print "Minimum monthly payment: " + str(round(MinMoPay,2))
    print "Remaining balance: " + str(round(balance,2))
    
    Month += 1           
print "Total paid: " + str(round(TotalPaid,2))     
print "Remaining balance: " + str(round(balance,2))

