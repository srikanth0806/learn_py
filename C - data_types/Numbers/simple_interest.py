def simple_interest( p, t, r ):
    """
    :param p: principal amount
    :param t: time
    :param r: rate
    :return: simple interest
    """
    si = p*t*r/100
    return si


print(simple_interest(1000, 2, 5))
print(help(simple_interest))




# #write a programe by using userdefined Exception on simple interest programe
# class Simple_Interest(Exception):
#     pass
#
# def s_i( p, t, r ):
#     """
#     :param p: principal amount
#     :param t: time
#     :param r: rate
#     :return: simple interest
#     """
#     try:
#         si = p*t*r/100
#         if si == 0:
#             raise Simple_Interest("the operation is failed")
#     except Simple_Interest as e:
#         print(e)
#     return si
# print(s_i(1000,0,5))
# print(help(s_i))