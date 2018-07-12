# -*- coding: utf-8 -*-
"""
Created on Mon Jun  25 13:41:10 2018

@author: Ebome
"""
balance=4773 # balance = outstanding balance (未偿付余额)
annualInterestRate=0.2
monthlyPaymentRate=0.04
monthlyInterestRate=annualInterestRate/12.0
i=1
while i<13   :
    i+=1
    monthlyPayment=monthlyPaymentRate*balance
    monthlyUnpaidBalance=balance-monthlyPayment
    balance=monthlyUnpaidBalance+(monthlyInterestRate*monthlyUnpaidBalance)

remain=round(balance,2)
print("Remaining balance: "+ str(remain))




