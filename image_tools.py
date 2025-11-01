from PIL import Image

def create_thumbnail(img_path, out_path, size=(320, 480)):
    img = Image.open(img_path)
    img.thumbnail(size)
    img.save(out_path)
