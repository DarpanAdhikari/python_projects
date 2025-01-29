from PIL import Image

ASCII_CHARS = "@%#*+=-:. "

def resize_image(image, new_width=100):
    width, height = image.size
    aspect_ratio = height / width
    new_height = int(aspect_ratio * new_width * 0.55)
    resized_image = image.resize((new_width, new_height))
    return resized_image

def grayscale_image(image):
    return image.convert("L")

def image_to_ascii(image, new_width=100):
    image = resize_image(image, new_width)
    image = grayscale_image(image)
    pixels = image.getdata()
    ascii_chars = [ASCII_CHARS[min(pixel // 70, len(ASCII_CHARS) - 1)] for pixel in pixels]
    ascii_image = "".join(ascii_chars)
    return "\n".join(ascii_image[i:i + new_width] for i in range(0, len(ascii_image), new_width))


def main(image_path, output_width=100):
    try:
        image = Image.open(image_path)
        ascii_art = image_to_ascii(image, new_width=output_width)
        print(ascii_art)
    except Exception as e:
        print(f"Error: {e}")

image_path = "../images/darpan.png"
main(image_path, output_width=80)
