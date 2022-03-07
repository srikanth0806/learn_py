import pickle

l = [1, 2, 3, 3, 4, 5, 56, 7]
fp = open("test_pickle1", "wb")


var = pickle.dump(l, fp)
fp.close()

