import customtkinter as ctk
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import random




# setting up window
root = ctk.CTk()
root.title("Hangman")
root.geometry("650x850")

# creating the photo list
photos = [PhotoImage(file="images/hang0.png"), PhotoImage(file="images/hang1.png"), PhotoImage(file="images/hang2.png"),
PhotoImage(file="images/hang3.png"), PhotoImage(file="images/hang4.png"), PhotoImage(file="images/hang5.png"),
PhotoImage(file="images/hang6.png"), PhotoImage(file="images/hang7.png"), PhotoImage(file="images/hang8.png"),
PhotoImage(file="images/hang9.png"), PhotoImage(file="images/hang10.png"), PhotoImage(file="images/hang11.png"),PhotoImage(file="images/hang12.png")]



# Making Title
title_label = ctk.CTkLabel(root,text="Hangman",font=("Arial",25))

# Making the entry box for letters
answer_entry = ctk.CTkEntry(root,text_color="white")

# creating the wrong counter and the hangman
correct_counter = 0
wrong_counter = 5
hangman_status_img = tk.Label(root)
hangman_status_img.config(image=photos[wrong_counter])


# creating the function to generate the word and making sure that the word isnt the same as the previous word
old_answer = ""
def word_generate():
    global word_list_with2letters
    global old_answer
    global full_answer_list
    global answer_word
    global one_a
    global two_a
    global three_a
    global four_a


    word_list = ["Tech","Ruby","Java","Byte","Code","HTML","Wifi","JSON","YAML","Bash","Perl","Node","Chip","Data","Disk","Logo","Beta"]
    word_list_with2letters = ["Java","Wifi","Data","Logo"]
    answer_word = random.choice(word_list)
    if old_answer == answer_word:
        answer_word = random.choice(word_list)
    old_answer=answer_word
    print(answer_word)
word_generate()



# creatign the Letters and the frame to hold them
letter_box_frame = ctk.CTkFrame(root)

letter_box1 = tk.Label(master=letter_box_frame,text="_",font=("Arial",40))
letter_box2 = tk.Label(master=letter_box_frame,text="_",font=("Arial",40))
letter_box3 = tk.Label(master=letter_box_frame,text="_",font=("Arial",40))
letter_box4 = tk.Label(master=letter_box_frame,text="_",font=("Arial",40))

letter_box1.place(relx = 0.20, rely = 0.5, anchor = CENTER)
letter_box2.place(relx = 0.40, rely = 0.5, anchor = CENTER)
letter_box3.place(relx = 0.60, rely = 0.5, anchor = CENTER)
letter_box4.place(relx = 0.80, rely = 0.5, anchor = CENTER)


# creating a few variables for the functions
a=1
b=1
c=1
d=1


# creating the button function
def reset():
    # declaring global
    global full_answer_list
    global answer_word
    global answer_letters
    global one_a
    global two_a
    global three_a
    global four_a
    global a
    global b
    global c
    global d

    global wrong_counter
    global correct_counter
    tk.messagebox.showinfo(message="Your board has been reset and a word has been generated for you to guess.")
    letter_box1.config(text="_", font=("Arial", 40))
    letter_box2.config(text="_", font=("Arial", 40))
    letter_box3.config(text="_", font=("Arial", 40))
    letter_box4.config(text="_", font=("Arial", 40))
    a = 1
    b = 1
    c = 1
    d = 1
    wrong_counter = 5
    correct_counter = 0
    hangman_status_img.config(image=photos[wrong_counter])
    word_generate()
def click():
    # declaring all the global
    global word_list_with2letters
    global placement
    global wrong_counter
    global correct_counter
    global a
    global b
    global c
    global d



    submit = str(answer_entry.get()).lower()
    if submit == answer_word.lower():
        letter1 = answer_word[0]
        letter2 = answer_word[1]
        letter3 = answer_word[2]
        letter4 = answer_word[3]
        letter_box1.config(text=letter1)
        letter_box2.config(text=letter2)
        letter_box3.config(text=letter3)
        letter_box4.config(text=letter4)
        correct_counter= 4
    # creating the system to make the letters correct
    if submit in answer_word.lower() and submit != answer_word.lower():
        placement = answer_word.lower().index(submit)
        if placement == 0:
            letter_box1.config(text=submit.upper())
            correct_counter +=a
            a=0
        if placement == 1:
            letter_box2.config(text=submit.lower())
            correct_counter += b
            b=0
        if placement == 2:
            letter_box3.config(text=submit.lower())
            correct_counter += c
            c=0
        if placement == 3:
            letter_box4.config(text=submit.lower())
            correct_counter += d
            d=0
        if placement == 1 and answer_word in word_list_with2letters:
            letter_box4.config(text=submit.lower())
            correct_counter += d
            d = 0
    if correct_counter == 4:
        tk.messagebox.showinfo(message="You WIN")



    # creating the hanging system
    if wrong_counter < 12 and submit not in answer_word:
        wrong_counter += 1
    if wrong_counter < 25:
        hangman_status_img.configure(image=photos[wrong_counter])
    if wrong_counter == 11:
        failed_text="Your game is over you have made to many attempts. Your word was: "+answer_word.upper()
        hangman_status_img.configure(image=photos[wrong_counter])
        tk.messagebox.showinfo(title="Game Over", message=failed_text)
        reset()







# Making the Submit Button
submit_button = ctk.CTkButton(root,text_color="white",text="Submit Your Letter",command=lambda: click())

# Making the new game button
new_game_button = ctk.CTkButton(root,text_color="white",text="New Game",command=lambda: reset())




# packing everything
title_label.pack(side="top",anchor="center",pady=15)
hangman_status_img.pack(side="top",anchor="center",pady=(100,15))
letter_box_frame.pack(anchor="center",pady=(50,15))
new_game_button.pack(side="bottom",anchor="center",pady=15)
submit_button.pack(side="bottom",anchor="center",pady=15)
answer_entry.pack(side="bottom",anchor="center",pady=15)



root.mainloop()