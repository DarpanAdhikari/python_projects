from PIL import Image
import imagehash

image1 = Image.open('../images/darpan.png')
image2 = Image.open('../images/dar1.png')

hash1 = imagehash.average_hash(image1)
hash2 = imagehash.average_hash(image2)

cutoff = 5

if hash1 - hash2 < cutoff:
    print("images are similar")
else:
    print("images are not similar")