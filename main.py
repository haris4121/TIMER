from tkinter import *
from math import floor
import pygame

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
TIMER = None
window = Tk()


# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def reset_timer():
    global REPS
    global TIMER
    window.after_cancel(TIMER)
    checkMarks.config(text="")
    timerLabel.config(text="Timer")
    canvas.itemconfig(timer_canvas, text="00:00")
    REPS = 0


def start_timer():
    global REPS
    REPS += 1
    if REPS % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        timerLabel.config(text="Break", fg=RED, )
        checkMarks.config(text)
    elif REPS % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        timerLabel.config(text="Break", fg=PINK)
    elif REPS <= 8:
        count_down(WORK_MIN * 60)
        timerLabel.config(text="Work", fg=GREEN)


def count_down(count):
    global TIMER
    minutes = floor(count / 60)
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"
    canvas.itemconfig(timer_canvas, text=f"{minutes} : {seconds}")
    if count > 0:
        TIMER = window.after(1000, count_down, count - 1)
    else:
        play()
        check = ""
        work_sessions = floor((REPS + 1) / 2)
        for _ in range(work_sessions):
            check += "✔"
        checkMarks.config(text=check)
        start_timer()


pygame.mixer.init()


def play():
    pygame.mixer.music.load("Message Tone.mp3")
    pygame.mixer.music.play(loops=0)


# ---------------------------- UI SETUP ------------------------------- #

window.title("pamadoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")  # way to read through file
canvas.create_image(100, 112, image=tomato_img)
timer_canvas = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

timerLabel = Label(window, text="Timer", width=10, fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
timerLabel.grid(row=0, column=1)

startButton = Button(window, text="Start", fg=GREEN, bg=YELLOW, highlightthickness=0, command=start_timer)
startButton.grid(row=2, column=0)

resetButton = Button(window, text="Reset", fg=GREEN, bg=YELLOW, highlightthickness=0, command=reset_timer)
resetButton.grid(row=2, column=2)

checkMarks = Label(window, text="", fg=GREEN, bg=YELLOW)
checkMarks.grid(row=2, column=1)

window.mainloop()
