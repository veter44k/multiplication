import tkinter as tk
import random

def check_answer():
    global question_number, correct_answers
    user_answer = entry.get()
    if user_answer and user_answer.isdigit():
        user_answer = int(user_answer)
        if user_answer == num1 * num2:
            result_label.config(text="\nМолодец!")
            root.after(1000, clear_label)
            correct_answers += 1
        else:
            result_label.config(text="\nНеправильно!")
            root.after(1000, clear_label)
    else:
        result_label.config(text="\nНужно вводить цифру!")
        root.after(1000, clear_label)

    question_number += 1
    if question_number <= 10:
        generate_question()
    else:
        entry.config(state='disabled')
        check_button.config(state='disabled')
        entry.unbind('<Return>')
        score_label.config(text="Итого: %s / 10" % correct_answers)

def generate_question():
    global num1, num2, timeout_id
    if timeout_id is not None:
        root.after_cancel(timeout_id)
    num1 = random.randint(2, 9)
    num2 = random.randint(2, 9)
    question_label.config(text='#%s: \n \n %s x %s = ' % (question_number, num1, num2), font=("Helvetica", 12, "bold"))
    entry.delete(0, tk.END)
    timeout_id = root.after(10000, handle_timeout)

def handle_timeout():
    global question_number
    question_number += 1
    result_label.config(text="\nВремя вышло!")
    root.after(1000, clear_label)
    if question_number <= 10:
        generate_question()
    else:
        entry.config(state='disabled')
        score_label.config(text="Итого: %s / 10" % correct_answers)

def reset_game():
    global question_number, correct_answers
    question_number = 1
    correct_answers = 0
    score_label.config(text='')
    entry.config(state='normal')
    check_button.config(state='normal')
    entry.bind('<Return>', on_enter)
    generate_question()

def on_enter(event):
    check_answer()

def clear_label():
    result_label.config(text='')

question_number = 1
correct_answers = 0
num1 = 0
num2 = 0
timeout_id = None

root = tk.Tk()
root.title("Таблица умножения")

window_width = 300
window_height = 250
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = int((screen_width / 2) - (window_width / 2))
y_coordinate = int((screen_height / 2) - (window_height / 2))
root.geometry(f'{window_width}x{window_height}+{x_coordinate}+{y_coordinate}')

question_label = tk.Label(root, text='')
question_label.pack()

entry = tk.Entry(root)
entry.pack()
entry.focus_set()

check_button = tk.Button(root, text="Проверить ответ", command=check_answer)
check_button.pack()

reset_button = tk.Button(root, text="Сброс", command=reset_game)
reset_button.pack()

result_label = tk.Label(root, text='')
result_label.pack()

score_label = tk.Label(root, text='')
score_label.pack()

generate_question()

entry.bind('<Return>', on_enter)

root.mainloop()