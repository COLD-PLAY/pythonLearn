from PIL import Image, ImageFilter
from PIL import ImageDraw, ImageFont
import random
from tkinter import *
import tkinter.messagebox as messagebox

print('===============PIL=============')
# im = Image.open('image\image.jpg')
# w, h = im.size
# print('Original image size: %sx%s' % (w, h))
# im.thumbnail((w//2, h//2))
# print('Resize image to: %sx%s' % (w//2, h//2))

# im.save('image\thumbnail.jpg', 'jpeg')

# im = Image.open('image\image.jpg')
# im2 = im.filter(ImageFilter.BLUR)
# im2.save('image\blur.jpg', 'jpeg')

# def rndChar():
# 	return chr(random.randint(65, 90))

# def rndColor():
# 	return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

# def rndColor2():
# 	return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

# width = 60*4
# height = 60
# image = Image.new('RGB', (width, height), (255, 255, 255))
# create Font object
# font = ImageFont.truetype('font\Arial.ttf', 36)
# create Draw object
# draw = ImageDraw.Draw(image)
# fill all pixel
# for x in range(width):
# 	for y in range(height):
# 		draw.point((x, y), fill = rndColor())

# output font
# for t in range(4):
# 	draw.text((60 * t + 10, 10), rndChar(), font = font, fill = rndColor2())

# blur
# image = image.filter(ImageFilter.BLUR)
# image.save('image\code.jpg', 'jpeg')

print('==============GUI程序============')

class Application(Frame):
	def __init__(self, master = None):
		Frame.__init__(self, master)
		self.pack()
		self.createWidgets()

	def createWidgets(self):
		# self.helloLabel = Label(self, text = 'Hello, world!')
		# self.helloLabel.pack()
		# self.quitButton = Button(self, text = 'Quit', command = self.quit)
		# self.quitButton.pack()
		self.nameInput = Entry(self)
		self.nameInput.pack()
		self.alertButton = Button(self, text = 'Hello', command = self.hello)
		self.alertButton.pack()

	def hello(self):
		name = self.nameInput.get() or 'world'
		messagebox.showinfo('Message', 'Hello, %s' % name)

app = Application()
# set title of window
app.master.title('Hello World!')
# loop of main message
app.mainloop()