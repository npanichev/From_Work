from urllib import request
myUrl = "https://www.goodbyefreedom.ru"

otvet = request.urlopen(myUrl)

mytext1 = otvet.readlines()
mytext2 = otvet.read()
print(otvet)
print(mytext2)
for line in mytext1:
    print(line)


