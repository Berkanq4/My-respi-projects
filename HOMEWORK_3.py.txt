from ast import Constant
import re
from struct import pack_into

data_base = input("Please enter the database: ")
movement_name = input("Please enter the movement name that you want to purchase: ")



liste = re.split(';|,|:', data_base)



if (movement_name in data_base):
    hareket_yeri = liste.index(movement_name)
    
    hareket_grubu = hareket_yeri / 3
    budget = float(input("Please enter the amount of money you have (in million): "))
    painting_name = input("Please enter the name of the painting that you want to buy: ").split(',')
    ikincil = 0
    garaj = False
    sum = 0
    yenileyici = ""
    bos = ""
    for i in range(0,len(painting_name)):

        if not painting_name[i] in liste:
            print(f"{painting_name[i]} is not in the database.")
       
        elif (movement_name != liste[liste.index(painting_name[i])+1]):
            print(f"{painting_name[i]} does not belong to {movement_name} movement.")

        
        
          
               
         
        else:
            bos = ""
            bos += liste[liste.index(painting_name[i])+2]
            bosx = bos.replace('M', '')
            sayi = float(bosx)
            sum += sayi

            
            ikincil += 1
            if (ikincil == len(painting_name)):
                count = 0
                for jaguar in painting_name:
                   
                    yenileyici += jaguar
                    count += 1
                    if (count != len(painting_name)):
                        yenileyici += ","
            
            
            if (budget < sum and i == len(painting_name)-1):
                print(f"Willing painting(s) value(s) are higher than your current budget.")
                
            elif (budget >= sum and i == len(painting_name)-1):
                print(f"You have successfully purchased {yenileyici}.")

           
    

else:
    print(f"There are no paintings belonging to {movement_name}.")

