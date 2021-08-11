import random
import PIL
from PIL import Image

value = random.randint(0,1)
val2 = random.randint(0,1)

if value == 1:
    background = Image.open("./sprites/backgrounds/purple_background.png")

else:
    background = Image.open("./sprites/backgrounds/green_background.png")


if val2 == 0:
    main_image = Image.open("./sprites/main_images/other.png")

elif val2 == 1:
     main_image = Image.open("./sprites/main_images/test.png")

background.paste(main_image, (0,0), main_image)
background.show()



