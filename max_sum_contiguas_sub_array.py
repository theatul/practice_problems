array = [10,10,-1, -9, -100, 10 , 30]

""" O(N^2)
Max = array[0]
x = 0
y = 0

#tmax= array[0]
for i in range (0, len(array)):
    tmax  = 0
    for j in range (i, len(array)):
        tmax = tmax + array[j]
        if tmax > Max:
            Max =  tmax
            x = i
            y = j

print (x)
print (y)
print (Max)
"""
array = [-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7] 

Max_so_far = 0
Max_ending_here = 0

for i in range(len(array)):
    Max_ending_here += array[i]
    if Max_so_far < Max_ending_here:
        Max_so_far = Max_ending_here

    if Max_ending_here < 0:
        Max_ending_here = 0

print (Max_so_far)