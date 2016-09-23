import sys 
from scipy import misc 
from scipy import ndimage



file=sys.argv[1]
image=misc.imread(file)
rotated_image = ndimage.rotate(image,180)
misc.imsave('ans2.png',rotated_image)
