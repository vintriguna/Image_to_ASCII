#Created by Vinayak Trigunayat
from PIL import Image
import numpy as np


img = Image.open("Mona_Lisa.jpg")
width, height = img.size
imageData = np.array(img)
for i in range(height):
    for j in range(width):
        x,y,z = imageData[i,j]
        imageData[i,j] = x-1,y-1,z-1 

newImage = Image.fromarray(imageData)
newImage.show()

# #print(len(imageData))
# print(imageData.shape)
# print(width)
# #print(imageData)

