from math import degrees


palgad=[1200,2500,750,395,1200]
inimesed=["A","B","C","D","E"]

option = str

def multple():
    x = 0
    while True:
    try:
        index = name.index("d",x)
        n.append(index)
        x = index + 1
    except:
        break

def menu():
    print("A = Add")
    print("R = Remove")
    print("B = Biggest salary")
    print("S = smallest salary")
    print("H = who same salary")
    print("Q = Quit")

    print()
#1
def AddPeople():
    people = str(input("give name: "))
    salary = int(input("give money: "))

    palgad.append(people)
    inimesed.append(salary)

#2
def RemovePeople():
    for i in range(len(inimesed)):
        print(f"{i+1}: {inimesed[i]}-{palgad[i]}")

    while(True):
        op = str(input("op: "))
        try:
            index = inimesed.index(op)
            inimesed.pop(index)
            palgad.pop(index)
            break
        except:
            print("that does not exits")
            pass
               
    print()

#3
def BiggestSalary():
    index = palgad.index(max(palgad))
    print("The richest")
    print(f"{inimesed[index]} - {palgad[index]}")
    print()

#4
def SmallSalery():
    index = palgad.index(min(palgad))
    print("The poorest")
    print(f"{inimesed[index]} - {palgad[index]}")
    print()

#5
#6
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
    print()

#9
def TopOfAll(): 
    BiggestSalary()
    SmallSalery()
    
#10

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
#14
#15
#16
#17

#18
def FindAletterStart():
    char = str(input(("less or more: ")))
    for i in range(len(inimesed)):
        if (char[0].lower() == "a"):
            print(f"{inimesed[i]}-{palgad[i]}")



while (True):
    menu()
    option = str(input("give an option: "))

    match option.upper():
        case "Q":
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
            tulemaks()
        case _ :
            print("unvalid option")

