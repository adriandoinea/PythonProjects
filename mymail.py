"""This is a GUI program that allows the users to send an email from their gmail account to any email platform.
It also shows a message if the email has been sent or an error if the email couldn't be sent.
The program was built using tkinter and smtplib modules"""

import smtplib
from tkinter import *

win = Tk()
win.configure(bg="#233b30")
win.geometry("600x500")
win.title("MyMail")

detail=LabelFrame(win,text="Hello! Enter your information down below to send an email",pady=20,bg="#233b30",fg="#b8e9ff")
detail.config(font=("Comic Sans MS",13,"italic"))
detail.pack()

m_mail=Label(detail,text="Input your email adress (gmail only) ",bg="#233b30",fg="#b8e9ff")
m_mail.config(font=("Comic Sans MS",10))
m_mail.grid(row=0,column=0)

passw=Label(detail,text="Input your password",bg="#233b30",fg="#b8e9ff")
passw.config(font=("Comic Sans MS",10))
passw.grid(row=1,column=0)

r_mail=Label(detail,text="Input the recipient's email adress",bg="#233b30",fg="#b8e9ff")
r_mail.config(font=("Comic Sans MS",10))
r_mail.grid(row=2,column=0)

msg=Label(detail,text="Message:",bg="#233b30",fg="#b8e9ff")
msg.config(font=("Comic Sans MS",10))
msg.grid(row=3,column=0)

m=Entry(detail,width=40,bg="#b8e9ff",fg="#00012b")
m.config(font=("Comic Sans MS",10))
m.grid(row=0,column=1)

p=Entry(detail,show="*",width=40,bg="#b8e9ff",fg="#00012b")
p.config(font=("Comic Sans MS",10))
p.grid(row=1,column=1)

r=Entry(detail,width=40,bg="#b8e9ff",fg="#00012b")
r.config(font=("Comic Sans MS",10))
r.grid(row=2,column=1)

mg=Entry(detail,width=40,bg="#b8e9ff",fg="#00012b")
mg.config(font=("Comic Sans MS",10))
mg.grid(row=3,column=1,padx=10)

def send():
    try:
        smtp_ob = smtplib.SMTP('smtp.gmail.com', 587)
        smtp_ob.starttls()
        smtp_ob.login(m.get(), p.get())
        smtp_ob.sendmail(m.get(), r.get(), mg.get())
        win.destroy()
        win1=Tk()
        win1.geometry("400x100")
        win1.configure(bg="#233b30")
        win1.title("MyMail")
        snt=Label(win1,text="Your message has been sent!",pady=50,fg="#b8e9ff",bg="#233b30")
        snt.config(font=("Comic Sans MS",12))
        snt.pack()
    except:
        win.destroy()
        win2=Tk()
        win2.geometry("400x100")
        win2.title("MyMail")
        win2.configure(bg="#233b30")
        err=Label(win2,text="Couldn't send the message! Try again later.",pady=50,fg="#ff2929",bg="#233b30")
        err.config(font=("Comic Sans MS",12))
        err.pack()

btn=Button(detail,text="SEND!",command=send,bg="#8fa87b",fg="#00012b")
btn.config(font=("Comic Sans MS",10))
btn.grid(row=5,column=1,pady=30)
win.mainloop()