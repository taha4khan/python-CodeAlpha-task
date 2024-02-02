#image to sound

import os
from gtts import *
from playsound import playsound

tts = gTTS ("tsts visible AI speech")
audioFile_tts = "bother.mp3"
tts.save(audioFile_tts)
#os.system('start' + audioFile_tts)
playsound(audioFile_tts)
#os.remove(audioFile_tts)


import pytesseract as pyt
from PIL import Image
import cv2
from gtts import gTTS
from playsound import playsound

# Set the path for tesseract if necessary
pyt.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Open the image and perform OCR
img = Image.open("sample.png")
extracted_text = pyt.image_to_string(img)
print(extracted_text)

# Convert the extracted text to speech and save it as an mp3 file
tts = gTTS(text=extracted_text, lang='en')
audio_file = "extracted_text.mp3"
tts.save(audio_file)

# Display the image using OpenCV
img_task = cv2.imread('sample.png')
cv2.imshow('Display', img_task)
cv2.waitKey(7000)
#cv2.destroyAllWindows()

# Auto-play the saved audio file
#pip install playsound
playsound(audio_file)

