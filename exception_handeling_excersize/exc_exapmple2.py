x = [1,2,4,"naga",45.6]
try:
    for i in range(0,20):
        print(x[i])
        print(x[i]/10)
except TypeError:
    pass
except IndexError:
    pass

# adding some dummy commment