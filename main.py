import pathlib
from math import sqrt, ceil

from PIL import Image, ImageDraw


FILE = 'book.txt'
path = pathlib.Path().cwd() / 'books' / FILE
print(path)

with open(path, encoding='utf-8', newline='') as f:
    a = f.read()

pixels = len(a) // 3
width = ceil(sqrt(pixels))
COLORS = []
print(f'width: {width}, pixels: {pixels} ')

img = Image.new('RGB', (width, width), 'white')
draw = ImageDraw.Draw(img)

start, stop = 0, 3
for i in range(pixels):
    raw_rgb = a[start:stop]
    rgb = [ord(i) for i in raw_rgb]
    COLORS.append(tuple(rgb))
    start += 3
    stop += 3

pixel_id = 0
for x in range(width):
    for y in range(width):
        try:
            draw.point((y, x), COLORS[pixel_id])
        except IndexError:
            draw.point((y, x), (255, 255, 255))
        pixel_id += 1

img.show()
img.save(FILE[:-3] + 'png')
