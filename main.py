import json
import os

def main():

    products_added=[]
    codes_added=[]
    codes_to_show=[]
    lines = "                                                  "
    mini_lines ="             "
    super_mini_lines="    "
    

    def load_data(route='productos.json'):#We need to load the file of json that we need
        with open(route) as content:
            products = json.load(content)
            return(products)
    def check_json(products, parameters, types):#We have to check the data that send to us the json file
        new_products = []
        delete_product = False
        quit_vector = []
        print(parameters)
        i = 0
        for product in products:

            j = 0
            product_line = {}
            for e in product:
                if type(product[e]) != type(types[j]):
                    try:
                        #Primera linea de fallo
                        if ( (type(product[e])==int) or (type(product[e])==float)) and ((type(product[e])==int) or (type(product[e])==float)):
                            product_line[parameters[j]]= product[e]
                            j = j + 1
                        else:
                            print("Fail, change: "+str(product['code'])+" for: "+str(type(product[e]))+" required type: "+str(type(types[j])))
                            product_line[parameters[j]]= product[e]
                            quit_vector.append[i]
                            j = j +1
                            delete_product = True
                    except: 
                        print("Fail, change: "+str(product['code'])+" for: "+str(type(product[e]))+" required type: "+str(type(types[j])))
                        quit_vector.append(i)
                        product_line[parameters[j]]= product[e]
                        j = j +1
                        delete_product = True
                else:
                    product_line[parameters[j]]= product[e]
                    j = j + 1
            
            new_products.append(product_line)
            i = i + 1 
                
        if new_products != products:#Here the program check the requierements of the json file
            products = new_products
            if delete_product == True:  
                for i in range(0, len(quit_vector)):
                    try:
                        for vector in quit_vector:
                            print(lines+"Product removed: "+str(products[vector]['code'])+" check your data file"+lines)
                            products.remove(products[vector])
                            quit_vector.remove(vector)
                            try:
                                for p in range(0,len(quit_vector)):
                                    quit_vector[p] = quit_vector[p] -1
                            except: 
                                print(lines+"The data that can make the program faiulere had been removed")
                    except:
                        print("El vector es: "+str(quit_vector))
                    i = i + -1
                
                return products
            return products
        else:
            if delete_product == True:
                for vector in quit_vector:
                    products.remove(products[vector])
            return products

    
        
    
    

    def scan(code):#Los 2 pueden devolver algo 
        try:
            code = code.upper()
            if len(codes) > 0:
                for i in range(0, len(codes)):
                    codes[i] = codes[i].upper()
            if code in codes:
                products_founded = [product for product in products if product['code'].upper()==code]#Cogemos los que se llamen así
                products_added.append(products_founded[0])#Take in account to make this for data base
                print("Porduct added: "+str(products_founded[0]['code']))
                if code not in codes_added:
                    codes_added.append(code)
                    codes_to_show.append(code)
                    return True
                else: 
                    codes_to_show.append(code)
                    print("Have been added: "+str(code)+" you have "+str(codes_to_show.count(code))+" in your list")
                    return True
            else:
                print("Product can't be added: "+str(code))
        except:
            print("Porduct can't be added: "+str(code))
            return False
    def remove(code):
        try:
            code = code.upper()
            if len(codes) > 0:
                for i in range(0, len(codes)):
                    codes[i] = codes[i].upper()
            if code in codes_added:
                products_founded = [product for product in products if product['code'].upper()==code]
                codes_to_show.remove(code)
                if codes_to_show.count(code) > 0:
                    pass
                else:
                    codes_added.remove(code)
                    
                print("Removed: "+code)
                products_added.remove(products_founded[0])
                return True
            else:
                print("Not in the list: "+code)
                return False
        except:
            print("Can't delete: "+str(code))
            print(codes_to_show)
            return False
                

    def check_2x1():#Solo con el que nos pida,x devuelve el precio que cuesta y el precio que hubiera costado, para impactar más al usuario
        check_pay = {}
        for code in codes_added:#codes_added
            try:
                products_founded = [product for product in products_added if product['code'].upper()==code.upper()]
                products_discounts = [product for product in products_founded if product['2x1_discount']=="YES"]
                i = len(products_founded)
                c_1, c = [i/2, i//2]
                price = products_founded[0]['price']
                total_price = i * price
                total_price_discount = total_price
                total_discount= 0
                discount = True
                if (products_founded[0]['2x1_discount']=="NO"):
                    discount = False

                try:
                    if discount == True and c >=1:
                        if (c_1==c)==True:
                            total_price_discount = c*price
                            total_discount = total_price - total_price_discount
                            
                        elif (c_1==c)==False:
                            total_price_discount = price*(c + 1)
                            total_discount = total_price - total_price_discount

                    else:

                        if ((c < 1)) or (discount==False):
                            total_price = total_price
                            total_price_discount = total_price
                            total_discount = total_price_discount - total_price
                        else:
                            print("Este no tendría que dar ni de broma")
                    check_pay[code]=[total_price_discount,total_price, total_discount]
                
                except:
                    print("-----------------------------------Failure in: "+str(code)+", removed from your products list: "+str(code))
                    products_added.remove(products_founded[0])
                    codes_added.remove(code)
                    codes_to_show.remove(code)
                    codes.remove(code)
            except:
                print("-----------------------------------Failure in: "+str(code)+", removed from your products list: "+str(code))
                products_added.remove(products_founded[0])
                codes_added.remove(code)
                codes.remove(code)

                print("--------------------------------------")
                
            
        return (check_pay)
        
    def check_bulk():
        check_pay={}
        for code in codes_added:
            products_discounts = []
            try:
                products_founded = [product for product in products_added if product['code'].upper()==code.upper()]
            except: 
                products_added.remove(products_founded[0])
                break
            product = products_founded[0]
            price = product['price']
            if type(price)== float or type(price)==int:
                print("")
            else:
                print("Failere in: "+str(code))
                codes_added.remove(code)
                break
            
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
        
            total_price = i * price
            total_price_discount = total_price
            total_discount= 0
            if discount==True and i >=quantity:
                total_price_discount= i * (price-discount)

            total_discount = total_price - total_price_discount
            check_pay[code]=[total_price_discount,total_price, total_discount]
        return check_pay
    #Print the total
    def total():
        try:
            total= 0
            total_discount = 0
            total_price_discount = 0
            count_2x1 = check_2x1()
            count_bulk = check_bulk()
            for code in codes_added:
                prices_bulk = count_bulk[code]
                prices_2x1 = count_2x1[code]
                #
                if prices_2x1[0] <= prices_bulk[0]:
                    total_price_discount = total_price_discount + count_2x1[code][0] 
                else:
                    total_price_discount = total_price_discount + count_bulk[code][0] 

                if prices_2x1[1] <= prices_bulk[1]:

                    total = total + count_2x1[code][1] 
                    
                else:
                    total = total + count_bulk[code][1]

                total_discount = total - total_price_discount

            print("Total price: "+str(total_price_discount)+mini_lines+" Original price: "+str(total)+mini_lines+" Total discount: "+str(total_discount))
            return[total_price_discount,total, total_discount]
        except Exception as  ex:
            print(codes)
            print(codes_added)
            print("Failure in system: "+str(ex)+" have to change data file, uses the sames types in all the products")
    
    #-----------------------------------------------------End of functions--------------------------------------
    


    try:
        route = 'productos.json'
        file = load_data(route)
        products_check = file['products']
        parameters = file['parameters']
    except:
        print(lines+"The file that you have is doesn't working properly, please chek it"+lines)
        
    #we only want prodcuts, so
    types = file['types']
    products = check_json(products_check, parameters, types)
    #print(products)
    codes = []
    for product in products:
        codes.append(product['code'])
    print("codes are: "+str(codes))
    print("                                                  __________________________")
    print("                                                  |Welcome to the Cofi shop|")


    
    run = True
    while run:
        
        option = input("Please select your option: \n"+lines+super_mini_lines+"Add object(Add)"+lines+"\n"+lines+super_mini_lines+"Remove objet(Remove)"+lines+"\n"+lines+super_mini_lines+"Show total(Total)"+lines+"\n"+lines+super_mini_lines+"Exit(Exit)"+lines+"\n"+mini_lines)
        posibles = ["ADD","REMOVE","TOTAL", "EXIT"]
        try:
            if option.upper() in posibles:
                option = option.upper()
                if option=="ADD":
                    if len(codes) > 0:
                        print("Now, select your product: "+str(codes))
                        new_product = scan(input(mini_lines+"¿Which one? "))
                    else: 
                        print("You don't have nothing in the list, please check your json file")
                        break
                    
                elif option=="REMOVE":
                    if (len(codes_to_show)) > 0:

                        print(super_mini_lines+"Remove a product from this list "+str(codes_to_show))
                        del_product = remove(input("¿Wich one do you want to be removed? "))
                    else:
                        print(mini_lines+"You can't choose this option, you don't have anything on your list")
                    #if del_product == True
                elif option == "TOTAL":
                    show_total = total()
                elif option == "EXIT":
                    print(mini_lines+"Thanks for buying in our store, we hope you've had a good experince. See you neext time ")
                    break
            else:
                print(lines+"Please select a available options"+lines)
        except Exception as e:
            print("Excepcion: "+str(e))

main()