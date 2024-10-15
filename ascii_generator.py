#Created by Vinayak Trigunayat
from PIL import Image
import numpy as np


img = Image.open("Mona_Lisa.jpg")
imageData = np.asarray(img)
print(imageData)

