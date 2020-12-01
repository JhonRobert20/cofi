producto =[{"bulk_discount":{"Yes":[1,3]} }]
productos= producto[0]["bulk_discount"]
print(productos)
productos2= producto[0]['bulk_discount']['Yes']
print(productos2)
print(len(productos2))
for e in productos:
    print (e, ":", productos[e])

nombres_masculinos = ['Ricky', 'Alvaro', 'David', 'Jacinto', 'Ricky', 'Jose', 'Jose']
nombres_masculinos.remove("Jose") 
nombres_masculinos.remove("Jose") 
print (nombres_masculinos) 
