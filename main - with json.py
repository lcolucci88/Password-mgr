from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_passwd():
    pass_entry.delete(0,END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for n in range(random.randint(8, 10))]
    password_numbers = [random.choice(letters) for n in range(random.randint(2, 4))]
    password_symbols = [random.choice(letters) for n in range(random.randint(2, 4))]
    password_list = password_letters + password_numbers + password_symbols
    random.shuffle(password_list)
    pass_entry.insert(END, string="".join(password_list))
    pyperclip.copy("".join(password_list))



# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_passwd():
    website = website_entry.get()
    email = email_entry.get()
    password = pass_entry.get()
    new_data= {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror(title="Some fills are empty", message="Please fill all the fields and retry")
    else:
        try:
            with open("readme.json", mode="r") as file:
                data= json.load(file)
        except FileNotFoundError:
            with open("readme.json", mode="w") as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)
            with open("readme.json", mode="w") as file:
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0,END)
            pass_entry.delete(0,END)

# ----------------------------Search Password -------------------------- #
def search_passwd():
    try:
        website_search = website_entry.get()
        with open("readme.json", mode="r") as file:
            data = json.load(file)
        email_search = data[website_search]["email"]
        password_search = data[website_search]["password"]
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="There are no passwords saved yet")
    except KeyError:
        messagebox.showinfo(title=f"{website_search}", message="There is no password saved for that website")
    else:
        messagebox.showinfo(title=f"{website_search}", message=f"Email: {email_search}\nPassword: {password_search}")

# ---------------------------- UI SETUP ------------------------------- #

window= Tk()
window.title("Password Manager")
window.config(bg="white", padx=25, pady=25)


canvas= Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100,100, image=logo_img)
canvas.config(bg="white", highlightthickness=0)
canvas.grid(row=0, column= 1)

website_label = Label(text= "Website: ")
website_label.config(bg="white")
website_label.grid(row=1, column= 0)


email_label = Label(text= "Email/Username: ")
email_label.config(bg="white")
email_label.grid(row=2, column= 0)


pass_label = Label(text= "Password: ")
pass_label.config(bg="white")
pass_label.grid(row=3, column= 0)

website_entry = Entry(width=36)
website_entry.focus()
website_entry.grid(row=1, column= 1, sticky="w")

email_entry = Entry(width=55)
email_entry.insert(END, string="lucianoc@email.com")
email_entry.grid(row=2, column= 1, columnspan=2, sticky="w")

pass_entry = Entry(width=36)
pass_entry.grid(row=3, column= 1, sticky="w")

add_button = Button(text= "Add")
add_button.config(bg="white", width=50, command=save_passwd)
add_button.grid(row=4, column= 1, columnspan=2, sticky="w")

generator_button = Button(text= "Generate Password")
generator_button.config(bg= "white", width=15, command=generate_passwd)
generator_button.grid(row=3, column= 2, sticky="w")

search_button = Button(text= "Search")
search_button.config(bg= "white", width=15, command=search_passwd)
search_button.grid(row=1, column= 2, sticky="w")

window.mainloop()