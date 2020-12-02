import numpy as np

parametros=["code", "name", "price", "2x1_discount", "bulk_discount"]
a= np.array(parametros)
parametros2  = ["code", "name", "price", "2x1_discount", "bulk_discount"]
b = np.array(parametros2)
c = np.less_equal(a, b)
for e 