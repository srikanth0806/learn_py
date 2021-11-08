

def even(x):
    if x % 2 == 0:
        return True
    else:
        return False


val = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

res = filter(even, val)

print(list(res))