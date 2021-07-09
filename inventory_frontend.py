#first edition of the front end system. Adding tkinter to the inventory_backend program
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
btn_exit.grid(row=1, rowspan =1, column=16, columnspan = 1, padx=30)



#for materialsale
def materialsale():
    #forgetentry()
    global l1
    l1 = tk.Label(window, text= "Enter the ID", width= 10, height=2, font="medium")
    l1.grid(row=10, rowspan =2, column=4, columnspan = 3, padx=10, pady=10)
    global e1
    e1 = tk.Entry(window, width=9, font="medium" )
    e1.grid(row=10, rowspan =2, column=7, columnspan = 1, padx=10, pady=10)
    global b1
    b1 = tk.Button(window, text = " OK ", command = okaybox1, bd=5, relief="raised")
    b1.grid(row=10, rowspan =2, column=10, columnspan = 1, padx=10, pady=10)

def okaybox1():
    global material
    material = open("material.csv",'r')
    global material_csv_index
    material_csv_index = material.readlines()
    material_id = int(e1.get())
    for i in range(1,len(material_csv_index)):
        material_individual = material_csv_index[i].split(',')
        global material_found_id
        material_found_id = int(material_individual[0])
        if material_found_id == material_id:
            global l12
            global l13
            global l14
            global l15
            global l16
            l12 = tk.Label(window, text = "ID   =  " +str(material_individual[0]),  width= 14, height=2, font="medium")
            l12.grid(row=4, rowspan =1, column=1, columnspan = 1, padx=10, pady=10)
            l13 = tk.Label(window, text = "NAME   =  " +str(material_individual[1]),  width= 14, height=2, font="medium")
            l13.grid(row=5, rowspan =1, column=1, columnspan = 1, padx=10, pady=10)
            l14 = tk.Label(window, text = "PRICE   =  " +str(material_individual[2]),  width= 14, height=2, font="medium")
            l14.grid(row=6, rowspan =1, column=1, columnspan = 1, padx=10, pady=10)
            l15 = tk.Label(window, text = "LENGTH   =  " +str(material_individual[3]),  width= 14, height=2, font="medium")
            l15.grid(row=7, rowspan =1, column=1, columnspan = 1, padx=10, pady=10)
            l16 = tk.Label(window, text = "STATUS   =  " +str(material_individual[4]),  width= 14, height=2, font="medium")
            l16.grid(row=8, rowspan =1, column=1, columnspan = 1, padx=10, pady=10)

            global l11
            l11 = tk.Label(window, text= "Enter the length bought", width= 20, height=2, font="medium")
            l11.grid(row=12, rowspan =2, column=4, columnspan = 3, padx=10, pady=10)
            global e11
            e11 = tk.Entry(window, width=9, font="medium" )
            e11.grid(row=12, rowspan =2, column=7, columnspan = 1, padx=10, pady=10)
            global b11
            b11 = tk.Button(window, text = " OK ", command = okaybox11, bd=5, relief="raised")
            b11.grid(row=12, rowspan =2, column=10, columnspan = 1, padx=10, pady=10)
            break
    
def okaybox11():
    material_bought=e11.get()
    material.seek(0)
    material_temp = open("material_temp.csv",'w')
    mat = material.readline()
    material_temp.write(mat)
    for i in range(1,len(material_csv_index)):
        mat = material.readline()
        mat_individual = mat.split(',')
        if int(mat_individual[0])== material_found_id:
            new_length=int(mat_individual[3])-int(material_bought)
            if (new_length>0):
                mat_individual[-2] = str(new_length)
            else:
                mat_individual[-2] = '0'
                mat_individual[-1] = 'N \n'
        mat_write = str(mat_individual[0]) + ',' + str(mat_individual[1]) + ',' + str(mat_individual[2]) + ',' + str(mat_individual[3]) + ',' +str(mat_individual[4])
        material_temp.write(mat_write)
    material_temp.close()
    material.close()    
    remove("material.csv")
    rename("material_temp.csv","material.csv")
    l1.grid_forget()
    e1.grid_forget()
    b1.grid_forget()
    l11.grid_forget()
    e11.grid_forget()
    b11.grid_forget()
    l12.grid_forget()
    l13.grid_forget()
    l14.grid_forget()
    l15.grid_forget()
    l16.grid_forget()
    
#for dress sale    
def dresssale():
    global l2
    l2 = tk.Label(window, text= "Enter the ID", width= 10, height=2, font="medium")
    l2.grid(row=10, rowspan =2, column=4, columnspan = 3, padx=10, pady=10)
    global e2
    e2 = tk.Entry(window, width=9, font="medium" )
    e2.grid(row=10, rowspan =2, column=7, columnspan = 1, padx=10, pady=10)
    global b2
    b2 = tk.Button(window, text = " OK ", command = okaybox2, bd=5, relief="raised")
    b2.grid(row=10, rowspan =2, column=10, columnspan = 1, padx=10, pady=10)

def okaybox2():
    global dress
    dress = open("dress.csv",'r')
    global dress_csv_index
    dress_csv_index = dress.readlines()
    dress_id = int(e2.get())
    for i in range(1,len(dress_csv_index)):
        dress_individual = dress_csv_index[i].split(',')
        global dress_found_id
        dress_found_id = int(dress_individual[0])
        if dress_found_id == dress_id:
            global l22
            global l23
            global l24
            global l25
            global l26
            l22 = tk.Label(window, text = "ID   =  " +str(dress_individual[0]),  width= 14, height=2, font="medium")
            l22.grid(row=4, rowspan =1, column=1, columnspan = 1, padx=10, pady=10)
            l23 = tk.Label(window, text = "NAME   =  " +str(dress_individual[1]),  width= 18, height=2, font="medium")
            l23.grid(row=5, rowspan =1, column=1, columnspan = 2, padx=1, pady=10)
            l24 = tk.Label(window, text = "PRICE   =  " +str(dress_individual[2]),  width= 14, height=2, font="medium")
            l24.grid(row=6, rowspan =1, column=1, columnspan = 1, padx=10, pady=10)
            l25 = tk.Label(window, text = "AGE   =  " +str(dress_individual[3]),  width= 14, height=2, font="medium")
            l25.grid(row=7, rowspan =1, column=1, columnspan = 1, padx=10, pady=10)
            l26 = tk.Label(window, text = "STATUS   =  " +str(dress_individual[4]),  width= 22, height=2, font="medium")
            l26.grid(row=8, rowspan =1, column=1, columnspan = 2, padx=1, pady=10)

            print(dress_individual)
            global l21
            l21 = tk.Label(window, text= "Confirm purshase?", width= 20, height=2, font="medium")
            l21.grid(row=12, rowspan =2, column=4, columnspan = 3, padx=10, pady=10)
            global b22
            b22 = tk.Button(window, text = " YES ", command = okaybox22, bd=5, relief="raised")
            b22.grid(row=12, rowspan =2, column=10, columnspan = 1, padx=10, pady=10)
            break

def okaybox22():
    dress.seek(0)
    dress_temp = open("dress_temp.csv","w")
    dre = dress.readline()
    dress_temp.write(dre)
    for j in range(1,len(dress_csv_index)):
        dre = dress.readline()
        dre_individual = dre.split(',')
        if int(dre_individual[0]) == dress_found_id:
            dre_individual[-1] = str(current_date)+' \n'
        dress_write = str(dre_individual[0]) + "," + str(dre_individual[1]) + "," + str(dre_individual[2]) + "," + str(dre_individual[3]) + "," + str(dre_individual[4])
        dress_temp.write(dress_write)
    dress.close()
    dress_temp.close()
    remove("dress.csv")
    rename("dress_temp.csv","dress.csv")


    l2.grid_forget()
    e2.grid_forget()
    b2.grid_forget()
    l21.grid_forget()
    b22.grid_forget()
    l22.grid_forget()
    l23.grid_forget()
    l24.grid_forget()
    l25.grid_forget()
    l26.grid_forget()
    
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
    
def dressinventory():
    global l41
    l41 = tk.Label(window, text= "Enter name:", width= 15, height=2, font="medium")
    l41.grid(row=12, rowspan =2, column=4, columnspan = 3, padx=10, pady=10)
    global e41
    e41 = tk.Entry(window, width=15, font="medium" )
    e41.grid(row=12, rowspan =2, column=7, columnspan = 1, padx=10, pady=10)
    global l42
    l42 = tk.Label(window, text= "Enter price:", width= 15, height=2, font="medium")
    l42.grid(row=13, rowspan =2, column=4, columnspan = 3, padx=10, pady=10)
    global e42
    e42 = tk.Entry(window, width=15, font="medium" )
    e42.grid(row=13, rowspan =2, column=7, columnspan = 1, padx=10, pady=10)
    global l43
    l43 = tk.Label(window, text= "Enter age:", width= 15, height=2, font="medium")
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

'''

'''


btn1 = tk.Button(window, text = " Material Sale ", command = materialsale, bd=10, bg="#87BBA2", activebackground="#609ffc", relief="raised", font ="BOLT")
btn2 = tk.Button(window, text = " Dress Sale ", command = dresssale, bd=10, bg="#87BBA2", activebackground="#609ffc", relief="raised", font ="BOLT")
btn3 = tk.Button(window, text = " Material Inventory ", command = materialinventory, bd=10, bg="#87BBA2", activebackground="#fb91ff", relief="raised", font ="BOLT")
btn4 = tk.Button(window, text = " Dress Inventory ", command = dressinventory, bd=10, bg="#87BBA2", activebackground="#fb91ff", relief="raised", font ="BOLT")

btn1.grid(row=4, rowspan =2, column=4, columnspan = 3, ipadx=70, padx=50, ipady=20, pady =20)
btn2.grid(row=4, rowspan =2, column=10, columnspan = 3, ipadx=70, padx=50, ipady=20, pady =20)
btn3.grid(row=7, rowspan =2, column=4, columnspan = 3, ipadx=50, padx=50, ipady=20, pady =20)
btn4.grid(row=7, rowspan =2, column=10, columnspan = 3, ipadx=50, padx=50, ipady=20, pady =20)

window.mainloop()
