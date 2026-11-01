import sys
import os
import tkinter as tk


def resource_path(relative_path):

     # Используется для упаковки в exe файл
     base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__))) # noqa
     return os.path.join(base_path, relative_path)


def calculate():

    example = entry.get()


    available = set("01234567890+-*/() ")


    clear = ''.join(c for c in example if c in available)


    if clear != example:
        result_label.config(text="Только числа и знаки: 01234567890+-*/()")

        return


    if not clear:
        result_label.config(text="Пустой ввод")

        return


    try:

        result = eval(clear)

        result_label.config(text=f"= {result}")

    except SyntaxError:

        result_label.config(text="Ошибка в примере")

    except ZeroDivisionError:

        result_label.config(text="Деление на ноль недопустимо")



root = tk.Tk()

root.iconbitmap(resource_path("icon.ico"))

root.title("Калькулятор")

root.geometry("400x300")

main_frame = tk.Frame(root, width=300, height=250)
main_frame.place(relx=0.5, rely=0.5, anchor="center")


title = tk.Label(main_frame, text="Введите пример:", font=("Arial", 14))
title.pack(pady=10)

version_label = tk.Label(root, text = "Версия 1.0", font=("Arial", 10), fg="gray")
version_label.place(relx=0.0, rely=1.0, anchor="sw", x=10, y=-10)


entry = tk.Entry(main_frame, font=("Arial", 16), width=20)
entry.pack(pady=10)


button = tk.Button(main_frame, text="Вычислить", font=("Arial", 14), command=calculate)
button.pack(pady=10)


result_label = tk.Label(main_frame, text="", font=("Arial", 14), wraplength=350)
result_label.pack(pady=10)



entry.bind("<Return>", lambda event: calculate())

root.mainloop()






