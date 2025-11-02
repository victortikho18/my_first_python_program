
""""
import imageio.v3 as iio
from PIL import Image

filenames = ['photos/20251023_125234.jpg', 'photos/20251023_125540.jpg']
images = [ ]

  img = Image.open(filename)
  img = img.rotate(90, expand=True)
  images.append(iio.imread(filename))

iio.imwrite('team.gif', images, duration = 500, loop = 0)
"""

import imageio.v3 as iio
from PIL import Image

filenames = ['photos/20251023_125234.jpg', 'photos/20251023_125540.jpg']
images = []

for filename in filenames:
    img = Image.open(filename)
    img = img.rotate(90, expand=True)
    images.append(img)

iio.imwrite('team.gif', images, duration=500, loop=0)
