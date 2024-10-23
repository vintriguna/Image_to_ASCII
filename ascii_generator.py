#Created by Vinayak Trigunayat
from PIL import Image
import numpy as np


def printASCII(grayVal):
    if (grayVal >= 0 and grayVal < 25):
        return("#")
    elif (grayVal >= 25 and grayVal < 50):
        return("@")
    elif (grayVal >= 50 and grayVal < 75):
        return("$")
    elif (grayVal >= 75 and grayVal < 100):
        return("%")
    elif (grayVal >= 100 and grayVal < 125):
        return("=")
    elif (grayVal >= 125 and grayVal < 150):
        return("*")
    elif (grayVal >= 150 and grayVal < 175):
        return(":")
    elif (grayVal >= 175 and grayVal < 200):
        return("\"")
    elif (grayVal > 200 and grayVal <= 225):
        return(".")
    else:
        return(" ")


img = Image.open("Mona_Lisa.jpg")
grayImg = img.convert("L")
width, height = grayImg.size
grayImg = grayImg.resize((width // 8, height // 8))
width, height = grayImg.size
imageData = np.array(grayImg)
print(imageData)

f = open("ascii.txt", "w")

for i in range(height):
    for j in range(width):
        f.write(printASCII(imageData[i][j]))
    f.write("\n")

f.close()
    #print("\n")

# for i in range(height):
#     for j in range(width):
#         x,y,z = imageData[i,j]
#         if ()
#     print("\n")        

# for i in range(height):
#     for j in range(width):
#         x,y,z = imageData[i,j]
#         imageData[i,j] = x-1,y-1,z-1 

# newImage = Image.fromarray(imageData)
# newImage.show()

# #print(len(imageData))
# print(imageData.shape)
# print(width)
# #print(imageData)

