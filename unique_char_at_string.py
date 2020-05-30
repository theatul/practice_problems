# Implement an algorithm to determine if a string has all unique characters. What if you
# cannot use additional data structures?
# Ans: if using additional data structure, create an array / map and keep track of all the char's O(N)
# 2- Not using any additional space  sort the array and check if a char is same as the next char. NlogN

# Intresting : can use a 32 bit integer and set bit value for each char index = char - ascii(a)

def uniquchar(string):
    if not string:
        return "failed"
    
    map = {} # Can be a bool array
    for char in string:
        if char in map:
            return False
        
        map[char] = 1

    return True

def uniquChar1Space(string):
    if not string:
        return "failed"

    string.sort(string) # Implement a sorting algo.
    for i in range(string.len() - 1):
        if string[i] == string[i+1]:
            return False

    return True

