#get the charge amount
charge = float(input('Enter the amount you were charge. $')) 

#apply the tip and tax

tip = charge* .18
tax = charge* .07
total =  charge + tip + tax

#display the amount

print('charge for the food: %.2f' % charge)
print('the tip amount: %.2f' %tip)
print('tax amount: %.2f' %tax)
print('total amount: %.2f' % (charge +tip +tax))
