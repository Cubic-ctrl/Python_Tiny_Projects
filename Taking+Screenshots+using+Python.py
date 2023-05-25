# Create a screen shot App
import pyscreenshot

image = pyscreenshot.grab()
image.show()
image.save("this is image.png")





# Program for partial screenshot
# im=pyscreenshot.grab(bbox=(x1,x2,y1,y2))
image = pyscreenshot.grab(bbox=(10, 10, 500, 500))

# To view the screenshot
image.show()

# To save the screenshot
image.save("image name.png")