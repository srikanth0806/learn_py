"""
    Python Program to Delete an Element From a Dictionary
"""

# by using the methods

def del_item(di):
    print(di)
    # popitem() method
    x = di.popitem()
    # pop() method in directory
    y = di.pop(2)
    print(di)
    # deletion values are stored in x and y which are returned in tuple form
    return x, y


print(del_item({1:"srikanth", 2:"gopi",  3:"murali"}))



# by Using del keyword


my_dict = {31: 'a', 21: 'b', 14: 'c'}

del my_dict[31]

print(my_dict)
