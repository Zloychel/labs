from PIL import Image, ImageFilter
def z1():
    filename = "arnold.jpg"
    with Image.open(filename) as img:
        img.load()

    img.show()
    width, height = img.size

    format = img.format

    mode = img.mode

    print("Ширина: ", width)
    print("Высота: ", height)
    print("Формат: ", format)
    print("Цветовая модель: ", mode)

def z2():
    filename = "arnold.jpg"
    with Image.open(filename) as img:
        img.load()

    new_img=img.resize((img.width // 3, img.height // 3))
    new_img.save("resized_arnold.jpg")
    new_img.show()

    new_img=img.rotate(180)
    new_img.save("rotate_arnold.jpg")
    new_img.show()

    new_img = img.transpose(Image.FLIP_LEFT_RIGHT)
    new_img.save("glass_arnold.jpg")
    new_img.show()

def z3():
    filename = ("1.jpg", "2.jpg", "3.jpg")

    for i in filename:
        with Image.open(i) as img:
            new_img=img.filter(ImageFilter.EMBOSS)
            new_img.show()
            new_img.save("filter/" + str(i))

def z4():
    water = "watermark.png"
    with Image.open(water) as img_water:
        img_water.load()

    filename = "arnold.jpg"
    with Image.open(filename) as img:
        img.load()

    img.paste(img_water, (77,77), img_water)
    img.show()
    img.save("watermark_arnold.jpg")


z3()
z4()