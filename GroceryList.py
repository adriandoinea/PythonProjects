"""This is a program in which the user makes a shopping list by introducing
different products in it."""


d={}
def meniu():
    print("""Press:
            0 - For showing the list
            1 - For entering a new item
            2 - For deleting an existing item
            3 - For deleting the whole list
            9 - For exit
            """)

def lista_c():
    while True:
        meniu()
        optiune=int(input("Choose your option "))
        if optiune==0:
            for i,j in d.items():
                print(i,j)
            continue
        elif optiune==1:
            while True:
                prod=input("Insert the product or press 5 to go back to the menu ")
                if d:
                    cheie=max(d.keys())+1
                else:
                    cheie=1
                d[cheie]=prod
                if prod=='5':
                    d.pop(max(d.keys()))
                    break
        elif optiune==2:
            for i,j in d.items():
                print(i,j)
            prod_s=int(input("Insert the key of the deleted item: "))
            d.pop(prod_s)
        elif optiune==3:
            d.clear()
        elif optiune==9:
            print("Good bye!")
            break

lista_c()