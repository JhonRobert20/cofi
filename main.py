import json

products_added=[]

def load_data(route):
    with open(route) as content:
        products = json.load(content)
        return(products)


if __name__ == '__main__':
    route = 'productos.json'
    file = load_data(route)
    #we only want prodcuts, so
    products = file['products']#products[0] #products[0]['bulk_discount']['NO']
    print(str(products[0]['bulk_discount']['NO'][0])+"jddddddddddddddddd")
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
        else:
            print("El producto no ha sido añadido")
    scan('VOUCHER')
    scan('TSHIRT')
    scan('MUG')

    def check_2x1(cod2e):#Solo con el que nos pida,x devuelve el precio que cuesta y el precio que hubiera costado, para impactar más al usuario
        if type(cod2e)!=(int or float) and cod2e.upper() in codes:
            for code in codes:
                print(code)
                products_founded = [product for product in products_added if product['code']==code.upper()]
                products_discounts = [product for product in products_founded if product['2x1_discount']=="YES"]
                i = len(products_founded)
                c_1, c = [i/2, i//2]
                price = products_founded[0]['price']
                
                total_price = i * price
                total_price_discount = c * price
                total_discount= 0
                have_to = True
                if (products_founded[0]['2x1_discount']=="NO"):
                    have_to = False
                #Podre eliminar esto numero 1
                if have_to == True:
                    print(str(c)+" en descuento "+products_founded[0]['code']+" son: "+str(i)+" y cada uno vale: "+str(price))
                else:
                    print(str(len(products_discounts))+" en descuento "+products_founded[0]['code']+" son: "+str(i)+" y cada uno vale: "+str(price))
                #Podre eliminar esto numero 1
                
                #print("-------------- \n"+str(products_discounts)+"\n ------------------")
                
                try:
                    if have_to == True and c >=1:
                        if (c_1==c)==True:
                            print("Estas en el primero")
                            total_price_discount = c*price
                            total_discount = total_price - total_price_discount
                            
                        elif (c_1==c)==False:
                            print("Estas en el segundo")
                            total_price_discount = price*(c + 1)
                            total_discount = total_price - total_price_discount
                        else:
                            print("Esto no tendría que saltar nunca fallado")
                    else:

                        if ((c < 1)) or (have_to==False):
                            print("Estas en el tercero")
                            total_price = total_price
                            total_price_discount = total_price
                            total_discount = total_price_discount - total_price
                        else:
                            print("Este no tendría que dar ni de broma")
                    print("----El precio final es: "+str(total_price_discount)+ " el precio total: "+str(total_price)+" y el descuento total: "+str(total_discount)+"--------")
                    #return [total_price_discount,total_price, total_discount]
                except:
                    print("--------------------------------------ROTO-----------------------------------")
        else:
            print(f"*****--------{cod2e} no esta en la lista-------****")
        
    def check_bulk(code):
        if type(code)!=(int or float) and code.upper() in codes:
            for codei in codes:
                return False
            
        else:
            print("nada, todo fake")
    
    check_2x1('MUG')
    scan('VOUCHER')
    scan('VOUCHER')
    scan('VOUCHER')
    scan('VOUCHER')
    scan('VOUCHER')
    scan('VOUCHddR')
    scan('TSHIRT')
    scan(23)
    scan('TSHIRT')
    scan('MUG')
    check_2x1('Voucher')
    check_2x1('Vouchedddr')
    check_2x1(23)
    check_2x1('TSHIRT')
    
    
    #def check_promo(products_added):#no modificar el precio del producto directamente
