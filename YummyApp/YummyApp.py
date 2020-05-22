"YummyApp is a food ordering app which was built using tkinter module and data structures (lists and dictionaries)."

from tkinter import *

main_menu=Tk()
main_menu.geometry("720x200")
main_menu.title("YummyApp")
main_menu.config(bg="#ffce63")

main_frame=LabelFrame(main_menu,text="Welcome to YummyApp! What do you want to eat today?",padx=10,pady=20)
main_frame.config(bg="#ffd882")
main_frame.pack()

price_list=[]
product_list=[]

cart_img=PhotoImage(file="cart.png")

def addin(x,y):
    price_list.append(x)
    product_list.append(y)

def minus(k,v):
    if k in price_list and v in product_list:
        price_list.remove(k)
        product_list.remove(v)
    else:
        err_win=Tk()
        err_win.config(bg="#ffd882")
        lbl1=Label(err_win,text="\n\""+v+"\""+" is not in the cart!\n",bg="#ffd882",fg="#e60000")
        lbl1.pack()

def drink():
    global drinks_win
    drinks_win=Toplevel()
    drinks_win.title("Non-Alcoholic Drinks")
    drinks_win.geometry("400x800")
    drinks_win.config(bg="#ffce63")

    drinks_frame=LabelFrame(drinks_win,padx=30,pady=5)
    drinks_frame.config(bg="#ffd882")
    drinks_frame.pack()

    coke_img = PhotoImage(file="coke.png")
    coke_img_lbl=Label(drinks_frame,image=coke_img,bg="#ffd882")

    coke0_img=PhotoImage(file="coke0.png")
    coke0_img_lbl=Label(drinks_frame,image=coke0_img,bg="#ffd882")

    fanta_img=PhotoImage(file="fanta.png")
    fanta_img_lbl=Label(drinks_frame,image=fanta_img,bg="#ffd882")

    sprite_img=PhotoImage(file="sprite.png")
    sprite_img_lbl=Label(drinks_frame,image=sprite_img,bg="#ffd882")

    water_img=PhotoImage(file="s_water.png")
    water_img_lbl=Label(drinks_frame,image=water_img,bg="#ffd882")

    m_water_img=PhotoImage(file="m_water.png")
    m_water_img_lbl=Label(drinks_frame,image=m_water_img,bg="#ffd882")

    blank_lbl1=Label(drinks_frame,text="",padx=10,bg="#ffd882")
    blank_lbl2=Label(drinks_frame,text="",padx=5,bg="#ffd882")
    blank_lbl3=Label(drinks_frame,text="",padx=30,bg="#ffd882")

    coke_lbl=Label(drinks_frame,text="Coke - 3$",bg="#ffd882")
    coke_btn = Button(drinks_frame,text='+',command=lambda: addin(3,"Coke"),bg="#f2e8ae")
    coke_minus_btn = Button(drinks_frame,text="-",command=lambda: minus(3,"Coke"),bg="#f2e8ae")
    coke0_lbl=Label(drinks_frame,text="Coke Zero - 3.5$",bg="#ffd882")
    coke0_btn=Button(drinks_frame,text="+",command=lambda :addin(3.5,"Coke Zero"),bg="#f2e8ae")
    coke0_minus_btn=Button(drinks_frame,text="-",command=lambda: minus(3.5,"Coke Zero"),bg="#f2e8ae")
    fanta_lbl=Label(drinks_frame,text="Fanta - 2.5$",bg="#ffd882")
    fanta_btn = Button(drinks_frame,text='+',command=lambda: addin(2.5,"Fanta"),bg="#f2e8ae")
    fanta_minus_btn = Button(drinks_frame, text="-", command=lambda: minus(2.5, "Fanta"),bg="#f2e8ae")
    sprite_lbl=Label(drinks_frame,text="Sprite - 2.5$",bg="#ffd882")
    sprite_btn=Button(drinks_frame,text="+",command=lambda: addin(2.5,"Sprite"),bg="#f2e8ae")
    sprite_minus_btn = Button(drinks_frame, text="-", command=lambda: minus(2.5, "Sprite"),bg="#f2e8ae")
    water_lbl=Label(drinks_frame,text="Still water - 1$",bg="#ffd882")
    water_btn= Button(drinks_frame,text="+",command=lambda:addin(1,"Still water"),bg="#f2e8ae")
    water_minus_btn = Button(drinks_frame, text="-", command=lambda: minus(1,"Still water"),bg="#f2e8ae")
    m_water_lbl = Label(drinks_frame, text="Mineral water - 1.5$",bg="#ffd882")
    m_water_btn = Button(drinks_frame, text="+", command=lambda: addin(1.5, "Mineral water"),bg="#f2e8ae")
    m_water_minus_btn = Button(drinks_frame, text="-", command=lambda: minus(1.5, "Mineral water"),bg="#f2e8ae")

    see_cart_d=Button(drinks_frame,image=cart_img,command=see,bg="#f2e8ae")

    coke_img_lbl.grid(row=0,column=0)
    coke_lbl.grid(row=1, column=0)
    blank_lbl1.grid(row=1,column=1)
    coke_minus_btn.grid(row=1, column=2)
    blank_lbl2.grid(row=1,column=3)
    coke_btn.grid(row=1,column=4)

    coke0_img_lbl.grid(row=2,column=0)
    coke0_lbl.grid(row=3, column=0)
    coke0_minus_btn.grid(row=3, column=2)
    coke0_btn.grid(row=3, column=4)

    fanta_img_lbl.grid(row=4,column=0)
    fanta_lbl.grid(row=5, column=0)
    fanta_minus_btn.grid(row=5, column=2)
    fanta_btn.grid(row=5, column=4)

    sprite_img_lbl.grid(row=6,column=0)
    sprite_lbl.grid(row=7, column=0)
    sprite_minus_btn.grid(row=7, column=2)
    sprite_btn.grid(row=7, column=4)

    water_img_lbl.grid(row=8,column=0)
    water_lbl.grid(row=9,column=0)
    water_minus_btn.grid(row=9,column=2)
    water_btn.grid(row=9,column=4)

    m_water_img_lbl.grid(row=10,column=0)
    m_water_lbl.grid(row=11, column=0)
    m_water_minus_btn.grid(row=11, column=2)
    m_water_btn.grid(row=11, column=4)

    blank_lbl3.grid(row=0,column=5)
    see_cart_d.grid(row=0, column=6)

    drinks_win.mainloop()

def alc_drinks():
    global alc_win
    alc_win=Toplevel()
    alc_win.geometry("400x800")
    alc_win.title("Alcoholic Drinks")
    alc_win.config(bg="#ffce63")

    alc_drinks_frame=LabelFrame(alc_win,padx=30,pady=10)
    alc_drinks_frame.config(bg="#ffd882")
    alc_drinks_frame.pack()

    beer_img = PhotoImage(file="beer.png")
    beer_img_lbl = Label(alc_drinks_frame, image=beer_img,bg="#ffd882")

    wine_img = PhotoImage(file="wine.png")
    wine_img_lbl = Label(alc_drinks_frame, image=wine_img,bg="#ffd882")

    mojito_img = PhotoImage(file="mojito.png")
    mojito_img_lbl = Label(alc_drinks_frame, image=mojito_img,bg="#ffd882")

    whiskey_img = PhotoImage(file="whiskey.png")
    whiskey_img_lbl = Label(alc_drinks_frame, image=whiskey_img,bg="#ffd882")

    vdk_img = PhotoImage(file="vodka.png")
    vdk_img_lbl = Label(alc_drinks_frame, image=vdk_img,bg="#ffd882")

    blank_lbl1 = Label(alc_drinks_frame, text="", padx=10,bg="#ffd882")
    blank_lbl2 = Label(alc_drinks_frame, text="", padx=5,bg="#ffd882")
    blank_lbl3 = Label(alc_drinks_frame, text="",padx=10,bg="#ffd882")

    beer_lbl = Label(alc_drinks_frame, text="Beer - 4$",bg="#ffd882")
    beer_btn = Button(alc_drinks_frame, text='+', command=lambda: addin(4, "Beer"),bg="#f2e8ae")
    beer_minus_btn = Button(alc_drinks_frame, text='-', command=lambda: minus(4, "Beer"),bg="#f2e8ae")
    wine_lbl = Label(alc_drinks_frame,text="Wine - 5$",bg="#ffd882")
    wine_btn= Button(alc_drinks_frame,text="+",command=lambda:addin(5,"Wine"),bg="#f2e8ae")
    wine_minus_btn= Button(alc_drinks_frame,text="-",command=lambda:minus(5,"Wine"),bg="#f2e8ae")
    mojito_lbl = Label(alc_drinks_frame, text="Mojito - 5.5$",bg="#ffd882")
    mojito_btn = Button(alc_drinks_frame, text="+", command=lambda: addin(5.5, "Mojito"),bg="#f2e8ae")
    mojito_minus_btn = Button(alc_drinks_frame, text="-", command=lambda: minus(5.5, "Mojito"),bg="#f2e8ae")
    whiskey_lbl = Label(alc_drinks_frame,text="Whiskey - 7$",bg="#ffd882")
    whiskey_btn= Button(alc_drinks_frame,text="+",command=lambda: addin(7,"Whiskey"),bg="#f2e8ae")
    whiskey_minus_btn= Button(alc_drinks_frame,text="-",command=lambda: minus(7,"Whiskey"),bg="#f2e8ae")
    vdk_lbl = Label(alc_drinks_frame, text="Vodka - 6$",bg="#ffd882")
    vdk_btn = Button(alc_drinks_frame, text="+", command=lambda: addin(6, "Vodka"),bg="#f2e8ae")
    vdk_minus_btn = Button(alc_drinks_frame, text="-", command=lambda: minus(6, "Vodka"),bg="#f2e8ae")
    see_cart_ad = Button(alc_drinks_frame, image=cart_img, command=see,bg="#f2e8ae")

    beer_img_lbl.grid(row=0,column=0)
    beer_lbl.grid(row=1, column=0)
    blank_lbl1.grid(row=1, column=1)
    beer_minus_btn.grid(row=1, column=2)
    blank_lbl2.grid(row=1, column=3)
    beer_btn.grid(row=1, column=4)

    wine_img_lbl.grid(row=2,column=0)
    wine_lbl.grid(row=3, column=0)
    wine_minus_btn.grid(row=3, column=2)
    wine_btn.grid(row=3, column=4)

    mojito_img_lbl.grid(row=4,column=0)
    mojito_lbl.grid(row=5, column=0)
    mojito_minus_btn.grid(row=5, column=2)
    mojito_btn.grid(row=5, column=4)

    whiskey_img_lbl.grid(row=6,column=0)
    whiskey_lbl.grid(row=7, column=0)
    whiskey_minus_btn.grid(row=7, column=2)
    whiskey_btn.grid(row=7, column=4)

    vdk_img_lbl.grid(row=8,column=0)
    vdk_lbl.grid(row=9, column=0)
    vdk_minus_btn.grid(row=9, column=2)
    vdk_btn.grid(row=9, column=4)

    blank_lbl3.grid(row=0, column=5)
    see_cart_ad.grid(row=0, column=6)

    alc_win.mainloop()

def pizzap():
    global pizza_win
    pizza_win = Toplevel()
    pizza_win.geometry("700x800")
    pizza_win.title("Pizza & Pasta")
    pizza_win.config(bg="#ffce63")

    pp_frame=LabelFrame(pizza_win,padx=30,pady=12)
    pp_frame.config(bg="#ffd882")
    pp_frame.pack()

    blank_lbl1 = Label(pp_frame, text="", padx=10,bg="#ffd882")
    blank_lbl2 = Label(pp_frame, text="", padx=5,bg="#ffd882")
    blank_lbl3 = Label(pp_frame, text="",padx=50,bg="#ffd882")
    blank_lbl4 = Label(pp_frame, text="",padx=10,bg="#ffd882")
    blank_lbl5=Label(pp_frame,text="",padx=5,bg="#ffd882")

    pizza_m_img=PhotoImage(file="pizza_m.png")
    pizza_m_img_lbl=Label(pp_frame,image=pizza_m_img,bg="#ffd882")

    pizza_c_img=PhotoImage(file="pizza_c.png")
    pizza_c_img_lbl=Label(pp_frame,image=pizza_c_img,bg="#ffd882")

    pizza_pr_f_img=PhotoImage(file="pizza_pr_f.png")
    pizza_pr_f_img_lbl=Label(pp_frame,image=pizza_pr_f_img,bg="#ffd882")

    pizza_v_img=PhotoImage(file="pizza_v.png")
    pizza_v_img_lbl=Label(pp_frame,image=pizza_v_img,bg="#ffd882")

    pizza_4f_img=PhotoImage(file="pizza_4f.png")
    pizza_4f_img_lbl=Label(pp_frame,image=pizza_4f_img,bg="#ffd882")

    pizza_4s_img=PhotoImage(file="pizza_4s.png")
    pizza_4s_img_lbl=Label(pp_frame,image=pizza_4s_img,bg="#ffd882")

    pizza_m_lbl = Label(pp_frame, text="Pizza Margherita - 7.5$",bg="#ffd882")
    pizza_m_btn = Button(pp_frame, text='+', command=lambda: addin(7.5, "Pizza Margherita"),bg="#f2e8ae")
    pizza_m_minus_btn = Button(pp_frame, text='-', command=lambda: minus(7.5, "Pizza Margherita"),bg="#f2e8ae")
    pizza_ch_lbl = Label(pp_frame, text="Pizza Carnivora - 8.5$",bg="#ffd882")
    pizza_ch_btn = Button(pp_frame, text="+", command=lambda: addin(8.5, "Pizza Carnivora"),bg="#f2e8ae")
    pizza_ch_minus_btn = Button(pp_frame, text="-", command=lambda: minus(8.5, "Pizza Carnivora"),bg="#f2e8ae")
    pizza_pr_f_lbl = Label(pp_frame, text="Pizza Prosciuto e Funghi - 8.5$",bg="#ffd882")
    pizza_pr_f_btn = Button(pp_frame, text="+", command=lambda: addin(8.5, "Pizza Prosciuto e Funghi"),bg="#f2e8ae")
    pizza_pr_f_minus_btn = Button(pp_frame, text="-", command=lambda: minus(8.5, "Pizza Prosciuto e Funghi"),bg="#f2e8ae")
    pizza_v_lbl = Label(pp_frame, text="Pizza Vegan - 8$",bg="#ffd882")
    pizza_v_btn = Button(pp_frame, text="+", command=lambda: addin(8, "Pizza Vegan"),bg="#f2e8ae")
    pizza_v_minus_btn = Button(pp_frame, text="-", command=lambda: minus(8, "Pizza Vegan"),bg="#f2e8ae")
    pizza_4f_lbl = Label(pp_frame, text="Pizza Quattro Formaggi- 9$",bg="#ffd882")
    pizza_4f_btn = Button(pp_frame, text="+", command=lambda: addin(9, "Pizza Quattro Formaggi"),bg="#f2e8ae")
    pizza_4f_minus_btn = Button(pp_frame, text="-", command=lambda: minus(9, "Pizza Quattro Formaggi"),bg="#f2e8ae")
    pizza_4s_lbl = Label(pp_frame, text="Pizza Quattro Stagioni- 8.5$",bg="#ffd882")
    pizza_4s_btn = Button(pp_frame, text="+", command=lambda: addin(8.5, "Pizza Quattro Stagioni"),bg="#f2e8ae")
    pizza_4s_minus_btn = Button(pp_frame, text="-", command=lambda: minus(8.5, "Pizza Quattro Stagioni"),bg="#f2e8ae")

    see_cart_pp = Button(pp_frame, image=cart_img, command=see,bg="#f2e8ae")
    pizzap_ing_btn=Button(pp_frame,text="Ingredients",command=show_pizza_ing,width=15,pady=7,bg="#f2e8ae")

    carbonara_img=PhotoImage(file="carbonara.png")
    carbonara_img_lbl=Label(pp_frame,image=carbonara_img,bg="#ffd882")

    bolognese_img=PhotoImage(file="bolognese.png")
    bolognese_img_lbl=Label(pp_frame,image=bolognese_img,bg="#ffd882")

    arrabiata_img=PhotoImage(file="arrabbiata.png")
    arrabiata_img_lbl=Label(pp_frame,image=arrabiata_img,bg="#ffd882")

    napolitana_img=PhotoImage(file="napolitana.png")
    napolitana_img_lbl=Label(pp_frame,image=napolitana_img,bg="#ffd882")

    pasta_c_lbl = Label(pp_frame, text="Spaghetti Carbonara - 8.5$",bg="#ffd882")
    pasta_c_btn = Button(pp_frame, text='+', command=lambda: addin(8.5, "Spaghetti Carbonara"),bg="#f2e8ae")
    pasta_c_minus_btn = Button(pp_frame, text='-', command=lambda: minus(8.5, "Spaghetti Carbonara"),bg="#f2e8ae")
    pasta_b_lbl = Label(pp_frame, text="Spaghetti Bolognese - 9$",bg="#ffd882")
    pasta_b_btn = Button(pp_frame, text="+", command=lambda: addin(8.5, "Spaghetti Bolognese"),bg="#f2e8ae")
    pasta_b_minus_btn = Button(pp_frame, text="-", command=lambda: minus(8.5, "Spaghetti Bolognese"),bg="#f2e8ae")
    pasta_a_lbl = Label(pp_frame, text="Spaghetti Arrabiata - 11.5$",bg="#ffd882")
    pasta_a_btn = Button(pp_frame, text="+", command=lambda: addin(11.5, "Spaghetti Arrabiata"),bg="#f2e8ae")
    pasta_a_minus_btn = Button(pp_frame, text="-", command=lambda: minus(11.5, "Spaghetti Arrabiata"),bg="#f2e8ae")
    pasta_n_lbl = Label(pp_frame, text="Spaghetti Napolitana - 10$",bg="#ffd882")
    pasta_n_btn = Button(pp_frame, text="+", command=lambda: addin(10, "Spaghetti Napolitana"),bg="#f2e8ae")
    pasta_n_minus_btn = Button(pp_frame, text="-", command=lambda: minus(10, "Spaghetti Napolitana"),bg="#f2e8ae")

    pizza_m_img_lbl.grid(row=0,column=0)
    pizza_m_lbl.grid(row=1, column=0)
    blank_lbl1.grid(row=1, column=1)
    pizza_m_minus_btn.grid(row=1, column=2)
    blank_lbl2.grid(row=1, column=3)
    pizza_m_btn.grid(row=1, column=4)

    pizza_c_img_lbl.grid(row=2,column=0)
    pizza_ch_lbl.grid(row=3, column=0)
    pizza_ch_minus_btn.grid(row=3, column=2)
    pizza_ch_btn.grid(row=3, column=4)

    pizza_pr_f_img_lbl.grid(row=4,column=0)
    pizza_pr_f_lbl.grid(row=5, column=0)
    pizza_pr_f_minus_btn.grid(row=5, column=2)
    pizza_pr_f_btn.grid(row=5, column=4)

    pizza_v_img_lbl.grid(row=6,column=0)
    pizza_v_lbl.grid(row=7, column=0)
    pizza_v_minus_btn.grid(row=7, column=2)
    pizza_v_btn.grid(row=7, column=4)

    pizza_4f_img_lbl.grid(row=8,column=0)
    pizza_4f_lbl.grid(row=9, column=0)
    pizza_4f_minus_btn.grid(row=9, column=2)
    pizza_4f_btn.grid(row=9, column=4)

    pizza_4s_img_lbl.grid(row=10,column=0)
    pizza_4s_lbl.grid(row=11, column=0)
    pizza_4s_minus_btn.grid(row=11, column=2)
    pizza_4s_btn.grid(row=11, column=4)

    blank_lbl3.grid(row=0, column=5)

    carbonara_img_lbl.grid(row=0,column=6)
    pasta_c_lbl.grid(row=1, column=6)
    blank_lbl4.grid(row=1, column=7)
    pasta_c_minus_btn.grid(row=1, column=8)
    blank_lbl5.grid(row=1, column=9)
    pasta_c_btn.grid(row=1, column=10)

    bolognese_img_lbl.grid(row=2,column=6)
    pasta_b_lbl.grid(row=3, column=6)
    pasta_b_minus_btn.grid(row=3, column=8)
    pasta_b_btn.grid(row=3, column=10)

    arrabiata_img_lbl.grid(row=4,column=6)
    pasta_a_lbl.grid(row=5, column=6)
    pasta_a_minus_btn.grid(row=5, column=8)
    pasta_a_btn.grid(row=5, column=10)

    napolitana_img_lbl.grid(row=6,column=6)
    pasta_n_lbl.grid(row=7, column=6)
    pasta_n_minus_btn.grid(row=7, column=8)
    pasta_n_btn.grid(row=7, column=10)

    pizzap_ing_btn.grid(row=9, column=6)
    see_cart_pp.grid(row=9, column=7)

    pizza_win.mainloop()

def burgers():
    global burgers_win
    burgers_win=Toplevel()
    burgers_win.geometry("450x800")
    burgers_win.title("Burgers")
    burgers_win.config(bg="#ffce63")

    burgers_frame=LabelFrame(burgers_win,padx=10,pady=7)
    burgers_frame.config(bg="#ffd882")
    burgers_frame.pack()
    blank_lbl1 = Label(burgers_frame, text="", padx=10,bg="#ffd882")
    blank_lbl2 = Label(burgers_frame, text="", padx=5,bg="#ffd882")
    blank_lbl3 = Label(burgers_frame, text="", padx=15,bg="#ffd882")

    classicb_img=PhotoImage(file="classic_burger.png")
    classicb_img_lbl=Label(burgers_frame,image=classicb_img,bg="#ffd882")

    italianb_img=PhotoImage(file="italian_burger.png")
    italianb_img_lbl=Label(burgers_frame,image=italianb_img,bg="#ffd882")

    cheeseb_img=PhotoImage(file="cheeseburger.png")
    cheeseb_img_lbl=Label(burgers_frame,image=cheeseb_img,bg="#ffd882")

    doublecheeseb_img=PhotoImage(file="doublecheeseburger.png")
    doublecheeseb_img_lbl=Label(burgers_frame,image=doublecheeseb_img,bg="#ffd882")

    chickenb_img=PhotoImage(file="chickenburger.png")
    chickenb_img_lbl=Label(burgers_frame,image=chickenb_img,bg="#ffd882")

    fries_img=PhotoImage(file="fries.png")
    fries_img_lbl=Label(burgers_frame,image=fries_img,bg="#ffd882")

    burger1_lbl = Label(burgers_frame, text="Classic Burger - 8$",bg="#ffd882")
    burger1_btn = Button(burgers_frame, text='+', command=lambda: addin(8, "Classic Burger"),bg="#f2e8ae")
    burger1_minus_btn = Button(burgers_frame, text='-', command=lambda: minus(8, "Classic Burger"),bg="#f2e8ae")

    burger2_lbl = Label(burgers_frame, text="Italian Burger - 8.5$",bg="#ffd882")
    burger2_btn = Button(burgers_frame, text='+', command=lambda: addin(8.5, "Italian Burger"),bg="#f2e8ae")
    burger2_minus_btn = Button(burgers_frame, text='-', command=lambda: minus(8.5, "Italian Burger"),bg="#f2e8ae")

    burger3_lbl = Label(burgers_frame, text="Cheeseburger - 8$",bg="#ffd882")
    burger3_btn = Button(burgers_frame, text='+', command=lambda: addin(8, "Cheeseburger"),bg="#f2e8ae")
    burger3_minus_btn = Button(burgers_frame, text='-', command=lambda: minus(8, "Cheeseburger"),bg="#f2e8ae")

    burger4_lbl = Label(burgers_frame, text="Double Cheeseburger - 9$",bg="#ffd882")
    burger4_btn = Button(burgers_frame, text='+', command=lambda: addin(9, "Double Cheeseburger"),bg="#f2e8ae")
    burger4_minus_btn = Button(burgers_frame, text='-', command=lambda: minus(9, "Double Cheeseburger"),bg="#f2e8ae")

    burger5_lbl = Label(burgers_frame, text="Chicken Burger - 7.5$",bg="#ffd882")
    burger5_btn = Button(burgers_frame, text='+', command=lambda: addin(7.5, "Chicken Burger"),bg="#f2e8ae")
    burger5_minus_btn = Button(burgers_frame, text='-', command=lambda: minus(7.5, "Chicken Burger"),bg="#f2e8ae")

    fries_lbl = Label(burgers_frame, text="Fries - 4$",bg="#ffd882")
    fries_btn = Button(burgers_frame, text='+', command=lambda: addin(4, "Fries"),bg="#f2e8ae")
    fries_minus_btn = Button(burgers_frame, text='-', command=lambda: minus(4, "Fries"),bg="#f2e8ae")

    burgers_ing_btn=Button(burgers_frame,text="Ingredients",command=show_burgers_ing,width=15,pady=7,bg="#f2e8ae")
    see_cart_bg= Button(burgers_frame,image=cart_img,command=see,bg="#f2e8ae")

    classicb_img_lbl.grid(row=0,column=0)
    burger1_lbl.grid(row=1, column=0)
    blank_lbl1.grid(row=1,column=1)
    burger1_minus_btn.grid(row=1, column=2)
    blank_lbl2.grid(row=1,column=3)
    burger1_btn.grid(row=1, column=4)

    italianb_img_lbl.grid(row=2 ,column=0)
    burger2_lbl.grid(row=3, column=0)
    burger2_minus_btn.grid(row=3, column=2)
    burger2_btn.grid(row=3, column=4)

    cheeseb_img_lbl.grid(row=4 ,column=0)
    burger3_lbl.grid(row=5, column=0)
    burger3_minus_btn.grid(row=5, column=2)
    burger3_btn.grid(row=5, column=4)

    doublecheeseb_img_lbl.grid(row=6 ,column=0)
    burger4_lbl.grid(row=7, column=0)
    burger4_minus_btn.grid(row=7, column=2)
    burger4_btn.grid(row=7, column=4)

    chickenb_img_lbl.grid(row=8 ,column=0)
    burger5_lbl.grid(row=9, column=0)
    burger5_minus_btn.grid(row=9, column=2)
    burger5_btn.grid(row=9, column=4)

    fries_img_lbl.grid(row=10,column=0)
    fries_lbl.grid(row=11, column=0)
    fries_minus_btn.grid(row=11, column=2)
    fries_btn.grid(row=11, column=4)

    blank_lbl3.grid(row=0,column=5)

    see_cart_bg.grid(row=0, column=6)
    burgers_ing_btn.grid(row=1,column=6)


    burgers_win.mainloop()

def sauces():
    global sauces_win
    sauces_win=Toplevel()
    sauces_win.geometry("400x700")
    sauces_win.title("Sauces")
    sauces_win.config(bg="#ffce63")

    sauces_frame=LabelFrame(sauces_win,padx=20,pady=25)
    sauces_frame.config(bg="#ffd882")
    sauces_frame.pack()

    blank_lbl1 = Label(sauces_frame, text="", padx=10,bg="#ffd882")
    blank_lbl2 = Label(sauces_frame, text="", padx=5,bg="#ffd882")
    blank_lbl3 = Label(sauces_frame, text="", padx=20,bg="#ffd882")

    ketchup_img=PhotoImage(file="ketchup.png")
    ketchup_img_lbl=Label(sauces_frame,image=ketchup_img,bg="#ffd882")

    s_ketchup_img = PhotoImage(file="s_ketchup.png")
    s_ketchup_img_lbl = Label(sauces_frame, image=s_ketchup_img,bg="#ffd882")

    mayo_img = PhotoImage(file="mayo.png")
    mayo_img_lbl = Label(sauces_frame, image=mayo_img,bg="#ffd882")

    bbq_img = PhotoImage(file="bbq.png")
    bbq_img_lbl = Label(sauces_frame, image=bbq_img,bg="#ffd882")

    samurai_img = PhotoImage(file="samurai.png")
    samurai_img_lbl = Label(sauces_frame, image=samurai_img,bg="#ffd882")

    sauce1_lbl=Label(sauces_frame,text="Ketchup - 1$",bg="#ffd882")
    sauce1_btn=Button(sauces_frame,text="+",command=lambda:addin(1,"Ketchup"),bg="#f2e8ae")
    sauce1_minus_btn = Button(sauces_frame, text="-", command=lambda: minus(1,"Ketchup"),bg="#f2e8ae")
    sauce2_lbl = Label(sauces_frame, text="Spicy ketchup - 1.5$",bg="#ffd882")
    sauce2_btn = Button(sauces_frame, text="+", command=lambda: addin(1.5, "Spicy ketchup"),bg="#f2e8ae")
    sauce2_minus_btn = Button(sauces_frame, text="-", command=lambda: minus(1.5, "Spicy ketchup"),bg="#f2e8ae")
    sauce3_lbl = Label(sauces_frame, text="Mayonnaise - 1$",bg="#ffd882")
    sauce3_btn = Button(sauces_frame, text="+", command=lambda: addin(1, "Mayonnaise"),bg="#f2e8ae")
    sauce3_minus_btn = Button(sauces_frame, text="-", command=lambda: minus(1, "Mayonnaise"),bg="#f2e8ae")
    sauce4_lbl = Label(sauces_frame, text="BBQ sauce - 2$",bg="#ffd882")
    sauce4_btn = Button(sauces_frame, text="+", command=lambda: addin(2, "BBQ sauce"),bg="#f2e8ae")
    sauce4_minus_btn = Button(sauces_frame, text="-", command=lambda: minus(2, "BBQ sauce"),bg="#f2e8ae")
    sauce5_lbl = Label(sauces_frame, text="Samurai sauce - 2.5$",bg="#ffd882")
    sauce5_btn = Button(sauces_frame, text="+", command=lambda: addin(2.5, "Samourai sauce"),bg="#f2e8ae")
    sauce5_minus_btn = Button(sauces_frame, text="-", command=lambda: minus(2.5, "Samourai sauce"),bg="#f2e8ae")
    see_cart_sauces = Button(sauces_frame,image=cart_img,command=see,bg="#f2e8ae")

    ketchup_img_lbl.grid(row=0,column=0)
    sauce1_lbl.grid(row=1, column=0)
    blank_lbl1.grid(row=1,column=1)
    sauce1_minus_btn.grid(row=1, column=2)
    blank_lbl2.grid(row=1,column=3)
    sauce1_btn.grid(row=1, column=4)

    s_ketchup_img_lbl.grid(row=2,column=0)
    sauce2_lbl.grid(row=3, column=0)
    sauce2_minus_btn.grid(row=3, column=2)
    sauce2_btn.grid(row=3, column=4)

    mayo_img_lbl.grid(row=4,column=0)
    sauce3_lbl.grid(row=5, column=0)
    sauce3_minus_btn.grid(row=5, column=2)
    sauce3_btn.grid(row=5, column=4)

    bbq_img_lbl.grid(row=6,column=0)
    sauce4_lbl.grid(row=7, column=0)
    sauce4_minus_btn.grid(row=7, column=2)
    sauce4_btn.grid(row=7, column=4)

    samurai_img_lbl.grid(row=8,column=0)
    sauce5_lbl.grid(row=9, column=0)
    sauce5_minus_btn.grid(row=9, column=2)
    sauce5_btn.grid(row=9, column=4)

    blank_lbl3.grid(row=0,column=5)
    see_cart_sauces.grid(row=0, column=6)

    sauces_win.mainloop()

def see():
    cart_win=Toplevel()
    cart_win.title("Cart")
    cart_win.config(bg="#ffd882")
    global prod_count
    prod_count={i:product_list.count(i) for i in product_list}
    total=sum(price_list)
    prod_lbl=Label(cart_win,text="Your products: {}".format(prod_count),bg="#ffd882")
    price_lbl=Label(cart_win,text="Total price: {}$".format(total),bg="#ffd882")
    prod_lbl.pack()
    price_lbl.pack()

def show_pizza_ing():
    global pizza_ing
    pizza_ing=Toplevel()
    pizza_ing.title("Pizza & Pasta Ingredients")
    pizza_ing.geometry("550x450")
    pizza_ing.config(bg="#ffd882")
    pizza_ing_lbl=Label(pizza_ing,bg="#ffd882",text="\n********** PIZZA **********"
                                       "\n\nPizza Margherita -> Tomato sauce, mozzarella, olive oil"
                                       "\n\nPizza Carnivora -> Tomato sauce, mozzarella, smoked prosciuto, beef jerky, bacon"
                                       "\n\nPizza Prosciutto e Funghi -> Tomato sauce, mozzarella, mushrooms, prosciutto cotto"
                                       "\n\nPizza Vegan -> Tomato sauce, vegan parmesan cheese, mushrooms, garlic pouder, oregano"
                                       "\n\nPizza Quattro Formaggi -> Tomato sauce, provolone, parmesan cheese, gruyere, pecorino"
                                       "\n\nPizza Quattro Stagioni -> Tomato sauce, mozzarella, olives, mushrooms, prosciutto, bacon"
                                       "\n\n\n\n********** PASTA **********"
                                       "\n\nSpaghetti Carbonara -> Spaghetti, parmesan, bacon, pepper"
                                       "\n\nSpaghetti Bolognese -> Spaghetti, meat sauce, chopped onions, cherry tomatoes, dried oregano"
                                       "\n\nSpaghetti Arrabiata -> Spaghetti, tomato sauce, oregano,parmesan cheese, tomatoes"
                                       "\n\nSpaghetti Napolitana -> Spaghetti, parmesan, buffalo mozzarella, granted parmesan")
    pizza_ing_lbl.pack()
def show_burgers_ing():
    global burgers_ing
    burgers_ing=Toplevel()
    burgers_ing.title("Burgers Ingredients")
    burgers_ing.geometry("550x200")
    burgers_ing.config(bg="#ffd882")
    burgers_ing_lbl=Label(burgers_ing,bg="#ffd882",text="\nClassic Burger -> Burger buns, ketchup, beef, mozzarella, rucola, pesto"
                                           "\n\nItalian Burger -> Burger buns, ketchup, lettuce, beef, tomatoes, red onion, pickles"
                                           "\n\nCheeseburger -> Burger buns, ketchup, lettuce, beef, Gouda cheese, tomatoes, red onion"
                                           "\n\nDouble Cheeseburger -> Burger buns, ketchup, 2x beef, 2x Gouda cheese, red onion, pickles"
                                           "\n\nChicken Burger -> Burger buns, ketchup Coleslaw salad, crispy chicken, Gouda cheese, pickles")
    burgers_ing_lbl.pack()

def reset():
    product_list.clear()
    price_list.clear()

drinks_btn = Button(main_frame,text="Drinks",command=drink,width=12,pady=5,bg="#f2e8ae")
alcohold_btn = Button(main_frame,text="Alcoholic drinks",command=alc_drinks,width=12,pady=5,bg="#f2e8ae")
pizzap_btn = Button(main_frame,text="Pizza & Pasta",command=pizzap,width=12,pady=5,bg="#f2e8ae")
burgers_btn= Button(main_frame,text="Burgers & Fries",command=burgers,width=12,pady=5,bg="#f2e8ae")
sauces_btn = Button(main_frame,text="Sauces",command=sauces,width=12,pady=5,bg="#f2e8ae")

cart_btn=Button(main_frame,image=cart_img,command=see,bg="#f2e8ae")
reset_btn=Button(main_frame,text="Reset cart",command=reset,pady=5,bg="#f2e8ae")

blank_lbl1=Label(main_frame,text="",pady=5,bg="#ffd882")
blank_lbl2=Label(main_frame,text="",padx=5,bg="#ffd882")
blank_lbl3=Label(main_frame,text="",padx=5,bg="#ffd882")
blank_lbl4=Label(main_frame,text="",padx=5,bg="#ffd882")
blank_lbl5=Label(main_frame,text="",padx=5,bg="#ffd882")
blank_lbl6=Label(main_frame,text="",padx=5,bg="#ffd882")
blank_lbl7=Label(main_frame,text="",pady=5,bg="#ffd882")


blank_lbl1.grid(row=1,column=0)
drinks_btn.grid(row=1,column=1)
blank_lbl2.grid(row=1,column=2)
alcohold_btn.grid(row=1,column=3)
blank_lbl3.grid(row=1,column=4)
pizzap_btn.grid(row=1,column=5)
blank_lbl4.grid(row=1,column=6)
burgers_btn.grid(row=1,column=7)
blank_lbl5.grid(row=1,column=8)
sauces_btn.grid(row=1,column=9)
blank_lbl6.grid(row=2,column=10)

reset_btn.grid(row=3,column=10)
cart_btn.grid(row=3,column=11,padx=5)

main_menu.mainloop()