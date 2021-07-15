from tkinter import *
from PIL import ImageTk, Image
import random
from tkinter import messagebox


def scissors():
    global computer_choice
    global user_choice
    global computer_choosed
    if computer_choice == 1:
        messagebox.showinfo("Result", "User = "+user_choice +
                            "\nComputer = "+computer_choosed+"\nIts A Draw")
    elif computer_choice == 2:  # rock
        messagebox.showinfo("Result", "User = "+user_choice +
                            "\nComputer = "+computer_choosed+"\nComputer Wins")
    else:
        messagebox.showinfo("Result", "User = "+user_choice +
                            "\nComputer = "+computer_choosed+"\nUser Wins")


def rock():
    global computer_choice
    global user_choice
    global computer_choosed
    if computer_choice == 2:
        messagebox.showinfo("Result", "User = "+user_choice +
                            "\nComputer = "+computer_choosed+"\nIts A Draw")
    elif computer_choice == 3:
        messagebox.showinfo("Result", "User = "+user_choice +
                            "\nComputer = "+computer_choosed+"\nComputer Wins")
    else:
        messagebox.showinfo("Result", "User = "+user_choice +
                            "\nComputer = "+computer_choosed+"\nUser Wins")


def paper():
    global computer_choice
    global user_choice
    global computer_choosed
    if computer_choice == 3:
        messagebox.showinfo("Result", "User = "+user_choice +
                            "\nComputer = "+computer_choosed+"\nIts A Draw")
    elif computer_choice == 1:
        messagebox.showinfo("Result", "User = "+user_choice +
                            "\nComputer = "+computer_choosed+"\nComputer Wins")
    else:
        messagebox.showinfo("Result", "User = "+user_choice +
                            "\nComputer = "+computer_choosed+"\nUser Wins")


def user_value(user_number):
    global computer_choice
    global user_choice
    global computer_choosed
    if user_number == 1:
        user_choice = "Scissors"
    elif user_number == 2:
        user_choice = "Rock"
    else:
        user_choice = "Paper"
    computer_choice = random.randint(1, 3)
    if computer_choice == 1:
        computer_choosed = "Scissors"
    elif computer_choice == 2:
        computer_choosed = "Rock"
    else:
        computer_choosed = "Paper"
    if user_number == 1:
        scissors()
    elif user_number == 2:
        rock()
    else:
        paper()


def start_game():
    start_game = Toplevel()
    start_game.title("Game")
    start_game.geometry('200x250+570+300')
    start_game.resizable(width=0, height=0)
    button_scissors = Button(start_game, text="Scissors", bg="Red",
                             padx=60, pady=10, command=lambda: user_value(1)).pack(pady=10)
    button_rock = Button(start_game, text="Rock", bg="Green", padx=60,
                         pady=10, command=lambda: user_value(2)).pack(pady=10)
    button_paper = Button(start_game, text="Paper", bg="Yellow",
                          padx=60, pady=10, command=lambda: user_value(3)).pack(pady=10)


def rule():
    global rule_image
    rules_window = Toplevel()
    rules_window.title("Rules")
    rules_window.geometry('960x720')
    rules_window.resizable(width=0, height=0)
    rules_window.iconbitmap(r"C:\Users\97798\Desktop\tt_python\Images\rps.ico")
    rule_image = ImageTk.PhotoImage(Image.open(
        r"C:\Users\97798\Desktop\tt_python\GUI\Resource\rules.jpg"))
    display_image = Label(rules_window, image=rule_image).pack()


winodow = Tk()
winodow.title("Rock Paper And Scissors Game")
winodow.state("zoomed")
winodow.resizable(width=0, height=0)
winodow.iconbitmap(r"C:\Users\97798\Desktop\tt_python\GUI\Resource\rps.ico")
# Creating a new winodw


# reszie the image
background_image = Image.open(
    r"C:\Users\97798\Desktop\tt_python\GUI\Resource\rps.jpg")
# reseize
resize = background_image.resize((1350, 600))
background_image = ImageTk.PhotoImage(resize)
display_backgroundimage = Label(winodow, image=background_image).pack()

button_startgame = Button(winodow, text="Start Game",
                          bg="Green", padx=40, command=start_game).pack(pady=5)
button_rule = Button(winodow, text="Rule", bg="Yellow",
                     padx=60, command=rule).pack(pady=5)
button_exit = Button(winodow, text="Exit", bg="red",
                     padx=60, command=winodow.quit).pack(pady=5)


winodow.mainloop()
