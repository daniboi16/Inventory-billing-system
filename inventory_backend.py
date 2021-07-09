import os
import datetime
now = datetime.datetime.now()

print(" Welcome to POC system, choose your option:")

while True:
    print(" 1) material sale")
    print(" 2) dress sale")
    print(" 3) material inventory")
    print(" 4) dress inventory")
    print(" 5) exit")
    a=input()

    if (a=="1"):
        material = open("material.csv",'r')
        material_csv_index = material.readlines()
        material_id = int(input("Enter The material ID: "))
        for i in range(1,len(material_csv_index)):
            material_individual = material_csv_index[i].split(',')
            material_found_id = int(material_individual[0])
            if material_found_id == material_id:    
                print(material_individual)
                material_bought = input("Enter the length bought")
                material.seek(0)
                break
            else:
                print("invalid ID")
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
        os.remove("material.csv")
        os.rename("material_temp.csv","material.csv")
        
    elif (a=="2"):
        dress = open("dress.csv",'r')
        dress_csv_index = dress.readlines()
        dress_id = int(input("enter the id for the dress"))
        for i in range(1,len(dress_csv_index)):
            dress_individual = dress_csv_index[i].split(',')
            dress_found_id = int(dress_individual[0])
            if dress_found_id == dress_id:
                print(dress_individual)
                Y = input("confirm buy ? Y/N")
                break
        if Y != "N":
            dress.seek(0)
            dress_temp = open("dress_temp.csv","w")
            dre = dress.readline()
            dress_temp.write(dre)
            for j in range(1,len(dress_csv_index)-2):
                dre = dress.readline()
                dre_individual = dre.split(',')
                
                if int(dre_individual[0]) == dress_found_id:
                    dre_individual[-1] = str(now)+' \n'
                dress_write = str(dre_individual[0]) + "," + str(dre_individual[1]) + "," + str(dre_individual[2]) + "," + str(dre_individual[3]) + "," + str(dre_individual[4])
                dress_temp.write(dress_write)
                print("1")
                    

            
        dress.close()
        dress_temp.close()
        os.remove("dress.csv")
        os.rename("dress_temp.csv","dress.csv")
    elif (a=="3"):
        material = open("material.csv",'r')
        b = material.readlines()
        material.close()
        material_number = len(b)+100
        material = open("material.csv",'a')
        material_name = input("enter name for material")
        material_price = input("enter price for material")
        material_length = input("enter length of material")
        material_list = str(material_number) + "," + str(material_name) + "," + str(material_price) + "," + str(material_length) + ",S \n"
        material.write(material_list)
        material.close()

    elif (a=="4"):
        dress = open("dress.csv",'r')
        a = dress.readlines()
        dress.close()
        dress = open("dress.csv",'a')
        dress_number = len(a)+100
        dress_name = input("enter name for dress")
        dress_price = input("enter price of dress")
        dress_age = input("enter age")
        dress_list = str(dress_number) + "," + str(dress_name) + "," + str(dress_price) + "," + str(dress_age) + ",S \n"
        dress.write(dress_list)
        dress.close()

    elif (a=="5"):
        break

    else:
        print(" invalid option ")
