import re
mail = "hello sir my mail id is tallapallisrikanth1159@gmail.com nafajsGJH67435429ga@gmail.com. kindly revert to" \
       "this mmail id"
y = re.search("[a-zA-Z0-9.]*@[a-zA-Z0-9]+.[a-z]*", mail)
print(y.group())
print(y.groups())

y = re.findall("[a-zA-Z0-9.]*@[a-zA-Z0-9]+.[a-z]*", mail)
print(y)