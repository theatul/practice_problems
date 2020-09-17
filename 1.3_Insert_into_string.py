"""
URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the string
has sufficient space at the end to hold the additional characters, and that you are given the "true"
length of the string. (Note: If implementing in Java, please use a character array so that you can
perform this operation in place.)
EXAMPLE
", 13
Input: "Mr John Smith
Output: "Mr%20John%20Smith"
"""

"""
def insertIntoString(str_list, char, index):

    for i in range(len(str_list)-1, index, -1):
        str_list[i] = str_list[i-1]

    str_list[index] = char

TODO: Dry run
"""
"""
[1,2,3,' ',4,5,6,7, '', '', '']
index = 3 loop 10 - 5
[1,2,3,' ',4,5,6,7, '', '', '7']
[1,2,3,%,2,0,4,5, 6, 7]
"""
""""
def insertIntoString2(str_list, repl, index):

    replacement_len = len(repl)
    print("Index {}, replacement_len {}, array {}".format(index,replacement_len, str_list))
    for i in range(len(str_list)-1, index+3, -1):
        str_list[i] = str_list[i-replacement_len]

    for i in range(replacement_len):
        str_list[index+i] = repl[i]

a = [1,2,' ', 3,' ',4,'','','','','','','']
for i in range(len(a)-1, 0, -1):
    if a[i] == ' ':
        insertIntoString2(a, '%20', i)
print(a)
"""

def countWhiteSpace(a):
    count = 0
    for i in range(len(a)):
        if a[i] == " ":
            count += 1

    return count


a = [1,2,' ', 3,' ',4,'','','','']

trueLength = 6
whitespacecount = countWhiteSpace(a)
totalspace = trueLength + (whitespacecount*2)
index = totalspace
for i in range(trueLength - 1, -1, -1):
    if a[i] == " ":
        a[index - 1] = '0'
        a[index - 2] = '2'
        a[index - 3] = '%'
        index = index -3

    else:
        a[index-1] = a[i]
        index -= 1


print (a)
