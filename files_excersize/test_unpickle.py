import pickle

fp = open("test_pickle", "rb")

var = pickle.load(fp)
fp.close()

print(var)

print(type(var))