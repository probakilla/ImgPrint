import Image

class ImageConverter(object):
  def __init__(self, filename):
    self.filename = filename

  def img_to_txt(self, factor):
    img = Image.open(self.filename)
    img = img.convert('RGB')
    width, height = img.size
    with open('output.txt', 'w+') as file:
      for y in range(0, height, factor):
        for x in range(0, width, factor):
          pixel = img.getpixel((x, y))
          r,g,b = pixel
          brightness = sum([r,g,b])/3
          file.write(self._char_from_brightness(brightness))
        file.write('\n')

  def _char_from_brightness(self, brightness):
    if brightness < 50:
      return ' '
    elif brightness < 100:
      return '.'
    elif brightness < 150:
      return 'o'
    elif brightness < 200:
      return 'O'
    else:
      return 'X'

  def img_to_img(self):
    img = Image.open(self.filename)
    img.convert('RGB')
    width, height = img.size
    dst = Image.new('RGB', img.size)
    for x in range(width):
      for y in range(height):
        pixel = img.getpixel((x, y))
        dst.putpixel((x, y), pixel)
    dst.save('tmp.jpg')