import random

print("\n \t Dice21 \n\n Throw the dice against the machine! \n The competitor with the least numeric differenz to 21 wins. Sums greater than 21 lose. \n\n")

dice_comp=0
dice_hum=0
roc_max=0
roh_max=0
a_list=[]
y=['y']
n=['n']
z=0
se=int(6)
fue=int(5)
einund=int(21)

for i in range(100):
    value=random.randint(1,6)
    s=str(value)
    a_list.append(s)
    
    
dice_hum+=int(a_list.pop())
print("Human's current sum:", dice_hum)
dice_comp+=int(a_list.pop())
print("Machine's current sum:", dice_comp)
print("__________________________")
dice_comp+=int(a_list.pop())
dice_hum+=int(a_list.pop())
print("Human's current sum:", dice_hum)
print("Machine's current sum:", dice_comp)
print("__________________________")
dice_comp+=int(a_list.pop())
dice_hum+=int(a_list.pop())
print("Human's current sum:", dice_hum)
print("Machine's current sum:", dice_comp)
print("__________________________")
#human interaction begins
s=input('Does the human want to roll the dice again? (y/n):')
roh1=dice_hum
if s in y:
    dice_hum+=int(a_list.pop())
    print("Human's current sum:", dice_hum)
else:
    print("Human is on hold")
    roh_max+=roh1
    
roc1=dice_comp
if (einund-roc1)>=fue and dice_hum<=einund and roc1<einund:
    dice_comp+=int(a_list.pop())
    print("Machine's current sum:", dice_comp)
    print("__________________________")
else:
    roc_max+=roc1
    print("Machine is on hold")
    print("__________________________")
    

#Round_2
roh2=dice_hum
if roh_max<=0 :
    s=input('Does the human want to roll the dice again? (y/n):')
    if s in y:
        dice_hum+=int(a_list.pop())
        print("Human's current sum:", dice_hum)
    else:
        print("Human is on hold")
        roh_max+=roh2
else:
    print("")
    
roc2=dice_comp
if roc_max is z and dice_hum<=einund and roc2<einund and (einund-roc2)>=fue:
    dice_comp+=int(a_list.pop())
    print("Machine's current sum:", dice_comp)
    print("__________________________")
else:
    roc_max=roc2
    if roc1 is not roc2:
        print("Machine is on hold")
        print("__________________________")
    else:
        print("")

#Round_3
roh3=dice_hum
if roh_max<=0 :
    s=input('Does the human want to roll the dice again? (y/n):')
    if s in y:
        dice_hum+=int(a_list.pop())
        print("Human's current sum:", dice_hum)
    else:
        print("Human is on hold")
        roh_max+=roh3
else:
    print("")
    
roc3=dice_comp
if roc_max is z and roh_max<=einund and roc3<einund and ((einund-roc3)+(dice_hum-roc3))>=se and roc3<=dice_hum:
    dice_comp+=int(a_list.pop())
    print("Machine's current sum:", dice_comp)
    print("__________________________")
else:
    roc_max=roc3
    if roc2 is not roc3:
        print("Machine is on hold")
        print("__________________________")
    else:
        print("")
    
#Round_4
roh4=dice_hum
if roh_max<=0 :
    s=input('Does the human want to roll the dice again? (y/n):')
    if s in y:
        dice_hum+=int(a_list.pop())
        print("Human's current sum:", dice_hum)
    else:
        print("Human is on hold")
        roh_max+=roh4
else:
    print("")
    
roc4=dice_comp
if roc_max is z and roh_max<=einund and roc4<einund and (einund-roc4)>=se and roc4<dice_hum:
    dice_comp+=int(a_list.pop())
    print("Machine's current sum:", dice_comp)
    print("__________________________")
else:
    roc_max=roc4
    if roc3 is not roc4:
        print("Machine is on hold")
        print("__________________________")
    else:
        print("")
    
   
#Round_5
roh5=dice_hum
if roh_max<=0 :
    s=input('Does the human want to roll the dice again? (y/n):')
    if s in y:
        dice_hum+=int(a_list.pop())
        print("Human's current sum:", dice_hum)
        roh_max=dice_hum
    else:
        print("Human is on hold")
        roh_max=roh5
else:
    print("")
    
roc5=dice_comp
if roc_max is z and roh_max<=einund and roc5<einund and (einund-roc5)>=se and roc5<=dice_hum:
    dice_comp+=int(a_list.pop())
    print("Machine's current sum:", dice_comp)
    print("__________________________")
    roc_max=dice_comp
else:
    roc_max=roc5
    if roc4 is not roc5:
        print("Machine is on hold")
    else:
        print("")
    

print("__________________________")
print("Your sum:", roh_max)    
print("The machine's sum:", roc_max)

print("\n")
print("==========================")

if roh_max>einund and roc_max>einund:
    print("No winner.")
elif roh_max>einund:
    print("The machine won!")
    exit
elif roc_max>einund:
    print("You won!")
    exit
elif roh_max>roc_max:
    print("You won!")
    exit
elif roh_max==roc_max:
    print("Draw!")
    exit
else:
    print("The machine won!")
    exit

print("==========================")


