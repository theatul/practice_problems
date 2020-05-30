#Given two strings, write a method to decide if one is a permutation of the
#other.

# Sol 1: count all char's of both string and permutation if count is same: O(A+B)
# Not use space? Sort both and compare N LOG N
# can use Const space if the char type is known.

def ComparePermutation(str1, str2):
    if not str1 or not str2:
        return False
    if len(str1)!= len(str2):
        return False

    charCountList = [0]*256

    for i in range(len(str1)):
        charCountList[ord(str1[i]) - ord('a')] += 1

    for i in range(len(str2)):
        charCountList[ord(str2[i])- ord('a')] -= 1 

    for i in range(len(charCountList)):
        if charCountList[i] > 0:
            return False

    return True

print(ComparePermutation("str", "tlss"))