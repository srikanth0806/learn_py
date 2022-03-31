"""14. Write a function find_longest_word()
that takes a list of words and returns the length of the longest one"""


def find_longest_word(li):
    height_word=li[1]
    for i in li:
        if len(i)>len(li[1]):
            height_word = i
            return len(i)


s=find_longest_word(["srikanth","gopi","murali","kondalu"])
print(s)