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
#window.attributes('-fullscreen', True)

#displaying date
l_date = tk.Label(window, text=current_date, font="medium", bd=10, bg="#C9E4CA")
l_date.grid(row=1, rowspan =1, column=1, columnspan = 1, padx=10)

#displaying title
l_pintucks = tk.Label(window, text = "PINTUCKS", font="BOLT", bd=20, bg="orange", width=80)
l_pintucks.grid(row=1, rowspan =2, column=3, columnspan = 9, padx=10)

#displaying exit button
def exitfunction():
    global window
    window.destroy()
b_exit = tk.Button(window, text= " EXIT ", bg="#f24444", activebackground="red", relief="raised", padx=25, pady=15,  font ="medium", bd=10, command = exitfunction)
b_exit.grid(row=1, rowspan =1, column=12, columnspan = 1, padx=30)

def dresssale():
    return

def materialsale():
    global l1_mat
    l1_mat = tk.Label(window, text= "Enter the ID", width= 15, height=2, font="medium")
    l1_mat.grid(row=10, rowspan =2, column=4, columnspan = 4, padx=10, pady=10)
    global e1_mat
    e1_mat = tk.Entry(window, width=9, font="medium" )
    e1_mat.grid(row=10, rowspan =2, column=7, columnspan = 4, padx=10, pady=10)
    global b1_mat
    b1_mat = tk.Button(window, text = " OK ", command = okaybox1_mat, bd=5, relief="raised")
    b1_mat.grid(row=10, rowspan =2, column=10, columnspan = 1, padx=10, pady=10)

def okaybox1_mat():
    global material
    material = open("material.csv",'r')
    global material_csv_index
    material_csv_index = material.readlines()
    material_id = int(e1_mat.get())
    for i in range(1,len(material_csv_index)):
        material_individual = material_csv_index[i].split(',')
        global material_found_id
        material_found_id = int(material_individual[0])
        if material_found_id == material_id:
            global l12_mat
            global l13_mat
            global l14_mat
            global l15_mat
            global l16_mat
            l12_mat = tk.Label(window, text = "ID   =  " +str(material_individual[0]),  width= 14, height=2, font="medium")
            l12_mat.grid(row=15, rowspan =1, column=1, columnspan = 1, padx=10, pady=10)
            l13_mat = tk.Label(window, text = "NAME   =  " +str(material_individual[1]),  width= 14, height=2, font="medium")
            l13_mat.grid(row=16, rowspan =1, column=1, columnspan = 1, padx=10, pady=10)
            l14_mat = tk.Label(window, text = "PRICE   =  " +str(material_individual[2]),  width= 14, height=2, font="medium")
            l14_mat.grid(row=17, rowspan =1, column=1, columnspan = 1, padx=10, pady=10)
            l15_mat = tk.Label(window, text = "LENGTH   =  " +str(material_individual[3]),  width= 14, height=2, font="medium")
            l15_mat.grid(row=18, rowspan =1, column=1, columnspan = 1, padx=10, pady=10)
            l16_mat = tk.Label(window, text = "STATUS   =  " +str(material_individual[4]),  width= 14, height=2, font="medium")
            l16_mat.grid(row=19, rowspan =1, column=1, columnspan = 1, padx=10, pady=10)

            global l11_mat
            l11_mat = tk.Label(window, text= "Enter the length bought", width= 20, height=2, font="medium")
            l11_mat.grid(row=12, rowspan =2, column=4, columnspan = 3, padx=10, pady=10)
            global e11_mat
            e11_mat = tk.Entry(window, width=9, font="medium" )
            e11_mat.grid(row=12, rowspan =2, column=7, columnspan = 1, padx=10, pady=10)
            global b11_mat
            b11_mat = tk.Button(window, text = " OK ", command = okaybox11_mat, bd=5, relief="raised")
            b11_mat.grid(row=12, rowspan =2, column=10, columnspan = 1, padx=10, pady=10)
            break
    
def okaybox11_mat():
    material_bought=e11_mat.get()
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
    l1_mat.grid_forget()
    e1_mat.grid_forget()
    b1_mat.grid_forget()
    l11_mat.grid_forget()
    e11_mat.grid_forget()
    b11_mat.grid_forget()
    l12_mat.grid_forget()
    l13_mat.grid_forget()
    l14_mat.grid_forget()
    l15_mat.grid_forget()
    l16_mat.grid_forget()

def ordersale():
    return

def advancesale():
    return

def okaybox1():
    cust_name = e_name.get()
    cust_phone = e_phone.get()
    l_name.grid_forget()
    l_phone.grid_forget()
    e_name.grid_forget()
    e_phone.grid_forget()
    b_ok1.grid_forget()
    
    b_sale1 = tk.Button(window, text = "DRESS", command = dresssale, bd=10, bg="#87BBA2", activebackground="#fb91ff", relief="raised", font ="BOLT")
    b_sale1.grid(row=5, rowspan =2, column=1, columnspan = 3, ipadx=60, padx=20, ipady=20, pady =20)
    b_sale2 = tk.Button(window, text = "MATERIAL", command = materialsale, bd=10, bg="#87BBA2", activebackground="#fb91ff", relief="raised", font ="BOLT")
    b_sale2.grid(row=5, rowspan =2, column=4, columnspan = 4, ipadx=60, padx=20, ipady=20, pady =20)
    b_sale3 = tk.Button(window, text = "ORDER", command = ordersale, bd=10, bg="#87BBA2", activebackground="#fb91ff", relief="raised", font ="BOLT")
    b_sale3.grid(row=5, rowspan =2, column=7, columnspan = 5, ipadx=60, padx=50, ipady=20, pady =20)
    b_sale4 = tk.Button(window, text = "ADVANCE", command = advancesale, bd=10, bg="#87BBA2", activebackground="#fb91ff", relief="raised", font ="BOLT")
    b_sale4.grid(row=5, rowspan =2, column=11, columnspan = 5, ipadx=60, padx=50, ipady=20, pady =20)
    
    
l_name = tk.Label(window, text = "CUSTOMER NAME :",  width= 25, height=2, font="medium")
l_phone = tk.Label(window, text = "PHONE NUMBER:",  width= 25, height=2, font="medium")
l_name.grid(row=4, rowspan =1, column=5, columnspan = 1, padx=10, pady=10)
l_phone.grid(row=5, rowspan =1, column=5, columnspan = 1, padx=10, pady=10)
e_name = tk.Entry(window, width=25, font="medium")
e_phone = tk.Entry(window, width=25, font="medium")
e_name.grid(row=4, rowspan =1, column=7, columnspan = 1, padx=10, pady=10)
e_phone.grid(row=5, rowspan =1, column=7, columnspan = 1, padx=10, pady=10)
b_ok1 = tk.Button(window, text = " OK ", command = okaybox1, bd=5, relief="raised")
b_ok1.grid(row=5, rowspan =1, column=8, columnspan = 1, padx=10, pady=10)
    











window.mainloop()
