from PIL import Image
import numpy as np

#Image path input
image_path = "1.jpg"

#Image input
img = Image.open(image_path)

#Image compression
size_x = 80
size_y = 300
size = size_x, size_y
img.thumbnail(size)

#Convertation to greyscale
img = img.convert('L')

#Convertation to array
img_array = np.array(img)

#Convertation to ASCII
for i in img_array:
    for j in i:
        j /= 10
        j = int(round(j, 0))
        img_array[i, j] = j

#Final array output
for i in img_array:
    for j in i:
        print(j, " ", end='')
    print()

input()
