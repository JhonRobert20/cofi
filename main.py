import json
import numpy as np

problem = 0
products_added=[]
codes_added=[]

def load_data(route):#We need to load the file of json that we need
    with open(route) as content:
        products = json.load(content)
        return(products)
def check_jason(products, parameters):#We have to check the data that send to us the json file
    new_products = []
    print(parameters)
    for product in products:

        j = 0
        product_line = {}
        for e in product:
            product_line[parameters[j]]= product[e]
            j = j + 1
        new_products.append(product_line)
    if new_products != products:
        products = new_products


        


if __name__ == '__main__':
    
    route = 'productos.json'
    file = load_data(route)
    #we only want prodcuts, so
    products = file['products']#products[0] #products[0]['bulk_discount']['NO']
    parameters = file['parameters']
    check_jason(products, parameters)
    codes = []
    for product in products:
        codes.append(product['code'])
    print(codes)
    print("----------------------------------------------------------------------------------")
    def scan(code):#Los 2 pueden devolver algo 
        if code in codes:
            products_founded = [product for product in products if product['code']==code.upper()]#Cogemos los que se llamen así
            products_added.append(products_founded[0])#Take in account to make this for data base
            print("producto añadido: "+str(products_founded[0]['code']))
            if code not in codes_added:
                codes_added.append(code)
            else: 
                print("No pasa nada")
        else:
            print("El producto no ha sido añadido")

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
                    print(str(c)+" en descuento "+products_founded[0]['code']+" son: "+str(i)+" y cada uno vale: "+str(price))
                else:
                    print(str(len(products_discounts))+" en descuento "+products_founded[0]['code']+" son: "+str(i)+" y cada uno vale: "+str(price))
                #Podre eliminar esto numero 1
                
                #print("-------------- \n"+str(products_discounts)+"\n ------------------")
                
                try:
                    if discount == True and c >=1:
                        if (c_1==c)==True:
                            total_price_discount = c*price
                            total_discount = total_price - total_price_discount
                            
                        elif (c_1==c)==False:
                            total_price_discount = price*(c + 1)
                            total_discount = total_price - total_price_discount
                        else:
                            print("Esto no tendría que saltar nunca fallado")
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
                print("--------------------------------------")
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
            
            discount = False
            DIC = product["bulk_discount"]
            quantity = 0
            discount = 0
            for key in DIC:
                if key =="YES":
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
            total= 0
            total_discount = 0
            total_price_discount = 0
            count_2x1 = check_2x1()
            count_bulk = check_bulk()
            for code in codes_added:
                prices_bulk = count_bulk[code]
                prices_2x1 = count_2x1[code]
                if prices_2x1[0] <= prices_bulk[0]:
                    total_price_discount = total_price_discount + count_2x1[code][0] 
                else:
                    total_price_discount = total_price_discount + count_bulk[code][0] 
                if prices_2x1[1] <= prices_bulk[0]:
                    total = total + count_2x1[code][1] 
                else:
                    total = total + count_bulk[code][1]
                if prices_2x1[2] <= prices_bulk[2]:
                    total_discount = total_discount + count_2x1[code][2]
                else:
                    total_discount = total_discount + count_bulk[code][2]

            print("el total es: "+str(total_price_discount))
        except:
            print("se intento")

            
    print(codes_added)
    scan("jol")
    scan('MUG')
    scan('VOUCHER')
    scan('MUGI')
    scan('TSHIRT')
    total()
    check_2x1()
    print(codes_added)
    print(products_added)
    print(len(products_added))
    scan('MUG')
    scan('MUGI')
    scan('VOUCHER')
    scan('TSHIRT')
    check_2x1()
    check_bulk()
    total()
    print(codes)
    print(codes_added)
    print(products_added)
    
    #def check_promo(products_added):#no modificar el precio del producto directamente
