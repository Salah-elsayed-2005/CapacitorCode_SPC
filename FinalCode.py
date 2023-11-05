import requests
from io import BytesIO

V1i = int(input(" Please Enter the First Capacitor Voltage (in V) :  "))
C1 = int(input(" Please Enter the First Capacitor Capacitance (in μF) :  "))
V2i = int(input(" Please Enter the Second Capacitor Voltage (in V) :  "))
C2 = int(input(" Please Enter the Second Capacitor Capacitance (in μF) : "))

k1 = 1
k2 = 1

temp = int(input("If you want to insert a dielectric for the first capacitor press 1 (otherwise press 0) : "))
if temp == 1:
    k1 = float(input("Please Enter the first dielectric constant : "))

temp = int(input("If you want to insert a dielectric for the second capacitor press 1 (otherwise press 0)  : "))
if temp == 1:
    k2 = float(input("Please Enter the second dielectric constant : "))

Case = 1
qmoves = 0
Q1i = 0
Q2i = 0
Q1 = 0
Q2 = 0

C1 = C1 * k1
C2 = C2 * k2

if V1i and V2i != 0:
    Case = int(input("Enter poles connectivity (1 for similar poles  and 0 for different) : "))

Q1i = C1 * V1i
Q2i = C2 * V2i

if Case == 1:
    if V1i > V2i:
        qmoves = (C2 * Q1i - C1 * Q2i) / (C1 + C2)
        Q1 = Q1i - qmoves
        Q2 = Q2i + qmoves
    else:
        qmoves = (C1 * Q2i - C2 * Q1i) / (C1 + C2)
        Q1 = Q1i + qmoves
        Q2 = Q2i - qmoves

else:
    qmoves = (C1 * Q2i + C2 * Q1i) / (C1 + C2)
    Q1 = Q1i - qmoves
    Q2 = Q2i - qmoves

V1 = Q1 / C1
V2 = Q2 / C2

from PIL import Image, ImageDraw, ImageFont

image_url = "https://drive.google.com/uc?export=download&id=1JCsu-rYGHVbHADn09kUm8qNR82dPdieN"
response = requests.get(image_url)
image = Image.open(BytesIO(response.content))

# Convert the image to RGB mode
image = image.convert("RGB")

# Create a drawing context
draw = ImageDraw.Draw(image)

# initial
text = f"V1b = {V1i:.2f} V\nQ1 = {Q1i:.2f} μq\nC1 = {C1:.2f} μF\n"
text2 = f"V2b = {V2i:.2f} V\nQ2 = {Q2i:.2f} μq\nC2 = {C2:.2f} μF\n"

# final
text11 = f"V2 = {V2:.2f} V\nQ2 = {Q2:.2f} μq\nC2 = {C2:.2f} μF\n"
text12 = f"V1 = {V1:.2f} V\nQ1 = {Q1:.2f} μq\nC1 = {C1:.2f} μF\n"

# poles
text3 = f"++"
text4 = f"--"

text_txt = "The negatvie sign (if there) in the (V or Q)indicates that\n the poles was reversed"
dielec1 = f"Dielectric = {k1}"
dielec2 = f"Dielectric = {k2}"
# Define a larger font size
font_size = 60  # Adjust the size as needed
font_size2 = 80
# Load a font with the specified size
font = ImageFont.truetype("arialbd.ttf", font_size)  # You can use a different font file
font2 = ImageFont.truetype("arialbd.ttf", font_size2)  # You can use a different font file

# text under
position_txt = (50, 1900)

# v,q,c initial for cap 1 bef
position = (20, 1600)

# v,q,c initial for cap 2 bef
position2 = (500, 1600)

# v,q,c initial for cap 1 after
position11 = (1580, 1600)

# v,q,c initial for cap 2 after
position12 = (1100, 1600)

# 3,4,5,6,7,8,9,10 poles
position3 = (165, 860)  # 1
position4 = (170, 970)  # 1

position7 = (850, 860)  # 2
position8 = (850, 970)  # 2

position5 = (1150, 860)  # 3
position6 = (1150, 970)  # 3

position9 = (1830, 860)  # 4
position10 = (1835, 970)  # 4

#position for dielec
position_elec1 = (330,1800) #1
position_elec2 = (1350,1800) #2


text_color = (0, 0, 0)  # RGB color code (white in this example)
text_color2 = (31, 16, 128)  # for values
text_color3 = (175, 175, 0)  # for dielectric
text_color4 = (255, 0, 0) # red
text_color5= (150,75,0) # brown
text_green = (5,182,35) #green
text_blue = (3,76,201)#blue
# Add the text to the image
draw.text(position, text, fill=text_color2, font=font)

# Add the second text to the image
draw.text(position2, text2, fill=text_color2, font=font)

draw.text(position3, text3, fill=text_green, font=font2)
draw.text(position4, text4, fill=text_blue, font=font2)

if (V1 >= 0):
    draw.text(position5, text3, fill=text_green, font=font2)
    draw.text(position6, text4, fill=text_blue, font=font2)
else:
    draw.text(position5, text4, fill=text_blue, font=font2)
    draw.text(position6, text3, fill=text_green, font=font2)

draw.text(position11, text11, fill=text_color2, font=font)
draw.text(position12, text12, fill=text_color2, font=font)

if (Case == 1):
    draw.text(position7, text3, fill=text_green, font=font2)
    draw.text(position8, text4, fill=text_blue, font=font2)

    if (V2 >= 0):
        draw.text(position9, text3, fill=text_green, font=font2)
        draw.text(position10, text4, fill=text_blue, font=font2)
    else:
        draw.text(position9, text4, fill=text_blue, font=font2)
        draw.text(position10, text3, fill=text_green, font=font2)
else:
    draw.text(position7, text4, fill=text_blue, font=font2)
    draw.text(position8, text3, fill=text_green, font=font2)

if (V2 >= 0):
  draw.text(position10, text3, fill=text_green, font=font2)
  draw.text(position9, text4, fill=text_blue, font=font2)
else:
    draw.text(position9, text3, fill=text_green, font=font2)
    draw.text(position10, text4, fill=text_blue, font=font2)

draw.text(position_txt, text_txt, fill=text_color4, font=font)


draw.text(position_elec1, dielec1, fill=text_color5, font=font)
draw.text(position_elec2, dielec2, fill=text_color5, font=font)
# Save the modified image as JPEG
image.save("output_image.jpg")
from PIL import Image

image = Image.open("output_image.jpg")
image.show()