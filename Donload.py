from urllib import request
import sys

myUrl = "https://goodbyefreedom.ru/wp-content/uploads/2021/04/WhatsApp-Image-2021-03-22-at-21.46.52.jpeg"
myFile = "C:\\Users\\n.panichev\\Desktop\\My\\love.jpg"

try:
    print("Start downloading file from: " + myUrl)
    request.urlretrieve(myUrl, myFile)
except Exception:
    print("Error!")
    print(sys.exc_info())
    exit()
print("File downloaded and saves at: "+ myFile)


