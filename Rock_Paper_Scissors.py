"""This is a Rock Paper Scissors game. When it starts, it shows a window in which the users can choose if they
want to play vs. Computer or vs. another player. It was built using random and tkinter modules."""

import random
from tkinter import *

window_choice=Tk()
window_choice.title("Rock Paper Scissors")
window_choice.geometry("450x200")
window_choice.config(bg="#c49000")
lbl=Label(window_choice,text="Welcome to Rock Paper Scissors!\nChoose an option down below to continue.", bg="#c49000",fg="white")
lbl.config(font=("Fixedsys",13))
lbl.pack()
blank_lbl1=Label(window_choice,bg="#c49000")

option_entry=Entry(window_choice,width=10000,bg="#f56c42",show=" ")
option_entry.pack()
blank_lbl1.pack()

def first_choice(c):
    option_entry.delete(0,END)
    option_entry.insert(0, c)
    if option_entry.get() == "computer":
        #window_choice.destroy()
        window = Tk()
        window.geometry("400x600")
        window.title("RPS - Player vs Computer")
        window.config(bg="#c49000")
        option = Entry(window,width=10000,bg="#f56c42",fg="white")
        option.config(font=("Fixedsys",12))
        option.pack()

        def who_wins(button_choice):

            option.delete(0, END)
            option.insert(0, button_choice.title())
            l = ["Rock", "Paper", "Scissors"]

            choice = random.choice(l)
            o = option.get().title()

            show_choice = Label(window, text=choice.title(), bg="#c49000")
            show_choice.config(font=("Fixedsys", 10))
            show_choice.pack()
            if choice == o:
                result = Label(window, text="Tie!", bg="#c49000", fg="white")
                result.config(font=("Fixedsys", 15))
                result.pack()
            elif choice == "Rock" and o == "Paper":
                result = Label(window, text="You won!", bg="#c49000", fg="#40ff00")
                result.config(font=("Fixedsys", 15))
                result.pack()
            elif choice == "Rock" and o == "Scissors":
                result = Label(window, text="You lost!", bg="#c49000", fg="#ff0000")
                result.config(font=("Fixedsys", 15))
                result.pack()
            elif choice == "Paper" and o == "Rock":
                result = Label(window, text="You lost!", bg="#c49000", fg="#ff0000")
                result.config(font=("Fixedsys", 15))
                result.pack()
            elif choice == "Paper" and o == "Scissors":
                result = Label(window, text="You won!", bg="#c49000", fg="#40ff00")
                result.config(font=("Fixedsys", 15))
                result.pack()
            elif choice == "Scissors" and o == "Rock":
                result = Label(window, text="You won!", bg="#c49000", fg="#40ff00")
                result.config(font=("Fixedsys", 15))
                result.pack()
            elif choice == "Scissors" and o == "Paper":
                result = Label(window, text="You lost!", bg="#c49000", fg="#ff0000")
                result.config(font=("Fixedsys", 15))
                result.pack()

        btn1 = Button(window, text="Rock", width=10, command=lambda: who_wins("rock"), bg="#38535e", fg="white")
        btn1.config(font=("Fixedsys", 10))
        btn2 = Button(window, text="Paper", width=10, command=lambda: who_wins("paper"), bg="#8affb9")
        btn2.config(font=("Fixedsys", 10))
        btn3 = Button(window, text="Scissors", width=10, command=lambda: who_wins("scissors"), bg="#cc0000", fg="white")
        btn3.config(font=("Fixedsys", 10))

        btn1.pack()
        btn2.pack()
        btn3.pack()
        window.mainloop()

    elif option_entry.get() == "1v1":
        #window_choice.destroy()
        window_1v1=Tk()
        window_1v1.title("RPS - Player vs Player")
        window_1v1.geometry("400x600")
        window_1v1.config(bg="#c49000")
        ent1=Entry(window_1v1,show=" ",width=10000,bg="#f56c42")
        ent2=Entry(window_1v1,show=" ",width=10000,bg="#f56c42")

        ent1.pack()
        ent2.pack()

        def p1_choice(c1):
            ent1.delete(0, END)
            ent1.insert(0, c1)
        def p2_choice(c2):
            ent2.delete(0, END)
            ent2.insert(0, c2)

        def show():
            if ent1.get()=="" and ent2.get()=="":
                no_choice1=Label(window_1v1,text="No choices!",bg="#c49000",fg="#cc0000")
                no_choice1.config(font=("Fixedsys", 13))
                no_choice1.pack()
            elif ent1.get()=="":
                no_choice2 = Label(window_1v1, text="Player1 did not choose!", bg="#c49000", fg="#cc0000")
                no_choice2.config(font=("Fixedsys", 13))
                no_choice2.pack()
            elif ent2.get()=="":
                no_choice3 = Label(window_1v1, text="Player2 did not choose!", bg="#c49000", fg="#cc0000")
                no_choice3.config(font=("Fixedsys", 13))
                no_choice3.pack()
            else:
                lbl1 = Label(window_1v1, text="Player1 chose: "+str(ent1.get().title()),bg="#c49000",fg="#7c00b5")
                lbl1.config(font=("Fixedsys",13))
                lbl2 = Label(window_1v1, text="Player2 chose: "+str(ent2.get().title()),bg="#c49000",fg="#7c00b5")
                lbl2.config(font=("Fixedsys", 13))
                lbl1.pack()
                lbl2.pack()

        def who_wins2():
            player1 = ent1.get()
            player2 = ent2.get()
            if player1 == player2:
                if player1=="" and player2=="":
                    pass
                else:
                    result_1v1 = Label(window_1v1, text="Tie!", bg="#c49000", fg="white")
                    result_1v1.config(font=("Fixedsys", 15))
                    result_1v1.pack()
            elif player1 == "rock" and player2 == "paper":
                result_1v1 = Label(window_1v1, text="Player2 wins!", bg="#c49000", fg="white")
                result_1v1.config(font=("Fixedsys", 15))
                result_1v1.pack()
            elif player1 == "rock" and player2 == "scissors":
                result_1v1 = Label(window_1v1, text="Player1 wins!", bg="#c49000", fg="white")
                result_1v1.config(font=("Fixedsys", 15))
                result_1v1.pack()
            elif player1 == "paper" and player2 == "rock":
                result_1v1 = Label(window_1v1, text="Player1 wins!", bg="#c49000", fg="white")
                result_1v1.config(font=("Fixedsys", 15))
                result_1v1.pack()
            elif player1 == "paper" and player2 == "scissors":
                result_1v1 = Label(window_1v1, text="Player2 wins!", bg="#c49000", fg="white")
                result_1v1.config(font=("Fixedsys", 15))
                result_1v1.pack()
            elif player1 == "scissors" and player2 == "rock":
                result_1v1 = Label(window_1v1, text="Player2 wins!", bg="#c49000", fg="white")
                result_1v1.config(font=("Fixedsys", 15))
                result_1v1.pack()
            elif player1 == "scissors" and player2 == "paper":
                result_1v1 = Label(window_1v1, text="Player1 wins!", bg="#c49000", fg="white")
                result_1v1.config(font=("Fixedsys", 15))
                result_1v1.pack()

        btn1_p1 = Button(window_1v1,text="Rock",command=lambda: p1_choice("rock"), bg="#38535e",width=10,fg="white")
        btn1_p1.config(font=("Fixedsys", 10))
        btn2_p1 = Button(window_1v1, text="Paper", command=lambda: p1_choice("paper"), bg="#8affb9",width=10)
        btn2_p1.config(font=("Fixedsys", 10))
        btn3_p1 = Button(window_1v1, text="Scissors", command=lambda: p1_choice("scissors"), bg="#cc0000",width=10,fg="white")
        btn3_p1.config(font=("Fixedsys", 10))
        btn1_p2 = Button(window_1v1, text="Rock", command=lambda: p2_choice("rock"), bg="#38535e",width=10,fg="white")
        btn1_p2.config(font=("Fixedsys", 10))
        btn2_p2 = Button(window_1v1, text="Paper", command=lambda: p2_choice("paper"), bg="#8affb9",width=10)
        btn2_p2.config(font=("Fixedsys", 10))
        btn3_p2 = Button(window_1v1, text="Scissors", command=lambda: p2_choice("scissors"), bg="#cc0000",width=10,fg="white")
        btn3_p2.config(font=("Fixedsys", 10))
        who_won = Button(window_1v1,text="Who wins?",command=who_wins2,bg="#f56c42",fg="white",width=10,pady=10)
        who_won.config(font=("Fixedsys", 10))
        show_btn = Button(window_1v1, text="Show choices", command=show,bg="#f56c42",fg="white",width=12)
        show_btn.config(font=("Fixedsys", 10))
        blank_lbl2=Label(window_1v1,text="Player1:",bg="#c49000",fg="white")
        blank_lbl2.config(font=("Fixedsys",13))
        blank_lbl3 = Label(window_1v1,text="Player2:", bg="#c49000",fg="white")
        blank_lbl3.config(font=("Fixedsys", 13))
        blank_lbl4 = Label(window_1v1, bg="#c49000")
        blank_lbl5 = Label(window_1v1, bg="#c49000")

        blank_lbl2.pack()
        btn1_p1.pack()
        btn2_p1.pack()
        btn3_p1.pack()

        blank_lbl3.pack()
        btn1_p2.pack()
        btn2_p2.pack()
        btn3_p2.pack()

        blank_lbl4.pack()

        who_won.pack()
        blank_lbl5.pack()
        show_btn.pack()

        window_1v1.mainloop()

btn_choice1=Button(window_choice,text="Play vs Computer",command=lambda:first_choice("computer"),bg="#f56c42",fg="white")
btn_choice1.config(font=("Fixedsys", 10))
btn_choice1.pack()

btn_choice2=Button(window_choice,text="Play 1v1",command=lambda:first_choice("1v1"),bg="#f56c42",fg="white")
btn_choice2.config(font=("Fixedsys", 10))
btn_choice2.pack()

window_choice.mainloop()