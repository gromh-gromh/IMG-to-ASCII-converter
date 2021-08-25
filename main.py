from PIL import Image
import numpy as np

#ASCII convertation table
ascii_table = np.array([' ', '.', '~', ':', '"', ';', '!', '+', 'i', 'l', 'I', '?', '*', 'O', '0', 'Q', 'q', 'w', 'm', 'W', 'M', '8', '&', '%', '$', '#', '@'])

#Image path input
image_path = "1.jpg"

#Image input
img = Image.open(image_path)

#Image compression
new_width = 235
width, height = img.size
ratio = height / width / 2
new_height = int(new_width * ratio)
size = new_width, new_height
img = img.resize(size)

#Convertation to greyscale
img = img.convert('L')

#Convertation to array
img_array = np.array(img) // 10

#Convertation to ASCII
ascii_array = ascii_table[img_array]

#Final array output
text_file = open(image_path + "2ASCII.txt", "w")
for i in ascii_array:
    for j in i:
        print(j, end='')
        text_file.write(j)
    text_file.write("\n")
    print()
text_file.close()

input()
