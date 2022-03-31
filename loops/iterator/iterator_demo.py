#   iterator :


nums = [5, 6, 7, 8, 9]
it = iter(nums)
#print(it)
print(it.__next__())
print(it.__next__())

#    or   #

print(next(it))
print(next(it))
