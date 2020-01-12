from tkinter import Tk
from tkinter.filedialog import askopenfilename
import PyPDF2
from gtts import gTTS

Tk().withdraw()
filelocation = askopenfilename()

print("Opening {}".format(filelocation))

with open(filelocation, "rb") as f:
    pdfReader = PyPDF2.PdfFileReader(f)

    print("File correctly read.")

    string_of_text = ''
    pages = pdfReader.numPages

    for page in range(0, pages):
        string_of_text += pdfReader.getPage(page).extractText()

    print("{}".format(string_of_text[0:79]))

    final_file = gTTS(text=string_of_text, lang='en')

    print("Audiofile generated. Saving...")

    final_file.save("Generated Speech.mp3")

    print("Done")
