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

def insertIntoString(str_list, char, index):

    for i in range(len(str_list)-1, index, -1):
        str_list[i] = str_list[i-1]

    str_list[index] = char

#TODO: Dry run
"""

[1,2,3,' ',4,5,6,7, '', '', '']
index = 3 loop 10 - 5
[1,2,3,' ',4,5,6,7, '', '', '7']
[1,2,3,%,2,0,4,5, 6, 7]
"""

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
