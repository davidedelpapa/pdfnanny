from tkinter import Tk
from tkinter.filedialog import askopenfilename
import PyPDF2
from gtts import gTTS

from pdfnanny import extract

if __name__ == "__main__":

    Tk().withdraw()
    filelocation = askopenfilename()

    print("Opening {}".format(filelocation))

    with open(filelocation, "rb") as f:
        pdfReader = PyPDF2.PdfFileReader(f)

        print("File correctly read.")

        string_of_text = extract.get_text(pdfReader)

        print(
            "\nPreview of text\n-----------\n{}\n-----------\n"
            .format(string_of_text[0:79]))

        final_file = gTTS(text=string_of_text, lang='en')

        print("Audiofile generated. Saving...")

        final_file.save("Generated Speech.mp3")

        print("Done")
