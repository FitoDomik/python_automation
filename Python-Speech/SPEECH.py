import PyPDF2
import pyttsx3
pdfReader = PyPDF2.PdfFileReader(open('dummypdf.pdf', 'rb'))
speaker = pyttsx3.init()
for page_num in range(pdfReader.numPages):
    text =  pdfReader.getPage(page_num).extractText()
    speaker.say(text)
    speaker.runAndWait()
speaker.stop()
speaker.save_to_file(text, 'audio.mp3')
string = "Lorem Ipsum is simply dummy text " \
    + "of the printing and typesetting industry."
engine = pyttsx3.init()
engine.save_to_file(string, 'speech.mp3')
engine.runAndWait()