"""4. Write a function that takes a character
 (i.e. a string of length 1)
 and returns True if it is a vowel, False otherwise."""


def test_v(x):
    # if x[0] in "aeiou":
    if x.lower() in ['a', 'e', 'i', 'o', 'u']:
        return True
    else:
        return False


y = test_v("s")
print(y)
z = test_v("o")
print(z)

