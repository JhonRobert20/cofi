import json


products_added=[]
codes_added=[]

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
            master_list = []
            for product in products:
                lista=[]
                for e in product:
                    lista.append(e)
                master_list.append(lista)
            print(master_list)
            i = 0
            while i < len(master_list):
                pene = master_list[i]
                comparacion= 0
                for list1 in master_list:
                    k = 0
                    for element in list1:
                        if element in pene:
                            k = k +1
                            if k ==len(list1):
                                comparacion = comparacion +1

                    comparacion = len(element)
                    if comparacion > (len(products) - 3 ):
                        products_added.append(products_founded[0])#Take in account to make this for data base
                        print("producto añadido: "+str(products_founded[0]['code']))
                        if code in codes_added:
                            print("Producto aceptado")
                        else: 
                            codes_added.append(code)
                            pass
                    
        else:
            print("El producto no ha sido añadido")
scan("jol")
scan('MUG')
scan('MUGI')
scan('VOUCHER')
