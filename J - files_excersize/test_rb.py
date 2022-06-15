fp = open("image1.jpg", "rb+")
fp2 = open("tree1.jpeg", "wb+")

fp2.write(fp.read())
fp.close()
fp2.close()
