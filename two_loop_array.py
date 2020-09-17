
arr = [1,2,6,3,22,346,436,434,31,2333,34534,546,43,34534,3453,4,5,45,34534,345,534,43]

"""
for i,j in zip(range(0,len(arr)), range(len(arr)-1, -1, -1)):
    print (i,j)
    if i ==j:
        break

print (i,j)

i = 0
j = 21
while True:
"""

for i in range(len(arr)):
    for j in range(0,len(arr)-i-1):
        if arr[j] > arr[j+1]:
            temp  = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp


print(arr)