"""
   Python – Extract Unique values dictionary values

   logic :
          # Python3 code to demonstrate working of
          # Extract Unique values dictionary values
          # Using set comprehension + values() + sorted()
"""

# Method - 1:


def uniqe_vals(di):
    print("The original dictionary is : " + str(di))
    result = list(sorted({ele for val in di.values() for ele in val}))
    return result


di = {"s": [1, 2, 3, 4], "r": [3, 4, 5, 6], "k": [5, 6, 7, 8]}
print("the unique values are:", uniqe_vals(di))



# Method - 2 :

# Python3 code to demonstrate working of
# Extract Unique values dictionary values
# Using chain() + sorted() + values()

from itertools import chain

# initializing dictionary
test_dict = {'gfg' : [5, 6, 7, 8],
			'is' : [10, 11, 7, 5],
			'best' : [6, 12, 10, 8],
			'for' : [1, 2, 5]}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Extract Unique values dictionary values
# Using chain() + sorted() + values()
res = list(sorted(set(chain(*test_dict.values()))))

# printing result
print("The unique values list is : " + str(res))





