import os
import datetime
now = datetime.datetime.now()
while (True):
    name=input("enter name")
    number=input("enter phone number")
    s=0;
    d=[]
    while(s==0):
        print("1)dress sale")
        print("2)material sale")
        print("3) custom")
        print("4) print bill")
        a=int(input())
        if (a==1):
            dress_id=int(input("enter dress id"))
            dress = open("dress.csv",'r')
            dress_csv_index = dress.readlines()
            for i in range(1,len(dress_csv_index)):
                dress_individual = dress_csv_index[i].split(',')
                dress_found_id = int(dress_individual[0])
                if dress_found_id == dress_id:
                    dress_list=[dress_individual[0],dress_individual[1],dress_individual[2],1,dress_individual[2]]
                    d.insert(0,dress_list)
                    print(dress_individual)
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
            dress.close()
            dress_temp.close()
            os.remove("dress.csv")
            os.rename("dress_temp.csv","dress.csv")
        elif (a==2):
            material_id=int(input("enter the id"))
            material_bought=int(input("enter the length"))
            material = open("material.csv",'r')
            material_csv_index = material.readlines()
            for i in range(1,len(material_csv_index)):
                material_individual = material_csv_index[i].split(',')
                material_found_id = int(material_individual[0])
                if material_found_id == material_id:
                    material_total=int(material_bought) * int(material_individual[2])
                    material_list=[material_individual[0],material_individual[1],material_individual[2],material_bought,material_total]
                    d.insert(0,material_list)
                    print(material_individual)
                    material.seek(0)
                    break
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
        elif (a==3):
            custom_name=input("enter name")
            custom_price=input("enter price")
            custom_quant=input("enter quantity")
            custom_total=int(custom_quant) * int(custom_price)
            custom_list=[1,custom_name,custom_price,custom_quant,custom_total]
            d.insert(0,custom_list)
        elif (a==4):
            d.reverse()
            print(d)
            s=1
