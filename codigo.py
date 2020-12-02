products = [{"hola":"pena", "nada": "togulin"},{"nada":"jaajaj", "jdjdjd": "jsjdjs"}]
parameters = ["jja", "gran pingu"]
hola_general= []
hola_1 = {}
for i in range(0, len(products)-1):
            product = products[i]
            j = 0
            hola_1 = {}
            for e in product:
                if e != parameters[j]:
                    print(e)

                    hola_1[parameters[j]]= product[e]
                    
                    print("cambio: "+str(e)+" por: "+str(parameters[j]))
                    print("i: "+str(i)+" j: "+str(j))
                j = j +1
                hola_general.append(hola_1)
print(hola_general)