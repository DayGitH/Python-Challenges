from PIL import Image

im = Image.open('ch7.png')

print(im)

pixels = list(im.getdata())
x=im.split()
print(x[0])

width, height = im.size
pix2 = []
for i in range(height):
    for j in range(width):
        if i == 50:
            pix2.append(pixels[((i + 1) * (j + 1)) - 1])
            print(pixels[((i + 1) * (j + 1)) - 1])
            
im2 = Image.merge('RGB', (pix2, pix2, pix2))