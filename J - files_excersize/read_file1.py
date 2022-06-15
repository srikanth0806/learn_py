fp = open("test5.txt", "r")
a = fp.read()
print(a)
def r_key_text(var):
    drum = dict()
    #max=dict()
    passage = var.split()
    print(passage)
    for i in passage:
        if i in drum:
            drum[i] += 1
        else:
            drum[i] = 1
    new_dict = drum.copy()

    emp = dict()
    values = sorted(list(new_dict.values()), reverse=True)[0:5]
    print(values)
    for i in values:
        try:
            for j in new_dict:
                if new_dict[j]==i:
                    emp[j]=i

                    new_dict.pop(j)
                    break
        except RuntimeError:
            pass
    print(emp)




mywords_count=r_key_text(a)
print(mywords_count)
