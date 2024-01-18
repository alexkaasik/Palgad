from math import degrees


palgad=[1200,2500,750,395,1200]
inimesed=["A","B","C","D","E"]

option = str

def multiple():
    c = 0
    n = []
    NewList = []

    for x in set(inimesed):
        NewList.append(x)

    NewList.sort()

    while (True):
        option = str(input("Who to pick: "))
        if option in NewList:
            break
        else:
            print("that name does not exits")

    while True:
        try:
            index = inimesed.index(option, c)
            n.append(index)
            c = index + 1
        except:
            break
    
    for x in range(len(n)):
        print(f" {x+1} {inimesed[n[x]]} {palgad[n[x]]} ")
    
    print()
    
    if ( len(n) >> 1 ):
        pick = int(input("pick what to remove: "))-1
        answer = n[pick]
    elif ( len(n) == 1 ):
        answer = n[0]
    
    return answer

def menu():
    print()
    print()
    print("A = Add") #1
    print("R = Remove") #2 
    print("B = Biggest salary") #3
    print("S = smallest salary") #4 
    print(" = ") #5
    print(" = Find out who receives the same salary") #6
    print(" = ") #7
    print(" = who receive more/less than the specified amount.") #8
    print(" = Show the richest person and poorest perspn") #9
    print(" = ") #10
    print(" = Calculate the salary that a person will receive in hand after calculating income tax") #11
    print(" = ") #12
    print(" = salary below average and remove them from the lists") #13
    print(" = ") #14
    print(" = Every year the companies employees salaries are raised by 5%") #15
    print(" = ") #16
    print(" = ") #17
    print(" = starting with the entered letter and their salaries") #18
    print("Q = Quit")

    print()
#1
def AddPeople():
    people = str(input("give name: "))
    salary = int(input("give money: "))

    inimesed.append(people)
    palgad.append(salary)
    print()
    
#2
def RemovePeople():
    for i in range(len(inimesed)):
        print(f"{i+1}: {inimesed[i]}-{palgad[i]}")

    inimesed.pop(multiple())

#3
def BiggestSalary():
    print("Riches")
    NewList = []
    n = []
    c = 0

    for x in set(palgad):
        NewList.append(x)
    
    NewList.sort()

    while True:
        try:
            index = palgad.index(NewList[-1], c)
            n.append(index)
            c = index + 1
        except:
            break

    for x in range(len(n)):
        print(f"{x+1}: {inimesed[n[x]]}, {palgad[n[x]]}")

#4
def SmallSalery():
    print("poorest")
    NewList = []
    n = []
    c = 0

    for x in set(palgad):
        NewList.append(x)
    
    NewList.sort()

    while True:
        try:
            index = palgad.index(NewList[0], c)
            n.append(index)
            c = index + 1
        except:
            break

    for x in range(len(n)):
        print(f"{x+1}: {inimesed[n[x]]}, {palgad[n[x]]}")

#5
#6
def SameSalary():

    NewList = []

    for x in set(palgad):
        NewList.append(x)

    NewList.sort()
    
    for x in range(len(NewList)):
        c = 0
        n = []
        while ( palgad.count(NewList[x]) >> 1):
            try:
                index = palgad.index(NewList[x], c)
                n.append(index)
                c = index + 1
            except:
                break
            
        for xy in n:
            print(f"{inimesed[xy]} {palgad[xy]}")

#7
#8
def MoreOrLess():
    lm = str(input(("less or more: ")))
    numb = int(input(("numb: ")))

    for i in range(len(inimesed)):

        if (lm[0].lower() == "m") and (numb < palgad[i]):
            print(f"{inimesed[i]}-{palgad[i]}")
        if (lm[0].lower() == "l") and (numb > palgad[i]):
            print(f"{inimesed[i]}-{palgad[i]}")
        else:
            continue

#9
def TopOfAll(): 
    BiggestSalary()
    SmallSalery()

    print()
#10
def keskmine():
    price = float()
    for x in palgad:
        price+=x
    
    f = price/len(palgad)

    for x in range(len(palgad)):
        if f > palgad[x]:
            print(f"{inimesed[x]}-{palgad[x]}")

#11
def tulemaks():
    n = []
    for x in range(len(palgad)):
        if (palgad[x] <= 1200):
            n.append(palgad[x] - 500)
        elif (palgad[x] > 1200 and palgad[x] < 2100):
            n.append(500 - ( 0.55556 * ( palgad[x]-1200 ) ))
        else:
            n.append(palgad[x]-0)


    for i in range(len(palgad)):
        print(f"{inimesed[i]}-{n[i]}")
        print(f"{inimesed[i]}-{palgad[i]}")

#12
#13
def RA():
    price = float()
    for x in palgad:
        price+=x
    
    f = price/len(palgad)
    for x in range(len(palgad),0,-1):
        if f < palgad[x]:
            inimesed.pop[x] 
            palgad.pop[x]

#14
#15
def YearRaised():
    per = 1.05
    year = int(input("yaer: "))
    for x in range(year):
        print(f"{x+1}y")
        for i in range(len(inimesed)):
            print(f"{inimesed[i]} { round(palgad[i]*per,2) }")
        per*=1.05
#16
#17
#18
def FindAletterStart():
    x=0
    letter = str(input(("1 char: ")))
    
    for i in inimesed:
        if i[0].lower() == letter:
            print(f"{i}-{palgad[x]}")
        x+=1

while (True):
    menu()
    option = str(input("give an option: "))

    match option.upper():
        case "Q":
            print("BYE")
            exit()
        case "A":
            AddPeople()
        case "R":
            RemovePeople()
        case "B":
            BiggestSalary()
        case "S":
            SmallSalery()
        case "M":
            MoreOrLess()
        case "TEST":
            SameSalary()
        case _ :
            print("unvalid option")
