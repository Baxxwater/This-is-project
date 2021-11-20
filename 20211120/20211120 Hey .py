# pi = 3.14
# r = input("請輸入半徑:")
# r = int(r)
# ans = r**2 *  pi
# print (ans)

# h = float(input("輸入身高(m)"))
# w = int(input("輸入體重"))
# ans = w / h**2
# print(ans)

import matplotlib.pyplot as pyp
import matplotlib.image as age

image = age.imread("20211120\WF_NewWarConceptArt2.jpg")
pyp.imshow(image)
pyp.show()
