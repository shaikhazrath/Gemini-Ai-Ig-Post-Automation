from PIL import Image, ImageDraw, ImageFont

def add_text_to_image(text, text_color=(255, 255, 255), text_size=20, padding=40, line_spacing=10):
    image = Image.open('bg.png')
    image_width, image_height = image.size
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('Roboto-Medium.ttf', text_size)
    lines = []
    line = ''
    for word in text.split():
        test_line = line + word + ' '
        test_line_width, test_line_height = font.getmask(test_line).size
        if test_line_width <= image_width - 2 * padding:
            line = test_line
        else:
            lines.append(line.strip())
            line = word + ' '
    lines.append(line.strip())
    y = (image_height - len(lines) * (text_size + line_spacing) + line_spacing) // 2
    for line in lines:
        line_width, line_height = font.getmask(line).size
        x = (image_width - line_width) // 2
        draw.text((x, y), line, fill=text_color, font=font)
        y += line_height + line_spacing
    image.save('post.png')