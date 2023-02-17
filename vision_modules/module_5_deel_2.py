from skimage.viewer import ImageViewer
import numpy as np
from skimage import data
from skimage.color import rgb2gray
from skimage.viewer import ImageViewer
from skimage import io, color, data
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
from skimage import data
from skimage import transform
from skimage import img_as_float
from skimage import transform as tf
from skimage import data, filters
from skimage.viewer import ImageViewer
import numpy as np
from skimage import io, color, data

image = data.camera()
fig, ax = plt.subplots(3, 2, figsize=(8, 4))

#original foto laten zien
ax[0,0].imshow(image)
ax[0,0].set_title("Original image")

#transform affine
transformers = transform.AffineTransform(
        shear=np.pi/6,
        )
AF_img = transform.warp(image, transformers.inverse )
ax[0,1].imshow(AF_img)
ax[0,1].set_title("Affine Transformation")


#roteren
Rotated_img = transform.rotate(image, 36, resize=True)
ax[1,0].imshow(Rotated_img)
ax[1,0].set_title("Rotated")

#swirl
Swirl_img = transform.swirl(image, strength=100, radius=250)
ax[1,1].imshow(Swirl_img)
ax[1,1].set_title("Swirly")

#strecthen
downscaled_img = transform.downscale_local_mean(image, (8, 3))
ax[2,0].imshow(downscaled_img)
ax[2,0].set_title("stretched")

#transleren
transformers1 = transform.AffineTransform(
         translation=(60, -50)
        )
Transleren_img = transform.warp(image, transformers1.inverse )
ax[2,1].imshow(Transleren_img)
ax[2,1].set_title("Translate")

plt.show()


