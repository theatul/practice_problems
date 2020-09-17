array = [0,1]

for i in range(2,100):
    array.append(array[i-1]+array[i-2])

print (array)