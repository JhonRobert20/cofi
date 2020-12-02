import json

def load_data(route):#We need to load the file of json that we need
    with open(route) as content:
        products = json.load(content)
        return(products)

def check_jason(products, parameters):#We have to check the data that send to us the json file
    master_list = []
    new_products = products
    print("Estos son los parametros: "+str(parameters))
    until = len(products) -1
    while True:
        for i in range(0, until):
            product = products[i]
            j = 0
            for e in product:
                if e != parameters[j]:
                    print(e)
                    print("hi "+str(new_products[i]))
                    new_products[i][parameters[j]]= product[e]
                    del new_products[i][e]
                    print("cambio: "+str(e)+" por: "+str(parameters[j]))
                    print("i: "+str(i)+" j: "+str(j))
                    print("hi "+str(new_products[i]))
                j = j +1
        if new_products != products:
            print("algo raro")
        else: 
            print(new_products)
            print(product)
            break
    print(new_products)
route = 'productos.json'
file = load_data(route)
#we only want prodcuts, so
products = file['products']#Hacer para que si nos equivocamos no pase nada
parameters = file['Parameters']
check_jason(products, parameters)
print(parameters)
