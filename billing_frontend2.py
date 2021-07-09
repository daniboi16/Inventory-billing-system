#final frontend system for the customer billing system
import tkinter as tk
from datetime import datetime
from os import remove,rename

#geting the current date
date_now= datetime.now()
current_date = date_now.strftime("%d %B %Y")

#opening window with name in fullscreen
window = tk.Tk()
window.title("Pintucks POS System")
window.configure(background='#FACAC0')
window.attributes('-fullscreen', True)

#displaying date
l_date = tk.Label(window, text=current_date, font="medium", bd=10, bg="#FACAC0")
l_date.grid(row=1, rowspan=1, column=1, columnspan=1, padx=10, pady=10)

#displaying title
l_pintucks = tk.Label(window, text="PINTUCKS", font="BOLT", bd=20, bg="#F3CFFF", width=81)
l_pintucks.grid(row=1, rowspan=1, column=3, columnspan=10, padx=10, pady=10)

#displaying exit button
def exitfunction():
    global window
    window.destroy()
b_exit = tk.Button(window, text=" EXIT ", bg="#FF8B8B", activebackground="RED", relief="raised", font="BOLT", bd=10, command=exitfunction, padx=25, pady=10)
b_exit.grid(row=1, rowspan=1, column=13, columnspan = 1, padx=10, pady=10)

#################################################################################################################################################
#################################################################################################################################################
#################################################################################################################################################
#################################################################################################################################################
#################################################################################################################################################

def dress_sale():
    global l2_dre,e2_dre,b2_dre
    l2_dre = tk.Label(window, text="Enter the ID", width=20, height=2, font="medium")
    e2_dre = tk.Entry(window, width=15, font="medium" )
    b2_dre = tk.Button(window, text="OK", command=okaybox1_dre, bd=5, relief="raised")
    l2_dre.grid(row=5, rowspan=2, column=3, columnspan=5, padx=10, pady=10)
    e2_dre.grid(row=5, rowspan=2, column=5, columnspan=7, padx=10, pady=10)
    b2_dre.grid(row=5, rowspan=2, column=10, columnspan=1, padx=10, pady=10)

def okaybox1_dre():
    global dress
    dress = open("dress.csv",'r')
    global dress_csv_index
    dress_csv_index = dress.readlines()
    dress_id = int(e2_dre.get())
    for i in range(1,len(dress_csv_index)):
        dress_individual = dress_csv_index[i].split(',')
        global dress_found_id
        dress_found_id = int(dress_individual[0])
        if dress_found_id == dress_id:
            global l23_dre,l24_dre,l25_dre,l26_dre
            l23_dre = tk.Label(window, text="NAME   =  " +str(dress_individual[1]),  width=14, height=2, font="medium")
            l24_dre = tk.Label(window, text="PRICE   =  " +str(dress_individual[2]),  width=14, height=2, font="medium")
            l25_dre = tk.Label(window, text="AGE   =  " +str(dress_individual[3]),  width=14, height=2, font="medium")
            l26_dre = tk.Label(window, text="STATUS   =  " +str(dress_individual[4]),  width=14, height=2, font="medium")

            l23_dre.grid(row=9, rowspan=1, column=3, columnspan=5, padx=10, pady=10)
            l24_dre.grid(row=10, rowspan=1, column=3, columnspan=5, padx=10, pady=10)
            l25_dre.grid(row=11, rowspan=1, column=3, columnspan=5, padx=10, pady=10)
            l26_dre.grid(row=12, rowspan=1, column=3, columnspan=5, padx=10, pady=10)

            global l21_dre,b22_dre
            l21_dre = tk.Label(window, text="Confirm purshase?", width=20, height=2, font="medium")
            b22_dre = tk.Button(window, text=" YES ", command=okaybox22, bd=5, relief="raised")

            l21_dre.grid(row=7, rowspan=2, column=3, columnspan=5, padx=10, pady=10)
            b22_dre.grid(row=7, rowspan=2, column=10, columnspan=1, padx=10, pady=10)
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
            dre_list=[dre_individual[0],dre_individual[1],dre_individual[2],dre_individual[3]]
            list_main.insert(0,dre_list)
            dre_individual[-1] = str(current_date)+' \n'
        dress_write = str(dre_individual[0]) + "," + str(dre_individual[1]) + "," + str(dre_individual[2]) + "," + str(dre_individual[3]) + "," + str(dre_individual[4])
        dress_temp.write(dress_write)
    dress.close()
    dress_temp.close()
    remove("dress.csv")
    rename("dress_temp.csv","dress.csv")


    l2_dre.grid_forget()
    e2_dre.grid_forget()
    b2_dre.grid_forget()
    l21_dre.grid_forget()
    b22_dre.grid_forget()
    l23_dre.grid_forget()
    l24_dre.grid_forget()
    l25_dre.grid_forget()
    l26_dre.grid_forget()

#################################################################################################################################################
#################################################################################################################################################

def material_sale():
    global l1_mat,e1_mat,b1_mat
    l1_mat = tk.Label(window, text= "Enter the ID", width=20, height=2, font="medium")
    e1_mat = tk.Entry(window, width=15, font="medium" )
    b1_mat = tk.Button(window, text = "OK", command = okaybox1_mat, bd=5, relief="raised")

    l1_mat.grid(row=5, rowspan =2, column=3, columnspan=5, padx=10, pady=10)
    e1_mat.grid(row=5, rowspan =2, column=5, columnspan=7, padx=5, pady=10)
    b1_mat.grid(row=5, rowspan =2, column=10, columnspan=1, padx=5, pady=10)

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
            
        

            global l13_mat,l14_mat,l15_mat,l16_mat
            l13_mat = tk.Label(window, text = "NAME   =  " +str(material_individual[1]),  width= 14, height=2, font="medium")
            l14_mat = tk.Label(window, text = "PRICE   =  " +str(material_individual[2]),  width= 14, height=2, font="medium")
            l15_mat = tk.Label(window, text = "LENGTH   =  " +str(material_individual[3]),  width= 14, height=2, font="medium")
            l16_mat = tk.Label(window, text = "STATUS   =  " +str(material_individual[4]),  width= 14, height=2, font="medium")

            l13_mat.grid(row=9, rowspan=1, column=3, columnspan = 5, padx=10, pady=10)
            l14_mat.grid(row=10, rowspan=1, column=3, columnspan = 5, padx=10, pady=10)
            l15_mat.grid(row=11, rowspan=1, column=3, columnspan = 5, padx=10, pady=10)
            l16_mat.grid(row=12, rowspan=1, column=3, columnspan = 5, padx=10, pady=10)

            global l11_mat,e11_mat,b11_mat
            l11_mat = tk.Label(window, text= "Enter the length bought", width= 20, height=2, font="medium")
            e11_mat = tk.Entry(window, width=15, font="medium" )
            b11_mat = tk.Button(window, text = "OK", command = okaybox11_mat, bd=5, relief="raised")

            l11_mat.grid(row=7, rowspan =2, column=3, columnspan=5, padx=10, pady=10)
            e11_mat.grid(row=7, rowspan =2, column=5, columnspan=7, padx=5, pady=10)
            b11_mat.grid(row=7, rowspan =2, column=10, columnspan=1, padx=5, pady=10)
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
            mat_list=[mat_individual[0],mat_individual[1],mat_individual[2],material_bought,int(material_bought)*int(mat_individual[2])]
            list_main.insert(0,mat_list)
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
    l13_mat.grid_forget()
    l14_mat.grid_forget()
    l15_mat.grid_forget()
    l16_mat.grid_forget()


#################################################################################################################################################
#################################################################################################################################################

def order_sale():
    global l31_ord,e31_ord,l32_ord,e32_ord,b31_ord
    l31_ord = tk.Label(window, text= "Enter order number", width=20, height=2, font="medium")
    e31_ord = tk.Entry(window, width=15, font="medium" )
    l32_ord = tk.Label(window, text= "Enter the price", width=20, height=2, font="medium")
    e32_ord = tk.Entry(window, width=15, font="medium" )
    b31_ord = tk.Button(window, text = "OK", command=okaybox3_ord, bd=5, relief="raised")
    
    l31_ord.grid(row=5, rowspan=2, column=3, columnspan=5, padx=10, pady=10)
    e31_ord.grid(row=5, rowspan=2, column=5, columnspan=7, padx=10, pady=10)
    l32_ord.grid(row=7, rowspan=2, column=3, columnspan=5, padx=10, pady=10)
    e32_ord.grid(row=7, rowspan=2, column=5, columnspan=7, padx=10, pady=10)
    b31_ord.grid(row=7, rowspan=2, column=10, columnspan=1, padx=10, pady=10)

def okaybox3_ord():
    order_number=e31_ord.get()
    order_price=e32_ord.get()
    order_list=[order_number,order_price]
    list_main.insert(0,order_list)
    l31_ord.grid_forget()
    e31_ord.grid_forget()
    l32_ord.grid_forget()
    e32_ord.grid_forget()
    b31_ord.grid_forget()
    
#################################################################################################################################################
#################################################################################################################################################

def advance_sale():
    global l41_adv,e41_adv,l42_adv,e42_adv,l43_adv,e43_adv,b41_adv
    l41_adv = tk.Label(window, text= "Enter order number", width=20, height=2, font="medium")
    e41_adv = tk.Entry(window, width=15, font="medium")
    l42_adv = tk.Label(window, text= "Enter due date", width=20, height=2, font="medium")
    e42_adv = tk.Entry(window, width=15, font="medium")
    l43_adv = tk.Label(window, text= "Enter amount", width=20, height=2, font="medium")
    e43_adv = tk.Entry(window, width=15, font="medium")
    b41_adv = tk.Button(window,text="OK", command=okaybox5_adv, bd=5, relief="raised")

    l41_adv.grid(row=5, rowspan=2, column=3, columnspan=5, padx=10, pady=10)
    e41_adv.grid(row=5, rowspan=2, column=5, columnspan=7, padx=10, pady=10)
    l42_adv.grid(row=7, rowspan=2, column=3, columnspan=5, padx=10, pady=10)
    e42_adv.grid(row=7, rowspan=2, column=5, columnspan=7, padx=10, pady=10)
    l43_adv.grid(row=9, rowspan=2, column=3, columnspan=5, padx=10, pady=10)
    e43_adv.grid(row=9, rowspan=2, column=5, columnspan=7, padx=10, pady=10)
    b41_adv.grid(row=9, rowspan=2, column=10, columnspan=1, padx=10, pady=10)

def okaybox5_adv():
    order_number=e41_adv.get()
    order_duedate=e42_adv.get()
    order_amount=e43_adv.get()
    order_list=[order_number,order_duedate,order_amount]
    list_main.insert(0,order_list)
    l41_adv.grid_forget()
    l42_adv.grid_forget()
    l43_adv.grid_forget()
    e41_adv.grid_forget()
    e42_adv.grid_forget()
    e43_adv.grid_forget()
    b41_adv.grid_forget()
    
#################################################################################################################################################
#################################################################################################################################################

def printbill():
    '''
    customer_book = open("customer.csv",'a')
    file_name = str(cust_name)+"_"+str(cust_phone)+".csv"
    current_cust = open(file_name,'w')
    list_main.reverse()
    #customer_book.writelines(list_main)
    #current_cust.write(list_main)
    customer_book.close()
    current_cust.close()
    '''
    print(list_main)
    b_sale1.grid_forget()
    b_sale2.grid_forget()
    b_sale3.grid_forget()
    b_sale4.grid_forget()
    b_sale5.grid_forget()
    customer()

def okaybox1():
    global cust_name,cust_phone
    cust_name = e_name.get()
    cust_phone = e_phone.get()
    list_cust=[cust_name,cust_phone]
    list_main.insert(0,list_cust)
    
    l_name.grid_forget()
    l_phone.grid_forget()
    e_name.grid_forget()
    e_phone.grid_forget()
    b_ok1.grid_forget()
    
    global b_sale1,b_sale2,b_sale3,b_sale4,b_sale5
    b_sale1 = tk.Button(window, text="  DRESS  ", command=dress_sale, bd=10, bg="#0BBCD0", activebackground="LIGHT BLUE", relief="raised", font ="BOLT")
    b_sale2 = tk.Button(window, text="MATERIAL", command=material_sale, bd=10, bg="#0BBCD0", activebackground="LIGHT BLUE", relief="raised", font ="BOLT")
    b_sale3 = tk.Button(window, text="ORDER", command=order_sale, bd=10, bg="#0BBCD0", activebackground="LIGHT BLUE", relief="raised", font ="BOLT")
    b_sale4 = tk.Button(window, text="ADVANCE", command=advance_sale, bd=10, bg="#0BBCD0", activebackground="LIGHT BLUE", relief="raised", font ="BOLT")
    b_sale5 = tk.Button(window, text="  BILL ", command=printbill, bd=10, bg="LIGHT BLUE", activebackground="LIGHT BLUE", relief="raised", font ="BOLT")

    b_sale1.grid(row=3, rowspan=2, column=1, columnspan=3, ipadx=30, padx=20, ipady=20, pady =20)
    b_sale2.grid(row=3, rowspan=2, column=4, columnspan=3, ipadx=30, padx=20, ipady=20, pady =20)
    b_sale3.grid(row=3, rowspan=2, column=7, columnspan=3, ipadx=30, padx=20, ipady=20, pady =20)
    b_sale4.grid(row=3, rowspan=2, column=10, columnspan=3, ipadx=30, padx=20, ipady=20, pady =20)
    b_sale5.grid(row=3, rowspan=2, column=13, columnspan=3, ipadx=18, padx=20, ipady=20, pady =20)

def customer():
    global list_main
    list_main=[]
    global l_name,l_phone,e_name,e_phone,b_ok1
    l_name = tk.Label(window, text = "CUSTOMER NAME :",  width= 25, height=1, font="medium")
    l_phone = tk.Label(window, text = "PHONE NUMBER:",  width= 25, height=1, font="medium")
    e_name = tk.Entry(window, width=25, font="medium")
    e_phone = tk.Entry(window, width=25, font="medium")
    b_ok1 = tk.Button(window, text = " OK ", command = okaybox1, bd=5, relief="raised")

    l_name.grid(row=2, rowspan =1, column=5, columnspan = 3, padx=10, pady=10)
    l_phone.grid(row=3, rowspan =1, column=5, columnspan = 3, padx=10, pady=10)
    e_name.grid(row=2, rowspan =1, column=8, columnspan = 3, padx=10, pady=10)
    e_phone.grid(row=3, rowspan =1, column=8, columnspan = 3, padx=10, pady=10)
    b_ok1.grid(row=3, rowspan =1, column=11, columnspan = 1, padx=10, pady=10)

customer()
window.mainloop()
