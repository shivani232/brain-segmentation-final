from sklearn import skimage
from PIL import Image

path = "brain3.jpg" # Your image pa v th 
img = Image.open(path)
skimage.util.random_noise(img, mode='gaussian', seed=None, clip=True, **kwargs)
img.save('noised.jpg')