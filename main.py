import random
from tkinter import *
import pandas
from random import *
BACKGROUND_COLOR = "#B1DDC6"
current_card = None
to_learn = None

# n = randint(0, 100)
def reset_game():
    data_frame = pandas.read_csv("./data/french_words.csv")
    global to_learn
    to_learn = data_frame.to_dict(orient="records")
    french_word_generator()


def french_word_generator():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    canvas.itemconfig(card_image, image=card_front)
    current_card = choice(to_learn)
    french_word = current_card["French"]
    # english_word = data_frame["English"][n]
    canvas.itemconfig(language, text="French", fill="black")
    canvas.itemconfig(word, text=french_word, fill="black")
    flip_timer = window.after(3000, flip_card)
    print(to_learn)

def flip_card():

    canvas.itemconfig(card_image, image=card_back)
    canvas.itemconfig(language, text="English", fill="white")
    canvas.itemconfig(word, text=current_card['English'], fill="white")
    if len(to_learn) > 0:
        to_learn.remove(current_card)

#===================================================Window=============================================================


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, flip_card)
#Images import
card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="./images/card_back.png")
right = PhotoImage(file="./images/right.png")
wrong = PhotoImage(file="./images/wrong.png")

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, border=-1)
canvas.config(highlightthickness=0)
card_image = canvas.create_image(410, 266, image=card_front)
canvas.grid(row=0, column=0, columnspan=2)
language = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))

right_button = Button(image=right, highlightthickness=0, width=100, height=100, border=0, command=french_word_generator)
right_button.grid(row=1, column=1)
wrong_button = Button(image=wrong, highlightthickness=0, width=100, height=100, border=0, command=reset_game)
wrong_button.grid(row=1, column=0)

reset_game()
french_word_generator()


window.mainloop()
