from tkinter import *
from tkinter import filedialog
from gtts import gTTS
from playsound import playsound
import pdfplumber

# ---------------------------- OPEN FILE SETUP ------------------------------- #


def openFile():
    file_location = filedialog.askopenfilename(initialdir=r"F:\python\pythonProject\files",
                                               title="Dialog box",
                                               filetypes=(("pdf files", "*.pdf"),
                                                          ("all files", "*.*")))

    # extracts the text from the pdf file
    pdf_obj = pdfplumber.open(file_location)
    pages = pdf_obj.pages[0]
    pdftext = pages.extract_text()
    print(pdftext)

    # saves file and plays the pdf
    tts = gTTS(text=pdftext, lang='en')
    tts.save('pdf.mp3')
    playsound('pdj.mp3')


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Text to Speech')
window.config(padx=100, pady=100)
open_btn = Button(text="Open", command=openFile)
open_btn.pack()
window.mainloop()

