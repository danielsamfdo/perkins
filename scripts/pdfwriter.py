import subprocess
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
import difflib
def keySimilar(text,config):
  res = difflib.get_close_matches(text, config.keys())
  if(len(res)>0):
    return res[0]
  return -1
  lst = [i.split(" ")lower() for i in config.keys()]
  lst = map(lambda x:x.lower(),lst)
  comp = map(lambda x:x.lower(), text.split(" "))

config = {"Given Name": "daniel sam pete", "family name": "thiyagu", "address 1": "81 belchertown road", "address 2": "", "house": "159", "Postcode": "01002", "Country": "United States", "City": "Amherst", "Gender": "Male", "Height": "160"}
img = Image.open("ocrImage.png")
draw = ImageDraw.Draw(img)
font = ImageFont.truetype("Aaargh/Aaargh.ttf", 40)
print subprocess.check_output(['tesseract','ocrImage.png','tmp','hocr'])
soup = BeautifulSoup(file("tmp.hocr").read(), "html.parser")
mydivs = soup.findAll("span", {"class": "ocr_line"})
for i in mydivs:
  text = " ".join(i.findAll(text=True,recursive=True))
  text = text.strip(' \t\n\r')
  if(len(text) > 0):
    pos = i['title'].split(";")[0].split(" ")[3:]
    print text, pos
    simK = keySimilar(text,config)
    if(simK==-1):
      continue
    else:
      print config[simK]
      draw.text((int(pos[0])+50, int(pos[1])-20),config[simK],"blue",font)

img.save('sample-out.jpg')