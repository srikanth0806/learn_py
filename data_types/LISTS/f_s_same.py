#5. Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings. Go to the editor
#Sample List : ['abc', 'xyz', 'aba', '1221']
def f_s_same(l):
    count=0
    for word in l:
        if len(word)>1 and word[0] == word[-1]:
            count += 1
    return count
print(f_s_same(["ars","jkj","kmk","dsa","mnm"]))