import fitz
from pdfminer.high_level import extract_text
from gtts import gTTS
from typing import Optional

def audio_handeling(filename, text):
    audio_filename = filename.split('.')[0] + '.mp3'
    audio = gTTS(text=text,lang_check=True)
    audio.save(audio_filename)

def extextract_text_(filename, page: Optional[list]=None):
    if filename.endswith('.pdf'):
        pages = page if page is not None else [page for page in range(fitz.open(filename).page_count+1)]
        text = extract_text(filename,page_numbers=pages)
    else:
        with open(filename,'r') as file:
            text = file.read()
    audio_handeling(filename, text)
    print(f"{filename} is saved !")


extextract_text_("short.txt")