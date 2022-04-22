from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- GLOBAL VARIABLES ------------------------------- #
reps = 0


# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    """Calls the count_down() & pass the corresponding time duration values"""
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # If it is the 8th repetition, take a long break
    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break", fg=RED)
    # Otherwise, take a short break
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)
    # Back to work
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    """Updates the text value of the canvas text (over the tomato image)"""
    # Compute the minutes of the count value, return the largest whole number that is <= the float number
    count_min = math.floor(count / 60)

    # Compute the seconds of the count value
    count_sec = count % 60
    # Use Python's dynamic typing to convert the 0 second to 00 format
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    # Display the countdown timer in the minutes:seconds format
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    # To prevent from counting down to the negative value
    if count > 0:
        # Calls itself after 1 second, pass count - 1 as parameter & loop through the function itself
        window.after(1000, count_down, count - 1)
    else:
        # Once done counting down, call the start_timer() again for the corresponding breaks between sessions
        start_timer()

        # After every work session, add a ✔
        marks = ""
        work_sessions = math.floor(reps/2)

        for _ in range(work_sessions):
            marks += "✔"

        check_marks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Add a timer label widget
title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)

# Add a canvass widget
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
# Add the tomato image at the center of the canvas
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
# Add some text over the tomato image
timer_text = canvas.create_text(100, 135, text="00:00", fill="white", font=(FONT_NAME, 28, "bold"))

canvas.grid(column=1, row=1)

# Add a start button widget
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

# Add a reset button widget
reset_button = Button(text="Reset", highlightthickness=0)
reset_button.grid(column=2, row=2)

# Add a check mark widget
check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

window.mainloop()
