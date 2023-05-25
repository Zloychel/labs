from PIL import Image
def z1():
    img = Image.open("1.jpg")
    crop = img.crop((1,100,300,400))
    crop.save("cropped.jpg")
    crop.show("cropped.jpg")

def z2():
    from PIL import Image, ImageFont, ImageDraw
    gallery = {"1":"1.jpg", "2":"2.jpg", "3":"3.jpg"}
    number = input("Какую открытку? ")
    name = input("Кого поздравляем? ")
    k = gallery.keys()
    user = ()
    for i in k:
        if str(number) == i:
            key = i
            user = gallery.get(key)
    with Image.open(user) as img:
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("arial.ttf", 150)
        draw.text((60, 50), name, (0, 77, 255), font=font)
        img.save("new.jpg")
        img.show()
z2()