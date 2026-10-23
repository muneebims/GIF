from PIL import Image


filenames = ["00.jpg", "01.jpg", "02.jpg", "10.jpg", "11.jpg"
             , "12.jpg", "20.jpg", "21.jpg", "22.jpg"]

images = []

for filename in filenames:
    image = Image.open(filename)
    images.append(image)

images[0].save(
    "sasuke.gif",
    save_all=True,
    append_images=images[1:],
    duration=250,
    loop=0
)