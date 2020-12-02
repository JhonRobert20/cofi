vector = [1,2,3]
quit_v = []
print(len(vector))
i = 0

while i < len(vector):
    print ("este: ")
    print("vector 2:  es esta: "+str(vector))
    v = vector[i]
    quit_v.append(v)
    print(i)
    i = i + 1
print(vector)
vector=[1,2,3]
for o in vector:
    print(o)
    vector.remove(o)
print(vector)