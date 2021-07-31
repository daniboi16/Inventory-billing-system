import tkinter as tk
from datetime import datetime
from os import remove,rename

#geting the current date
date_now= datetime.now()
current_date = date_now.strftime("%d %B %Y")

#opening window with name in fullscreen
window = tk.Tk()
window.title("Pintucks POS System")
window.configure(background='#C9E4CA')
window.attributes('-fullscreen', True)

#displaying date
date_lable = tk.Label(window, text=current_date, font="medium", bd=10, bg="#C9E4CA")
date_lable.grid(row=1, rowspan =1, column=1, columnspan = 1, padx=20)

#displaying title
title_pintucks = tk.Label(window, text = "PINTUCKS", font="BOLT", bd=20, bg="orange", width=65)
title_pintucks.grid(row=1, rowspan =2, column=4, columnspan = 8, padx=80)

#displaying exit button
def exitfunction():
    global window
    window.destroy()
btn_exit = tk.Button(window, text= " EXIT ", bg="#f24444", activebackground="red", relief="raised", padx=25, pady=15,  font ="medium", bd=10, command = exitfunction)
btn_exit.grid(row=1, rowspan =1, column=14, columnspan = 1, padx=30)

#material inventory    
def materialinventory():
    global l31
    l31 = tk.Label(window, text= "Enter name:", width= 15, height=2, font="medium")
    l31.grid(row=12, rowspan =2, column=4, columnspan = 3, padx=10, pady=10)
    global e31
    e31 = tk.Entry(window, width=15, font="medium" )
    e31.grid(row=12, rowspan =2, column=7, columnspan = 1, padx=10, pady=10)
    global l32
    l32 = tk.Label(window, text= "Enter price:", width= 15, height=2, font="medium")
    l32.grid(row=13, rowspan =2, column=4, columnspan = 3, padx=10, pady=10)
    global e32
    e32 = tk.Entry(window, width=15, font="medium" )
    e32.grid(row=13, rowspan =2, column=7, columnspan = 1, padx=10, pady=10)
    global l33
    l33 = tk.Label(window, text= "Enter length:", width= 15, height=2, font="medium")
    l33.grid(row=14, rowspan =2, column=4, columnspan = 3, padx=10, pady=10)
    global e33
    e33 = tk.Entry(window, width=15, font="medium" )
    e33.grid(row=14, rowspan =2, column=7, columnspan = 1, padx=10, pady=10)
    global b31
    b31 = tk.Button(window, text = " OK ", command = okaybox3, bd=5, relief="raised")
    b31.grid(row=14, rowspan =2, column=10, columnspan = 1, padx=10, pady=10)
    
def okaybox3():
    material = open("material.csv",'r')
    b = material.readlines()
    material.close()
    material_number = len(b)+100
    material = open("material.csv",'a')
    material_name = e31.get()
    material_price = e32.get()
    material_length = e33.get()
    material_list = str(material_number) + "," + str(material_name) + "," + str(material_price) + "," + str(material_length) + ",S \n"
    material.write(material_list)
    material.close()

    l31.grid_forget()
    e31.grid_forget()
    l32.grid_forget()
    e32.grid_forget()
    l33.grid_forget()
    e33.grid_forget()
    b31.grid_forget()

    global l34,l35,l36,l37,b32
    l34 = tk.Label(window, text = "ID   =  " +str(material_number),  width= 14, height=2, font="medium")
    l34.grid(row=4, rowspan =1, column=1, columnspan = 1, padx=10, pady=10)
    l35 = tk.Label(window, text = "NAME   =  " +str(material_name),  width= 18, height=2, font="medium")
    l35.grid(row=5, rowspan =1, column=1, columnspan = 2, padx=1, pady=10)
    l36 = tk.Label(window, text = "PRICE   =  " +str(material_price),  width= 14, height=2, font="medium")
    l36.grid(row=6, rowspan =1, column=1, columnspan = 1, padx=10, pady=10)
    l37 = tk.Label(window, text = "LENGTH   =  " +str(material_length),  width= 14, height=2, font="medium")
    l37.grid(row=7, rowspan =1, column=1, columnspan = 1, padx=10, pady=10)
    b32 = tk.Button(window, text = " OK ", command = okaybox33, bd=5, relief="raised")
    b32.grid(row=8, rowspan =2, column=1, columnspan = 1, padx=10, pady=10)

def okaybox33():
    l34.grid_forget()
    l35.grid_forget()
    l36.grid_forget()
    l37.grid_forget()
    b32.grid_forget()

#dress inventory    
def dressinventory():
    global l41
    l41 = tk.Label(window, text= "Enter name:", width= 10, height=2, font="medium")
    l41.grid(row=12, rowspan =2, column=4, columnspan = 3, padx=10, pady=10)
    global e41
    e41 = tk.Entry(window, width=15, font="medium" )
    e41.grid(row=12, rowspan =2, column=7, columnspan = 1, padx=10, pady=10)
    global l42
    l42 = tk.Label(window, text= "Enter price:", width= 10, height=2, font="medium")
    l42.grid(row=13, rowspan =2, column=4, columnspan = 3, padx=10, pady=10)
    global e42
    e42 = tk.Entry(window, width=15, font="medium" )
    e42.grid(row=13, rowspan =2, column=7, columnspan = 1, padx=10, pady=10)
    global l43
    l43 = tk.Label(window, text= "Enter age:", width= 10, height=2, font="medium")
    l43.grid(row=14, rowspan =2, column=4, columnspan = 3, padx=10, pady=10)
    global e43
    e43 = tk.Entry(window, width=15, font="medium" )
    e43.grid(row=14, rowspan =2, column=7, columnspan = 1, padx=10, pady=10)
    global b41
    b41 = tk.Button(window, text = " OK ", command = okaybox4, bd=5, relief="raised")
    b41.grid(row=14, rowspan =2, column=10, columnspan = 1, padx=10, pady=10)

def okaybox4():
    dress = open("dress.csv",'r')
    a = dress.readlines()
    dress.close()
    dress = open("dress.csv",'a')
    dress_number = len(a)+100
    dress_name = e41.get()
    dress_price = e42.get()
    dress_age = e43.get()
    dress_list = str(dress_number) + "," + str(dress_name) + "," + str(dress_price) + "," + str(dress_age) + ",S \n"
    dress.write(dress_list)
    dress.close()
    l41.grid_forget()
    e41.grid_forget()
    l42.grid_forget()
    e42.grid_forget()
    l43.grid_forget()
    e43.grid_forget()
    b41.grid_forget()
    global l44,l45,l46,l47,b42
    l44 = tk.Label(window, text = "ID   =  " +str(dress_number),  width= 14, height=2, font="medium")
    l44.grid(row=4, rowspan =1, column=1, columnspan = 1, padx=10, pady=10)
    l45 = tk.Label(window, text = "NAME   =  " +str(dress_name),  width= 18, height=2, font="medium")
    l45.grid(row=5, rowspan =1, column=1, columnspan = 2, padx=1, pady=10)
    l46 = tk.Label(window, text = "PRICE   =  " +str(dress_price),  width= 14, height=2, font="medium")
    l46.grid(row=6, rowspan =1, column=1, columnspan = 1, padx=10, pady=10)
    l47 = tk.Label(window, text = "AGE   =  " +str(dress_age),  width= 14, height=2, font="medium")
    l47.grid(row=7, rowspan =1, column=1, columnspan = 1, padx=10, pady=10)
    b42 = tk.Button(window, text = " OK ", command = okaybox44, bd=5, relief="raised")
    b42.grid(row=8, rowspan =2, column=1, columnspan = 1, padx=10, pady=10)

def okaybox44():
    l44.grid_forget()
    l45.grid_forget()
    l46.grid_forget()
    l47.grid_forget()
    b42.grid_forget()




btn3 = tk.Button(window, text = " Material Inventory ", command = materialinventory, bd=10, bg="#87BBA2", activebackground="#fb91ff", relief="raised", font ="BOLT")
btn4 = tk.Button(window, text = " Dress Inventory ", command = dressinventory, bd=10, bg="#87BBA2", activebackground="#fb91ff", relief="raised", font ="BOLT")

btn3.grid(row=4, rowspan =2, column=4, columnspan = 3, ipadx=50, padx=50, ipady=20, pady =20)
btn4.grid(row=4, rowspan =2, column=10, columnspan = 3, ipadx=50, padx=50, ipady=20, pady =20)

window.mainloop()
