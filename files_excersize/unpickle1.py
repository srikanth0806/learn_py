import pickle

l = [1, 2, 3, 3, 4, 5, 56, 7 ]
fp = open("test_pickle1", "rb")
var = pickle.load(fp)
fp.close()
print(var)

