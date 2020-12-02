products = [{"hola":"pena", "nada": "togulin"},{"nada":"jaajaj", "jdjdjd": "jsjdjs"}]
parameters = ["hola", "gran pingu"]
hola_general= []
hola_1 = {}
print(len(products)-1)
for i in range(0, len(products) ):
            product = products[i]
            j = 0
            hola_1 = {}
            for e in product:

                hola_1[parameters[j]]= product[e]

                j = j +1
            hola_general.append(hola_1)
print(hola_general)