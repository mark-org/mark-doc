
# pillow
https://pillow.readthedocs.io/en/stable/handbook/tutorial.html

```
from PIL import Image
im = Image.open("hopper.ppm")
print(im.format, im.size, im.mode)
# PPM (512, 512) RGB

# Convert files to JPEG
try:
	with Image.open(infile) as im:
		im.save(outfile)
except IOError:
	print("cannot convert", infile)


```