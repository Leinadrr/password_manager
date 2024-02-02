from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_pass():
    pass_input.delete(0, "end")
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letters_list = [random.choice(letters) for _ in range(random.randint(8, 10))]
    symbol_list = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    numbers_list = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = letters_list + symbol_list + numbers_list

    random.shuffle(password_list)

    password = "".join(password_list)
    pass_input.insert(0, password)
    pyperclip.copy(password)
    messagebox.showinfo(title="Copied to Clipboard!", message="Password copied to clipboard.")


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_data():
    data_web_input = web_input.get()
    data_user_input = user_input.get()
    data_pass_input = pass_input.get()
    new_data = {
        data_web_input: {
            "email": data_user_input,
            "password": data_pass_input,
        }
    }

    if len(data_web_input) == 0 or len(data_pass_input) == 0:
        messagebox.showwarning(title="Warning!", message="Hey! You need to complete all forms!")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
                # Updating old data with new data
                data.update(new_data)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(new_data, data_file, indent=4)
        else:
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            web_input.delete(0, END)
            pass_input.delete(0, END)
            web_input.focus()


# ------------------------FIND INFORMATION----------------------------------- #


def find_password():
    data_web_input = web_input.get()
    try:
        with open("data.json", mode="r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data File Found")
    else:
        if data_web_input in data:
            messagebox.showinfo(title=data_web_input, message=f"User: {data[data_web_input]['email']} \nPassword: "
                                                              f"{data[data_web_input]['password']}")
        else:
            messagebox.showwarning(title="Warning", message=f"No details for the {data_web_input} existed")


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# -------------------------LABELS---------------------------------- #

website = Label(text="Website:")
website.grid(column=0, row=1)

username = Label(text="Email/Username:")
username.grid(column=0, row=2)

password = Label(text="Password:")
password.grid(column=0, row=3)

# ----------------------ENTRY------------------------------------- #

web_input = Entry(width=33)
web_input.focus()
web_input.grid(column=1, row=1)

user_input = Entry(width=52)
user_input.insert(0, "example@gmail.com")
user_input.grid(column=1, row=2, columnspan=2)

pass_input = Entry(width=33)
pass_input.grid(column=1, row=3)

# ------------------------BUTTONS--------------------------------- #
pass_button = Button(text="Generate Password", command=generate_pass)
pass_button.grid(column=2, row=3)

add_button = Button(width=44, text="Add", command=save_data)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", command=find_password, width=15)
search_button.grid(column=2, row=1)

window.mainloop()
