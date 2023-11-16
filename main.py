from PIL import Image
from turtle import *

f = open('out.py', 'w')

f.write(
    "from turtle import *\n"
    "penup()\n"
    "tracer(False)\n"
    "hideturtle()\n"
    "def drawPixel(x,y,hexcolor):\n"
    "   setpos(x,y)\n"
    "   dot(1,hexcolor)\n"
)

def rgb_to_hex(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

def toggle_tracer():
    tracer(True)
    tracer(False)



hideturtle()
penup()
speed(0)
screensize(500,500)
tracer(False)

image = Image.open("pinkfloyd_dsotm.png", 'r')
im = image.resize((200,315))
width, height = im.size
pixel_values = list(im.getdata())

startingposx = 0 - width//2
startingposy = 0 - height//2
x = 0
y = 0
i = 0

for x in range(0, width):
    for y in range(0, height):
        r, g, b, a = im.getpixel((x,-y))
        hexcolor = rgb_to_hex(r, g, b)
        setpos( (startingposx + x), (startingposy + y) )
        dot(1,hexcolor)
        i += 1
        if i % 5000 == 0:
            toggle_tracer()
        f.write(
            "drawPixel(" + str(startingposx + x) + "," + str(startingposy + y) + ",\"" + hexcolor + "\")\n"
        )

f.write("exitonclick()\n")

f.close()

exitonclick()
