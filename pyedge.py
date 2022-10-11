'''
pyEdge: a small utility to detect edges in images
It supports three different methods for edge detection: Canny, Sobel and Prewitt
'''
# Import libraries
import matplotlib.pyplot as plt
from skimage.io import imread,imsave
from skimage.filters import sobel, prewitt
from skimage.feature import canny
# TODO:these files should be passed by the user
# If notput filename is passed, it should be generated automatically
input_filename="workshop/nucleoli.png"
output_filename="workshop/nucleoli_edges.png"
# Read images and find edges
img=imread(input_filename)
img_edges=canny(img, sigma=7)
# Save to file
imsave(output_filename,arr=img_edges)
# Display images
fig,ax=plt.subplots(1,2,figsize=(10,5))
ax[0].imshow(img,cmap="gray")
ax[1].imshow(img_edges,cmap="gray")

for a in ax:
    a.axis("off")

plt.show()

