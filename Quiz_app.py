from tkinter import *
from tkinter import messagebox

root = Tk()

root.title("Quiz Maker")

root.geometry("600x400")

quiz_data = [

    {
        "question":"What is the capital of France?",
        "options":["Paris","London","Berlin","Rome"],
        "answer":"Paris"
    },

    {
        "question":"Which language is used in Data Science?",
        "options":["Python","HTML","CSS","JavaFX"],
        "answer":"Python"
    },

    {
        "question":"2 + 2 = ?",
        "options":["3","4","5","6"],
        "answer":"4"
    }

]

current_question = 0

score = 0

selected_option = StringVar()

question_label = Label(
    root,
    text="",
    font=("Arial",14),
    wraplength=500
)

question_label.pack(pady=20)

radio_buttons = []

for i in range(4):

    rb = Radiobutton(
        root,
        text="",
        variable=selected_option,
        value=""
    )

    rb.pack(anchor="w")

    radio_buttons.append(rb)

def display_question():

    q = quiz_data[current_question]

    question_label.config(text=q["question"])

    selected_option.set(None)

    for i in range(4):

        radio_buttons[i].config(
            text=q["options"][i],
            value=q["options"][i]
        )

def next_question():

    global current_question
    global score

    answer = selected_option.get()

    if answer == quiz_data[current_question]["answer"]:

        score += 1

    current_question += 1

    if current_question < len(quiz_data):

        display_question()

    else:

        show_result()

def show_result():

    messagebox.showinfo(
        "Result",
        f"Your Score: {score}/{len(quiz_data)}"
    )

    root.destroy()

Button(
    root,
    text="Next",
    command=next_question
).pack(pady=20)

display_question()

root.mainloop()