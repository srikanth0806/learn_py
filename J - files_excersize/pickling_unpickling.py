import pickle

x = {"std1" : {"name": "naga", "age" : 31}, "std2" : {"name" : "srikanth"}}

#li = [1, 2, 3, 4, 5, 6, 7]

fp = open("test_pickle", "wb")
var = pickle.dump(x, fp)

fp.close()

# var = pickle.dumps(x)
#
# print(var)
#
# var2 = pickle.loads(var)
# print(var2)
