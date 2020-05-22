"""This is a program in which you can enter certain data such as name,
measure unit, quantity and the date when a product enters or exits the
deposit . It sends a warning email when the stock needs to be
restocked."""

from datetime import datetime

class Stoc:

    def __init__(self, prod, categ,um='Buc', sold=0, lim=5,pret=0):
        self.prod = prod
        self.categ = categ
        self.sold = sold
        self.um = um
        self.lim = lim
        self.pret = pret
        self.i = {}
        self.e = {}
        self.d = {}

    def intr(self, cant, data=str(datetime.now().strftime('%Y%m%d'))):
        self.data = data
        self.cant = cant
        self.sold += cant
        if self.d.keys():
            cheie = max(self.d.keys()) + 1
        else:
            cheie = 1
        self.i[cheie] = cant
        self.d[cheie] = self.data

    def iesi(self, cant, data=str(datetime.now().strftime('%Y%m%d'))):
        self.data = data
        self.cant = cant
        self.sold -= self.cant
        if self.d.keys():
            cheie = max(self.d.keys()) + 1
        else:
            cheie = 1
        self.e[cheie] = self.cant
        self.d[cheie] = self.data

    def fisap(self):

        print('Product info ' + self.prod + ': ' + self.um)
        print(40 * '-')
        print(' Nrc ', '  Data ', 'Enters', 'Exits')
        print(40 * '-')
        for v in self.d.keys():
            if v in self.i.keys():
                print(str(v).rjust(5), self.d[v], str(self.i[v]).rjust(6), str(0).rjust(6))
            else:
                print(str(v).rjust(5), self.d[v], str(0).rjust(6), str(self.e[v]).rjust(6))
        print(40 * '-')
        print('Actual stock:      ' + str(self.sold).rjust(10))
        print(40 * '-' + '\n')

    def exp(self,datap=str(datetime.now().strftime('%Y%m%d'))):
        self.datap=datap
        from datetime import date
        today = date.today()
        if self.datap<str(today):
            print("The product has expierd.")
        else:
            print("The product has not expired.")

    def profit(self):
        self.cheltuieli=0
        self.venit=0
        for k in self.i:
            self.cheltuieli=self.pret*self.i[k]
        for j in self.e:
            self.venit=self.pret*self.e[j]
        if self.cheltuieli>self.venit:
            print("You are at a loss of",self.pret,"€")
        elif self.cheltuieli<self.venit:
            print("You are on a profit of",self.pret,"€")
        else:
            print("Expenses are equal to income. 0 profit and 0 loss")

strawberries = Stoc('strawberries', 'fruits', 'kg', 5, 4)  # cream instantele clasei
milk = Stoc('milk', 'diary prod', 'liter', 5, 4,3)
watches = Stoc('watches', 'watches')
milk.intr(2,"2020-01-01")
milk.iesi(3,"2020-01-02")
milk.exp("2020-01-01")
milk.profit()

lst = [strawberries, milk, watches]
for i in lst:
    try:
        if i.sold < i.lim:
            print("The stock of", i.prod, "is under limit."
                                          " Insert the following data to send a warning:")
            import smtplib

            expeditor = "Adrian"
            destinatar = input("Insert the recipient's email: ")
            username = input("Insert your email: ")
            parola = input("Insert your password: ")
            mesaj = "The stock of {} is under limit! Please restock!".format(i.prod)
            smtp_ob = smtplib.SMTP('smtp.gmail.com', 587)  #
            smtp_ob.starttls()
            smtp_ob.login(username, parola)
            smtp_ob.sendmail(expeditor, destinatar, mesaj)
            print("Sent!")

    except:
        print('The message could\'t be sent!')

import re

l=[strawberries,milk,watches]
den_p = input("Type the product you want to search for: ")
w=den_p.lower()
nr=0
for i in l:
    if re.search(w,i.prod):
        nr+=1
if nr==1:
    print("\"",w,"\" is in deposit.")
else:
    print("\"",w,"\" isn't in deposit.")


