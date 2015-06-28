__author__ = 'Silvia'

print ("Tax Calculator")
cost = input("Enter cost: $")
print ("$"+cost)
cost = int(cost)

taxType = input("a)Federal (10%)\nb)State (8.5%) Tax ?: ")

def taxCalc(taxType):

    if (taxType == 'a'):
        tax = .10
    elif(taxType == 'b'):
        tax = .085
    else:
        print ("Invalid input")

    taxAmount = cost*tax
    total = taxAmount + cost
    return print("Total cost: "+str(total))
taxCalc (taxType)