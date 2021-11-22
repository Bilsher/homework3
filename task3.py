import numpy as np
import matplotlib.pyplot as plt
#import math
#from scipy.misc import face

def totalsum(image, y, x, mult=1):
    ts2 = corner(image, y-mult, x) + corner(image, y+mult, x) + corner(image, y, x-mult) + corner(image, y, x+mult) + corner(image, y-mult, x-mult) + corner(image, y+mult, x+mult) + corner(image, y+mult, x-mult) + corner(image, y-mult, x+mult)
    return (ts2)


def corner(image, y, x):
    if(y >= 0 and x >= 0 and y < image.shape[0] and x < image.shape[1]):
        if image[y, x] == 1:
            return 1
    return 0

def objectCount(image):
    count = [0, 0, 0, 0, 0, 0]
    obj = 0
    
    mask1 = np.array([
        [1, 1, 0, 0, 1, 1],
        [1, 1, 0, 0, 1, 1],
        [1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1],
    ])
     
    mask2 = np.array([
        [1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1],
    ])

    for y in range(0, image.shape[0], 2):
        for x in range(0, image.shape[1], 2):
            if image[y, x] == 1:
                c = totalsum(image, y, x, mult=2)
                if c == 4:
                    
                    if corner(image, y-2,x) == 0 and corner(image, y-2,x+2) == 1:
                        count[0] += 1
                    
                    if corner(image, y,x-2) == 0 and corner(image, y-2,x-2) == 1:
                        count[1] += 1
                    
                    if corner(image, y+2,x) == 0 and corner(image, y+2,x-2) == 1:
                        count[2] += 1
                    
                    if corner(image, y,x+2) == 0 and corner(image, y+2,x+2) == 1:
                        count[3] += 1
                        
                if c == 5:
                    
                    if corner(image, y+2, x) + corner(image, y-2, x) == 1:
                        count[4] += 1
                    
                    if corner(image, y, x-2) + corner(image, y, x+2) == 1:
                        count[5] += 1

   
   
    for i in range(len(count) - 2):
        print(mask1)
        obj += count[i]
        print(count[i])
        mask1 = np.rot90(mask1)
    for i in range(4, len(count)):
        print(mask2)
        obj += int(count[i]/2)
        print(int(count[i]/2))
        mask2 = np.rot90(mask2)
    print("Total objects: " + str(obj))



image = np.load("ps.npy").astype("uint")
objectCount(image)


plt.figure(figsize=(6, 6))
plt.subplot(121)
plt.imshow(image)
plt.show()
