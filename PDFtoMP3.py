import pdfplumber
from gtts import gTTS

try:
    pdf = pdfplumber.open("path-to-/document.pdf") #Writing the full path to the pdf file
    text = ""
    print("Starting processing...")
    for page in pdf.pages:
        text += page.extract_text()
        print("Processing the page ", page)
except pdfplumber.exceptions.PDFSyntaxError:
    print("Error: Invalid PDF file")
    exit()

print("Processing completed")
tts = gTTS(text, lang='ru') #Instead of "ru", we specify the language that you need
tts.save("path-to-/document.mp3") #We are writing the full path where we will save the MP3
print("mp3 file saved")
