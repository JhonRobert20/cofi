def main():
    import json
    problem = 0
    products_added=[]
    codes_added=[]

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
                            print("Fallo definitivo, cambia: "+str(product['code'])+" e: "+str(product[e])+" tipo: "+str(types[j]))
                            product_line[parameters[j]]= product[e]
                            quit_vector.append[i]
                            j = j +1
                            delete_product = True
                    except: 
                        print("Fallo definitivo, cambia: "+str(product['code'])+" e: "+str(product[e])+" tipo: "+str(types[j]))
                        quit_vector.append(i)
                        product_line[parameters[j]]= product[e]
                        j = j +1
                        delete_product = True
                else:
                    product_line[parameters[j]]= product[e]
                    j = j + 1
            
            new_products.append(product_line)
            i = i + 1 
        
        if new_products != products:
            products = new_products
            if delete_product == True:
                for vector in quit_vector:
                    print("------------Product removed: "+str(products[vector]['code'])+" ----------------")
                    products.remove(products[vector])
                return products
            return products
        else:
            if delete_product == True:
                for vector in quit_vector:
                    products.remove(products[vector])
            return products

        
    route = 'productos.json'
    file = load_data(route)
    #we only want prodcuts, so
    products_check = file['products']#products[0] #products[0]['bulk_discount']['NO']
    parameters = file['parameters']
    types = file['types']
    products = check_json(products_check, parameters, types)
    #print(products)
    codes = []
    for product in products:
        codes.append(product['code'])
    print(codes)
    print("----------------------------------------------------------------------------------")
    def scan(code):#Los 2 pueden devolver algo 
        try:
            if code.upper() in codes:
                products_founded = [product for product in products if product['code']==code.upper()]#Cogemos los que se llamen así
                products_added.append(products_founded[0])#Take in account to make this for data base
                print("producto añadido: "+str(products_founded[0]['code']))
                if code not in codes_added:
                    codes_added.append(code)
                    return True
                else: 
                    print("El: "+str(code)+" ya esta añadido")
                    return True
            else:
                print("El producto no ha sido añadido: "+str(code))
        except:
            print("El producto no ha sido añadido: "+str(code))
            return False
    def remove(code):
        try:
            code = code.upper()
            if code in codes_added:
                products_founded = [product for product in products if product['code']==code.upper()]
                codes_added.remove(code)
                products_added.remove(products_founded[0])
                print("Se quito de la lista de productos actuales a: "+str(code))
                return True
            else:
                print("No se encuentra en la lista")
                return False
        except:
            print("Error al eliminar: "+str(code))
            print(codes_added)
            return False
                

    def check_2x1():#Solo con el que nos pida,x devuelve el precio que cuesta y el precio que hubiera costado, para impactar más al usuario
        check_pay = {}
        problem = 0
        for code in codes_added:
            try:
                products_founded = [product for product in products_added if product['code']==code.upper()]
                products_discounts = [product for product in products_founded if product['2x1_discount']=="YES"]
                i = len(products_founded)
                c_1, c = [i/2, i//2]
                price = products_founded[0]['price']
                total_price = i * price
                total_price_discount = total_price
                total_discount= 0
                discount = True
                print(code)
                if (products_founded[0]['2x1_discount']=="NO"):
                    discount = False
                #Podre eliminar esto numero 1
                if discount == True:
                    print("***"+str(c)+" en descuento "+products_founded[0]['code']+" son: "+str(i)+" y cada uno vale: "+str(price)+"****")
                else:
                    print("*** Ninguno en descuento "+products_founded[0]['code']+" son: "+str(i)+" y cada uno vale: "+str(price)+"****")
                #Podre eliminar esto numero 1

                try:
                    if discount == True and c >=1:
                        if (c_1==c)==True:
                            total_price_discount = c*price
                            total_discount = total_price - total_price_discount
                            
                        elif (c_1==c)==False:
                            total_price_discount = price*(c + 1)
                            total_discount = total_price - total_price_discount
                        else:
                            print("Esto no tendría que saltar nunca fallado lo dejo por si no he acertado")
                    else:

                        if ((c < 1)) or (discount==False):
                            total_price = total_price
                            total_price_discount = total_price
                            total_discount = total_price_discount - total_price
                        else:
                            print("Este no tendría que dar ni de broma")
                    #print("----El precio final es: "+str(total_price_discount)+ " el precio total: "+str(total_price)+" y el descuento total: "+str(total_discount)+"--------")
                    check_pay[code]=[total_price_discount,total_price, total_discount]
                
                except:
                    print("--------------------------------------ROTO-----------------------------------")
            except:
                print(str(codes_added)+"--------rrr------------------------------"+str(code))
                products_added.remove(products_founded[0])
                codes_added.remove(code)
                codes.remove(code)
                print(codes_added)
                print(products_added)
                print(codes)
                problem = problem + 1 
                print("--------------------------------------")
                
            
        print(check_pay)
        return (check_pay)
        
    def check_bulk():
        check_pay={}
        for code in codes_added:
            products_discounts = []
            try:
                products_founded = [product for product in products_added if product['code']==code.upper()]
            except: 
                products_added.remove(products_founded[0])
                break
            product = products_founded[0]
            price = product['price']
            if type(price)== float or type(price)==int:
                print("")
            else:
                print("fallo aqui 189")
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
            print(total_discount)
            check_pay[code]=[total_price_discount,total_price, total_discount]
            print(check_pay)
        return check_pay

    def total():
        try:
            if problem >=1:
                check_2x1()
                print("-----------------Esto no tiene que dar, linea 179----------------------")
            total= 0
            total_discount = 0
            total_price_discount = 0
            count_2x1 = check_2x1()#no se porque no va
            count_bulk = check_bulk()#no se porque no va
            print("Bien ya no es esto")
            for code in codes_added:
                prices_bulk = count_bulk[code]
                prices_2x1 = count_2x1[code]
                if prices_2x1[0] <= prices_bulk[0]:
                    total_price_discount = total_price_discount + count_2x1[code][0] 
                else:
                    total_price_discount = total_price_discount + count_bulk[code][0] 
                if prices_2x1[1] <= prices_bulk[1]:#puse un 0 antes
                    total = total + count_2x1[code][1] 
                    
                else:
                    total = total + count_bulk[code][1]
                if prices_2x1[2] <= prices_bulk[2]:
                    total_discount = total_discount + count_2x1[code][2]
                else:
                    total_discount = total_discount + count_bulk[code][2]

            print("El total es: "+str(total_price_discount))
            return[total_price_discount,total, total_discount]
        except Exception as  ex:
            print(codes)
            print(codes_added)
            print("Fallo del sistema: "+str(ex)+" has de cambiar el archivo json, si usas int en uno has de mantener lo mismo")
    lines = "------------------"
    run = True
    while run:
        option = input("Diferents options: \n"+lines+"Add object(Add)"+lines+"\n"+lines+"Remove objet(Remove)"+lines+"\n"+lines+"Show total(Total)"+lines+"\n"+lines+"Exit(Exit)"+lines+"\n")
        posibles = ["ADD","REMOVE","TOTAL", "EXIT"]
        try:
            if option.upper() in posibles:
                option = option.upper()
                if option=="ADD":
                    print("You can add: "+str(codes))
                    new_product = scan(input("¿Which one? "))
                    #if new_product = True
                elif option=="REMOVE":
                    print("products posibles to delete: "+str(codes_added))
                    del_product = remove(input("¿Wich one do you want to be removed? "))
                    #if del_product == True
                elif option == "TOTAL":
                    show_total = total()
                elif option == "EXIT":
                    print("Thanks to use that program, exit actived")
                    break
            else:
                print("Write Chose other option")
        except Exception as e:
            print("Excepcion: "+str(e))

main()