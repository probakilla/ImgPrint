from img_print import ImageConverter

if __name__ == "__main__":
  converter = ImageConverter("index.jpg")
  converter.img_to_txt(5)
  print('Finished')