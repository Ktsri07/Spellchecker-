import tkinter as tk
from tkinter import *
from textblob import *
import nltk
# nltk.download('wordnet')
from nltk.corpus import wordnet
from PIL import Image, ImageTk
import requests
from io import BytesIO
# def login_page():
#     main_window.destroy()
#     import login

def get_synonyms(word):
    synonyms = []
    
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonym = lemma.name().replace("_", " ")
            synonyms.append(synonym)
    
    return list(set(synonyms))[:5]

def check_spelling():
    word = enter_text.get()
    a = TextBlob(word)
    corrected_word = str(a.correct())
    synonyms = get_synonyms(corrected_word)
    
    cs = Label(main_window, text="Correct spelling is: ", justify="center", font=("poppins", 20), bg="black", fg="white")
    cs.place(x=100, y=256)
    
    cs1 = Label(main_window, text="Synonyms are: ", justify="center", font=("poppins", 20), bg="black", fg="white")
    cs1.place(x=100, y=300)
    
    spell.config(text=corrected_word)
    synonyms_label.config(text=", ".join(synonyms))

# BACKGROUND PART
main_window = Tk()
main_window.title("Check the spelling buddy!!")

# Get screen width and height
screen_width = main_window.winfo_screenwidth()
screen_height = main_window.winfo_screenheight()

# Fetch image from Google (replace 'YOUR_GOOGLE_IMAGE_URL' with the actual URL)
image_url = 'https://i.pinimg.com/originals/c8/63/eb/c863eb3621b82b0a0871853e221ef119.jpg'
response = requests.get(image_url)
background_image = Image.open(BytesIO(response.content))
background_image = background_image.resize((screen_width, screen_height))
bg_photo = ImageTk.PhotoImage(background_image)
main_window.iconphoto(False, ImageTk.PhotoImage(file='logo.png'))

# Background Image
bg_label = Label(main_window, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# SPELLING CHECKING PART
heading = Label(main_window, text="WELCOME TO SPELL CHECK!", font=("arial", 25, "italic"), fg="white",bg = "black")
heading2 = Label(main_window, text="Type the word", font=("arial", 20, "italic"), fg="white",bg = "black")

heading.pack(pady=(50, 0))
heading2.pack(pady=(5, 0))

# DATA ENTRY PART
enter_text = Entry(main_window, justify="center", width=30, font=("arial", 25), bg="white", border=2)
enter_text.pack(pady=10)
enter_text.focus()

# BUTTON DEFINING PART
button = Button(main_window, text="Check", font=("arial", 15, "bold"), fg="black", bg="white", command=check_spelling)
button.pack()

spell = Label(main_window, font=("poppins", 20), bg="black", fg="White")
spell.place(x=350, y=256)

synonyms_label = Label(main_window, font=("poppins", 20), bg="black", fg="white")
synonyms_label.place(x=350, y=300)

main_window.mainloop()