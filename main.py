from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    password = "".join(password_list)
    password_text.insert(0,password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_text.get()
    email = email_text.get()
    password = password_text.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
    }}

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure none of the fields are empty! ")
    else:
        try:
            with open("passwords.json","r") as data:
                data_1 = json.load(data)

        except FileNotFoundError:
            with open("passwords.json","w") as data:
                json.dump(new_data, data, indent=4)
        else:
            data_1.update(new_data)

            with open("passwords.json","w") as data:
                json.dump(data_1, data, indent=4)
        finally:
            website_text.delete(0,END)
            password_text.delete(0,END)

# ---------------------------- FIND PASSWORD ------------------------------- #


def find_password():
    website = website_text.get()
    try:
        with open("passwords.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\n Password: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists")


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("My Password Manager")
window.config(padx=40, pady=40)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100,100, image=logo)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_text = Entry(width=21)
website_text.grid(column=1,row=1)
website_text.focus()

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

email_text = Entry(width=35)
email_text.grid(column=1,row=2,columnspan=2)
email_text.insert(END,"mfrankllin@gmail.com")

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_text = Entry(width=21)
password_text.grid(column=1,row=3)

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3)

search_button = Button(text="Search", width= 13, command=find_password)
search_button.grid(column=2, row=1)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)



window.mainloop()