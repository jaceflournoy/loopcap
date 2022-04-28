import pyscreenshot as ImageGrab
from pynput.mouse import Listener, Controller, Button
import logging
import time
import random
import os
import img2pdf


mouse = Controller()

logging.basicConfig(filename="mouse_log.txt", level=logging.DEBUG, format='%(asctime)s: %(message)s')

x1 = 0
x2 = 0
y1 = 0
y2 = 0
x3 = 0
y3 = 0

def on_click1(x, y, button, pressed):
    global x1
    global y1
    if pressed:
        x1 = x
        y1 = y
        return False

def on_click2(x, y, button, pressed):
    global x2
    global y2
    if pressed:
        x2 = x
        y2 = y
        return False

def on_click3(x, y, button, pressed):
    global x3
    global y3
    if pressed:
        x3 = x
        y3 = y
        return False


    
def get_first_corner():
        with Listener(on_click=on_click1) as listener:
            print("Enter first corner: ")
            listener.join()
            print(x1, y1)
            return x1, y1

def get_second_corner():
        with Listener(on_click=on_click2) as listener:
            print("Enter second corner: ")
            listener.join()
            print(x2, y2)
            return x2, y2
        
def get_button():
        with Listener(on_click=on_click3) as listener:
            print("Enter button coordinates: ")
            listener.join()
            print(x3, y3)
            return x3, y3

def generate_pdf(directory, filename):
    with open(filename, "wb") as f:
        os.chdir(directory)
        f.write(img2pdf.convert([i for i in os.listdir(os.getcwd()) if i.endswith(".png")]))



first_corner = get_first_corner()
second_corner = get_second_corner()
button = get_button()


num_of_slides = input("Enter total number of slides: ")
directory_question = input("Please input directory input the name of the directory to save the files to: ")
os.mkdir(directory_question)

print("Starting capture session in 5 seconds..")
time.sleep(5)

for slide in range(int(num_of_slides)):
    im=ImageGrab.grab(bbox=(first_corner[0],first_corner[1],second_corner[0],second_corner[1]))
    mouse.position = (button[0], button[1])
    im.save(str(directory_question.lower()) + '/slide' + str(slide) + ".png")
    mouse.press(Button.left)
    mouse.release(Button.left)
    time.sleep(random.randrange(1, 3))


generate_pdf_question = input("Generate PDF? (y/n): ")
if generate_pdf_question.lower() == "y":
    file_name = input("Please enter file name: ")
    if file_name.endswith(".pdf"):
        generate_pdf(directory_question, file_name.lower())
    else:
        generate_pdf(directory_question, str(file_name.lower() + ".pdf"))
else:
    exit()