REQUIRED PACKAGES (they should be in the virtual environment)
------------------------------------------------------------
pdf2image
pytesseract
Pillow
google-generativeai
-----------------------------------------------------------
External dependencies (Windows)
-----------------------------------------------------------

Poppler – required for pdf2image
Tesseract OCR – required for text extraction
-----------------------------------------------------------
API
-----------------------------------------------------------
Google gemini https://aistudio.google.com/api-keys
-----------------------------------------------------------
HOW TO RUN
-----------------------------------------------------------
Place the PDF in the same folder as main.py.

Run:

py main.py

OUT:

what is your pdf file name?: MyPDF
-----------------------------------------------------------

script will then 

Convert the PDF to images

OCR each image

Write all extracted text to file.txt

Send the text to Gemini

Print flashcards to your terminal
