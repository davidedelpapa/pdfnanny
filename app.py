from tkinter import Tk
from tkinter.filedialog import askopenfilename
import PyPDF2
from gtts import gTTS

from pdfnanny import extract, recognize

# Confs
PRETRAINED_MODEL_PATH = 'data/lid.176.ftz'

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
        # Text recognition
        print("Recognizing language... ")
        lang = recognize.get_lang(PRETRAINED_MODEL_PATH, string_of_text)
        print(lang[0][0])
        # TODO generate from tokenized text
        final_file = gTTS(text=string_of_text, lang=str(lang[0][0]))

        print("Audiofile generated. Saving...")
        final_file.save("Generated Speech.mp3")

        print("Done")
