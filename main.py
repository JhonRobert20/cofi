#
import json
import os
from datetime import datetime
#

#Funtion that makes the program run
def main():

    #-----------------------------------------------------------------Constants (until line 18)-----------------------------------------------------------------#
    products_added=[]#List, products added, used to control products
    codes_added=[]#List of products code in basket, use to control operations
    codes_to_show=[]#List of products code in the basket, used to count how much
    lines = "                                                  "#String, used to show things
    mini_lines ="              "#String, used to show things
    super_mini_lines="      "#String, used to show things
    now = datetime.now()#Date, used to record the date in "Json_changes(it is not created yet)"
    #-----------------------------------------------------------------Constants-----------------------------------------------------------------#

    #-----------------------------------------------------------------Functions (until line 310)-----------------------------------------------------------------#

    #Write in "Json_Changes any issue and all the shopping operations"
    def write_ticket(line, show=True):#You send "line" as a parameter and select if you want to show it or not. 
        file_name="Json_Changes"
        extention = ".txt"
        name = file_name + extention
        try:#If the file exists
            file = open(name,"r")
            lines = file.readlines()
            file.close()
            file_w = open(name, "a")
            file_w.write(line+"\n")
            file_w.close()
        
        except:#If the file does not exist
                file_a = open(name, "a")
                file_a.write(line+"\n")
                file_a.close()
        finally:
            if show == True:#If we need to show it
                    print("Added to "+ file_name+": "+line)
            else:#If we don't want to show the message
                pass 
    
    #load the json file that we need
    def load_data(route):#The program uses the route of file to upload the file
        with open(route) as content:
            products = json.load(content)
            return(products)

    #Check if the data of json file is correct
    def check_json(products, parameters, types):# Parameters: List of products, parameters that have to be followed, correct types of data

        new_products = []#List of futures products (the parameters are checked)
        delete_product = False
        quit_vector = []#List of futures removed porducts
        write_ticket("The parameters to make this operation are: "+str(parameters))
        i = 0#Increment 1, for any product in products

        for product in products:
            j = 0#Increment 1 for any parameter inside a product and it reset for any new product
            product_line = {}#Dictionary of a product and it reset for any product
            for e in product:
                if type(product[e]) != type(types[j]):#If the type of data is different, the program will do more checks

                    try:#If there aren't errors, the program will check the type 
                        
                        if ( (type(product[e])==int) or (type(product[e])==float)) and ((type(product[e])==int) or (type(product[e])==float)):#If it is a number, pass the type check
                            pass
                            
                        else:#If it is not, the program says that is a bad product
                            #The program won't delete the products yet
                            write_ticket("Fail, change: "+str(product['code'])+" for: "+str(type(product[e]))+" required type: "+str(type(types[j])))
                            quit_vector.append[i] #Prepare to delete
                            delete_product = True
                        
                    except:#If there are any issue the program says that it is a bad product
                        write_ticket("Fail, change: "+str(product['code'])+" for: "+str(type(product[e]))+" required type: "+str(type(types[j])))
                        quit_vector.append(i) #Prepare to delete
                        delete_product = True

                product_line[parameters[j]]= product[e]#Add keys and values to a product
                j = j +1

            new_products.append(product_line)#Products with the parameter checked
            i = i + 1 

        products = new_products#Just to be sure that uses all the parameters available

        #Now the program have to remove all the products that have not pased the check
        if delete_product == True:  
            for i in range(0, len(quit_vector)):#The program run a loop until quit_vector dissapears
                try:#If a failure is not occur, the program will write it in the: Json_Changes
                    for vector in quit_vector:
                        
                        write_ticket("Product removed: "+str(products[vector]['code'])+" check your data file")#Information
                        products.remove(products[vector])
                        quit_vector.remove(vector)
                        try:#Until "quit_vector" dissapears
                            quit_vector[-1] = quit_vector[-1] -1
                        except: 

                            write_ticket("The data that could make the program to fail has been removed")#Information
                except:#If ther is a failure,  the program will continue with the loop
                    pass           
        return products#Finally return products checked
            
    #Function to add a product to the basket
    def scan(code):#The parameters are: the code to scan

        try:#If the user uses letters
            #Pass codes to upper
            code = code.upper()
            if len(codes) > 0:
                for i in range(0, len(codes)):
                    codes[i] = codes[i].upper()

            if code in codes:
                products_founded = [product for product in products if product['code'].upper()==code]#Add all products if they have the same code
                products_added.append(products_founded[0])#The product is added to "products_added"

                if code not in codes_added:#If it has not been added in "codes_added" yet
                    codes_added.append(code)
                    codes_to_show.append(code)
    
                else: #If it exists in "codes_added"
                    codes_to_show.append(code)

                write_ticket("Have been added: "+str(code)+" you have "+str(codes_to_show.count(code))+" in your list", False)#Information
                print("Have been added: "+str(code)+" you have "+str(codes_to_show.count(code))+" in your list")#Information
                return True
            else:#If code is not in codes
                
                write_ticket("Product can't be added: "+str(code), False)#Information
                print("Product can't be added: "+str(code))#Information
                return False
        except:#If user try to add something different that letters
            print("Porduct can't be added: "+str(code))#Information
            return False

    #Function to remove a product from the basket
    def remove(code):
        try:#If user uses letters
            #Pass codes to upper
            code = code.upper()
            
            if code in codes_added:
                products_founded = [product for product in products if product['code'].upper()==code]#Add all products if they have the same code

                codes_to_show.remove(code)#First removes "codes_to_show", later it checks if there are no product and delete the "codes_added"
                if codes_to_show.count(code) > 0:
                    pass
                else:
                    codes_added.remove(code)

                write_ticket("Removed: "+code, False)#Information
                print("Removed: "+code)#Information
                products_added.remove(products_founded[0])#Remove the product of "producst_added"
                return True

            else:
                write_ticket("It is not in the list: "+code+", take into acount for the future", False)#Information
                print(mini_lines+"It is not in the list: "+code)#Information
                return False

        except:#If the user don't use letters
            print(mini_lines+"It can't be deleted: "+str(code))#Information
            print(codes_to_show)#Information
            return False
                
    #Function that check if the products have 2x1_discount
    def check_2x1():#Return: Total to pay,  Total original

        check_pay = {}
        for code in codes_added:#codes_added
            try:
                products_founded = [product for product in products_added if product['code'].upper()==code.upper()]#Add all products if they have the same code
                #Formulas for "2x1_discount"
                i = len(products_founded)
                c_1, c = [i/2, i//2]
                price = products_founded[0]['price']
                total_price = i * price
                total_price_discount = total_price
                discount = True
                if (products_founded[0]['2x1_discount']!="YES"):#If in json file we don't find a "yes" (in products.json)
                    discount = False

                try:
                    if discount == True and c >=1:
                        if (c_1==c)==True:#Formula if the quantity is even
                            total_price_discount = c*price
                            
                        elif (c_1==c)==False:#Formula if it is not
                            total_price_discount = price*(c + 1)

                    else:

                        if ((c < 1)) or (discount==False):
                            total_price = total_price
                            total_price_discount = total_price
                        else:
                            pass
                    check_pay[code]=[total_price_discount,total_price]
                
                except:#New filter if there is some error in "check_json" funtion, it will only apears if there are any changes in "bulk_disocunt" in json file
                    write_ticket("There is a failure in: "+str(code)+", it has been removed from your products list", False)#Information
                    print("-----------------------------------There is a failure in: "+str(code)+", it has been removed from your products list-----------------------------------")#Information
                    #------------Remove all from this product----#
                    products_added.remove(products_founded[0])
                    products.remove(products_founded[0])
                    codes_added.remove(code)
                    codes_to_show.remove(code)
                    codes.remove(code)
                    #------------Remove all from this product----#

            except:#New filter if there is some error in "check_json" funtion, it will only apears if there are any changes in "bulk_disocunt" in json file
                write_ticket("There is a failure in: "+str(code)+", it has been removedit has been removed from your products list", False)#Information
                print("-----------------------------------Failure in: "+str(code)+", it has been removedit has been removed from your products list-----------------------------------")#Information
                #------------Remove everything of this product----#
                products_added.remove(products_founded[0])
                codes_added.remove(code)
                codes_to_show.remove(code)
                codes.remove(code)
                #------------Remove everything of this product----#
            
        return (check_pay)
    
    
    def check_bulk():
        check_pay={}
        for code in codes_added:
            try:#It can fail if "bulk_discount" it is not used in json file
                products_discounts = []

                products_founded = [product for product in products_added if product['code'].upper()==code.upper()]#Add all products if have the same code

                product = products_founded[0]
                price = product['price']
                #Another filter: if can pass the "check_json"
                if type(price)== float or type(price)==int:
                    pass
                else:
                    print("There is a failere in: "+str(code))#Information
                    codes_added.remove(code)
                    break

                #The program acces to "bulk_discount"
                discount = False
                DIC = product["bulk_discount"]
                quantity = 0
                discount = 0
                for key in DIC:
                    if key.upper() =="YES":
                        products_discounts.append(product)
                        discount = True
                        quantity = DIC['YES'][0]
                        discount = DIC['YES'][1]
                i = len(products_founded)
                #Calculates if there are a discount or not
                total_price = i * price
                total_price_discount = total_price

                if discount==True and i >=quantity:
                    total_price_discount= i * (price-discount)

                check_pay[code]=[total_price_discount,total_price]#Add the prices with discount of every product

            except:#New filter: if there is some error in "check_json" funtion, it will apears if there are any changes in "bulk_disocunt"
                print(lines+"Please use bulk_disocunt in the parameters of your products")#Information

        return check_pay#The program return all the prices (The total price with the discount and the total price without it)

    #Show the total price that the client have to pay
    def total():
        try:
            total= 0 #Original
            total_discount = 0 #Total that the client have to pay
            total_price_discount = 0 #The total discount made
            count_2x1 = check_2x1()
            count_bulk = check_bulk()

            #Check the lower price in "prices_2x1" or "prices_bulk" 
            for code in codes_added:
                prices_bulk = count_bulk[code]
                prices_2x1 = count_2x1[code]
                
                if prices_2x1[0] <= prices_bulk[0]:
                    total_price_discount = total_price_discount + count_2x1[code][0] 
                else:
                    total_price_discount = total_price_discount + count_bulk[code][0] 

                if prices_2x1[1] <= prices_bulk[1]:

                    total = total + count_2x1[code][1] 
                    
                else:
                    total = total + count_bulk[code][1]

                total_discount = total - total_price_discount
            #Show the results
            write_ticket("Total price: "+str(total_price_discount)+mini_lines+" Original price: "+str(total)+mini_lines+" Total discount: "+str(total_discount), False)#Information
            print("Total price: "+str(total_price_discount)+mini_lines+" Original price: "+str(total)+mini_lines+" Total discount: "+str(total_discount))#Information
            return[total_price_discount,total, total_discount]
        except Exception as  ex:
            print(codes)
            print(codes_added)
            print("There is failure in the system: "+str(ex)+", you have to change the data file, you must use the sames types in all the products, the program have been ended")#Information
            quit()
    
    #-----------------------------------------------------------------Functions-----------------------------------------------------------------#
    

    #-----------------------------------------------------------------Filter pass (until 337)-----------------------------------------------------------------#
    try:#Check if the file exists and the program can use it
        route = 'products.json'
        file = load_data(route)

        # Paramatemers to check in json file
        products_check = file['products']
        parameters = file['parameters']
        types = file['types']

    except: # The program will be closed
        print(mini_lines+"The file that you have it is not working properly, please check it, the program have been ended"+lines)
        write_ticket("The file that you have it is not working properly, the program have been ended", False)
        write_ticket("-------------------------------------"+str(now)+"------------------------------------")
        quit()

    #Products and codes after the checking
    products = check_json(products_check, parameters, types)
    codes = []
    for product in products:
        codes.append(product['code'])
    print("Available codes are: "+str(codes))
    print("                                                  __________________________")
    print("                                                  |Welcome to the Cofi shop|")
    #-----------------------------------------------------------------Filter pass-----------------------------------------------------------------#

    #-----------------------------------------------------------------Menu (until 397)-----------------------------------------------------------------#
    run = True
    while run:
        
        option = input("Please select your option: \n"+lines+super_mini_lines+"Add object(Add)"+lines+"\n"+lines+super_mini_lines+"Remove objet(Remove)"+lines+"\n"+lines+super_mini_lines+"Show total(Total)"+lines+"\n"+lines+super_mini_lines+"Exit(Exit)"+lines+"\n"+mini_lines)
        posibles = ["ADD","REMOVE","TOTAL", "EXIT"]
        try:
            if option.upper() in posibles:#If the client select any option available

                option = option.upper()
                if option=="ADD":#Command_try: Add a product with a available code

                    if len(codes) > 0:#If there are products to be added
                        print("Now, select your product: "+str(codes))
                        new_product = scan(input(mini_lines+"¿Which one? "))

                    else:#If the file data don't have codes inside, the program is breaked
                        print("You don't have anything in the list, please check your json file")
                        write_ticket("You don't have anything in the list, please check your json file")
                        write_ticket("-------------------------------------"+str(now)+"------------------------------------")
                        break
                    
                elif option=="REMOVE":#Command-try: Delete a product added

                    if (len(codes_to_show)) > 0:#If something was added
                        print("Remove a product from this list "+str(codes_to_show))
                        del_product = remove(input(mini_lines+"¿Wich one do you want to be removed? "))

                    else:#If don't have any product added
                        print("You can't choose this option, you don't have anything on your list")

                elif option == "TOTAL":#Command_try: Show how much the client have to pay

                    if (len(codes_to_show)) > 0:#If something was added
                        show_total = total()
                        for codes_price in codes_added:
                            print(codes_price+": "+str(codes_to_show.count(codes_price))+"   ")

                    else:#If the client haven't add anything
                        print("You can't choose this option, you don't have anything on your list")
                    
                elif option == "EXIT":#Command: Quit the program

                    if len(codes_to_show) > 0:#If the client have any product added
                        for codes_price in codes_added:
                            write_ticket(codes_price+": "+str(codes_to_show.count(codes_price)), False)
                        print(mini_lines+"Thanks for buying in our store, we hope you've had a good experince. See you neext time ")

                    else:#If don't have anything added
                        print(super_mini_lines+lines+"   Thanks to come to our shop")
                    write_ticket("-------------------------------------"+str(now)+"------------------------------------")
                    break

            else:#If the client don't select any available option
                print(str(option)+" it is not correct, please select a available options")

        except Exception as e:#If there are any error, the program is not breaked
            print("Exception: "+str(e))
    #-----------------------------------------------------------------Menu-----------------------------------------------------------------#

main()
