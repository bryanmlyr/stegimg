import argparse
import math

from PIL import Image, ImageDraw


def encode(string_to_encode: str):
    image_size = math.ceil(math.sqrt(len(string_to_encode) / 3))

    img = Image.new('RGB', (image_size, image_size), (0, 0, 0))
    draw = ImageDraw.Draw(img)
    i, x, y = 0, 0, 0
    current_color = [0, 0, 0]

    for c in string_to_encode:
        print(c, ord(c))
        current_color[i] = ord(c)

        if i == 2:
            draw.point(xy=(x, y), fill=(current_color[0], current_color[1], current_color[2]))
            current_color = [0, 0, 0]
            i = 0

            if x == image_size - 1:
                y += 1
                x = 0
            else:
                x += 1
        else:
            i += 1

    if current_color != [0, 0, 0]:
        draw.point(xy=(x, y), fill=(current_color[0], current_color[1], current_color[2]))
    img.save('output.png', 'PNG')


def decode(file_path: str) -> str:
    output_text = ''
    img = Image.open(file_path)
    pixels = img.load()
    width, height = img.size

    for x in range(width):
        for y in range(height):
            current_pixel = pixels[y, x]
            if current_pixel[0] != 0:
                output_text += chr(current_pixel[0])
            if current_pixel[1] != 0:
                output_text += chr(current_pixel[1])
            if current_pixel[2] != 0:
                output_text += chr(current_pixel[2])

    return output_text


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Hide ascii text in image\'s pixels.')
    parser.add_argument('-a', '--action', choices=['encode', 'decode'], required=True)
    parser.add_argument('-i', '--input', required=True, help='In action mode encode it should be an ascii string and in decode mode it should be png file path.')
    args = parser.parse_args()

    if args.action == 'encode':
        encode(args.input)
    if args.action == 'decode':
        print(decode(args.input))
