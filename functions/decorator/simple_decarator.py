"""
  write a python programme to implement the simple decorator.
  with sivaparvati.
"""


def beauty_parlour(women):        # ------> function - 1
    def room():
        print("before make up")
        women()
        print("after make up")
    return room


@beauty_parlour                 # --------> it makes a link
def lady():                     # --------> function - 2
    print("i am sivaparvathi")


lady()               # remind: here, some changes are there
                    # that is,  lady = beauty_parlour(lady) --> function calling
                    #            lady()   -----> modified function


#  OR   #     clearly explained below


# def beauty_parlour(women):        # ------> function - 1
#     def room():
#         print("before make up")
#         women()
#         print("after make up")
#     return room
#
#
# def lady():                     # --------> function - 2
#     print("i am sivaparvathi")
#
#
# x = beauty_parlour(lady)
# x()


# below programme is also one of the example.

# def decorator_is_simple(func):
#     def inner():
#         print("hai i am srikanth")
#         func()
#         print("i am a computer graduate.")
#     return inner
#
# @decorator_is_simple
# def my_func():
#     print("i am from tyallur")
