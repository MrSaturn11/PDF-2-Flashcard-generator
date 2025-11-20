#read the README before trying to use
#remember to paste your key into the key variable
from pdf2image import convert_from_path
import pytesseract
from PIL import Image
from google import genai
key = "AIzaSyAm3pu3I1Yg8Ihu61k6zpPm5CheTYpveyQ"
#pointing to where tesseract.exe is installed on my comptuer
pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
pdf_name = input('what is your pdf file name?:')

# Store Pdf with convert_from_path function
images = convert_from_path(f"{pdf_name}.pdf",poppler_path='C:\\Program Files\\poppler-25.11.0\\Library\\bin')
for i in range(len(images)):
   # Save pages as images in the pdf
  images[i].save('page'+ str(i) +'.jpg', 'JPEG')
#read text in the images
with open("file.txt","w",encoding = "utf-8") as f:
  for i in range(len(images)):
    im_file = f"page{i}.jpg"
    im = Image.open(im_file)
    text = pytesseract.image_to_string(im)
    f.write(text)
with open("file.txt","r",encoding="utf-8") as f:
  contents =f.read()

client = genai.Client(api_key =key )

response = client.models.generate_content(
  model = "gemini-2.0-flash",
  contents=f"""
you are a machine whos only purpose is to create high quality flash cards
RULES FOR CREATING FLASHCARDS:
1. answer should be short and simple, one sentence max
2. only exrract content that seems important
CRITCAL
only respond with plaintext in this format
front:question
back:answer
do not include text other than the question and answer

content to process
{contents}
""")

print(response.text)
