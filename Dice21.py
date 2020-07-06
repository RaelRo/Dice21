import random

print("\n \t Dice21 \n\n Throw the dice against the machine! \n The competitor with the least numeric difference to 21 wins. Sums greater than 21 lose. \n\n")

dice_comp=0
dice_hum=0
roc_max=0
roh_max=0
value=0
y=['y']
se=int(6)
fue=int(5)
einund=int(21)

def ran_roll ():
    value=random.randint(1,6)
    return value;

for i in range(3):
    dice_hum+=ran_roll()
    dice_comp+=ran_roll()
    print("Human's current sum:", dice_hum)
    print("Machine's current sum:", dice_comp)
    print("__________________________")

#human interaction begins
while dice_comp<=einund and dice_hum<=einund and roh_max==0 or roc_max==0:
    if roh_max==0:
        s=input("Does the human want to roll the dice again? (y/n):")
        if s in y:
            dice_hum+=ran_roll()
            print("Human's current sum:", dice_hum)
            if dice_hum>=einund:
                roh_max+=dice_hum
        else:
            print("Human is on hold")
            roh_max+=dice_hum
    else:
        print("Human is on hold")
        
        
    if roc_max==0 and dice_hum<=einund and dice_comp<einund and (einund-dice_comp)>=fue:
        dice_comp+=ran_roll()
        print("Machine's current sum:", dice_comp)
        print("__________________________")
    elif roc_max==0 and roh_max!=0 and dice_hum<=einund and roh_max>dice_comp and dice_comp<einund:
        dice_comp+=ran_roll()
        print("Machine's current sum:", dice_comp)
        print("__________________________")
        
    else:
        roc_max=dice_comp
        print("Machine is on hold")
        print("__________________________")


if roh_max==0 and dice_hum>=einund:
    roh_max=dice_hum
elif roc_max==0 and dice_comp>=einund:
    roc_max=dice_comp
            
#Game ends with results
print("__________________________")
print("Your sum:", roh_max)    
print("The machine's sum:", roc_max)

print("\n")
print("==========================")

if roh_max>einund and roc_max>einund:
    print("\t No winner.")
    exit
elif roh_max>einund:
    print("    The machine won!")
    exit
elif roc_max>einund:
    print("\t You won!")
    exit
elif roh_max>roc_max:
    print("\t You won!")
    exit
elif roh_max==roc_max:
    print("\t Draw!")
    exit
else:
    print("    The machine won!")
    exit

print("==========================")

