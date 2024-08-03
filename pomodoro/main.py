from tkinter import *
import math
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
timer = None


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global REPS
    REPS = 0
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    checkmarks.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global REPS
    REPS += 1

    if REPS % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        timer_label.config(fg=RED, text="Break")
    elif REPS % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        timer_label.config(fg=PINK, text="Break")
    else:
        count_down(WORK_MIN * 60)
        timer_label.config(fg=GREEN, text="Work")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer
    count_min = math.floor(count/60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_session = math.floor(REPS/2)
        for _ in range(work_session):
            marks = "✔"
        checkmarks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()


window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(fg=GREEN, bg=YELLOW, text="Timer", font=(FONT_NAME, 50))
timer_label.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
pomodoro_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=pomodoro_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)


start_btn = Button(text="Start", highlightthickness=0, command=start_timer)
start_btn.grid(row=2, column=0)
reset_btn = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_btn.grid(row=2, column=2)

checkmarks = Label(fg=GREEN, bg=YELLOW)
checkmarks.grid(row=3, column=1)

window.mainloo