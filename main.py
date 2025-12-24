from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
output = ""
FONT_NAME = "Courier"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project

def generate_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list=[random.choice(symbols) for i in range(nr_symbols)] + [random.choice(letters) for i in range(nr_letters)] + [random.choice(numbers) for i in range(nr_numbers)]
    random.shuffle(password_list)
    password = "".join(password_list)
    pyperclip.copy(password)
    return password

def pass_gen():
    password.delete(0, END)
    new_gen_pass = generate_pass()
    pyperclip.copy(new_gen_pass)
    password.insert(0, new_gen_pass)

def pass_search():

    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror("Error", "Data file does not exist")
    else:

        if web_url.get() in data:
            messagebox.showinfo("Information", f"Website: {web_url.get()}\nEmail: {data[web_url.get()]["email"]}\nPassword: {data[web_url.get()]["password"]}")
        else:
            messagebox.showinfo("Information", f"That doesnt exist")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def search_pass():
    pass_search()


def save_info():
    global output
    websites = web_url.get()
    user_email = username.get()
    user_pass = password.get()
    new_data = { websites : {
        "email" : user_email,
        "password" : user_pass,
    }
    }

    if web_url.get() == "" or username.get() == "" or password.get() == "" or password.get() == "Enter a password or auto generate password.":
        messagebox.showerror("Error", "Fields cannot be empty.")
    else:
        try:
            with open("data.json", "r") as file:
                data = json.load(file)

        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data,file,indent=4)

        else:
            data.update(new_data)
            with open("data.json", "w") as file:
                json.dump(data,file,indent=4)
        finally:

            web_url.delete(0,END)
            password.delete(0, END)
            password.insert(0,"Enter a password or auto generate password.")

# ---------------------------- UI SETUP ------------------------------- #

screen = Tk()
screen.title("Password Manager🔐")
screen.minsize(width=500,height=600)
screen.config(pady=100,padx=100,bg="white")
background_img = PhotoImage(file="logo.png")
canvas = Canvas(width=500, height=300,bg="white",highlightthickness=0)
canvas.create_image(175,150,image=background_img)
canvas.grid(column = 1 ,row =0)

website = Label(text="Website", font=(FONT_NAME, 20),bg="white",fg="black")
website.config(padx=10,pady=10)
website.grid(column=0, row=2)


web_url = Entry(width=35)
web_url.insert(END, string="")
web_url.config(bg="white",fg="black")
web_url_text = web_url.get()
web_url.focus()
web_url.grid(column = 1, row = 2,sticky="w")

search_button = Button(text="Search",command=search_pass,width=15,bg="white",highlightthickness=0,highlightbackground="white")
search_button.config(padx=10,pady=10)
search_button.grid(column = 1, row = 2,sticky="e")

email_user = Label(text="Email/Username", font=(FONT_NAME, 20),bg="white",fg="black")
email_user.config(padx=10,pady=10)
email_user.grid(column=0, row=3)


username = Entry(width=60)
username.insert(END, string="laxsan.jeya@gmail.com")
username.config(bg="white",fg="black")
username_text = username.get()

username.grid(column = 1, row = 3,columnspan=2)

password_label = Label(text="Password", font=(FONT_NAME, 20),bg="white",fg="black")
password_label.config(padx=10,pady=20)
password_label.grid(column=0, row=4)


password = Entry(width=35)
password.insert(END, string="Enter a password or auto generate password.")
password.config(bg="white",fg="black")
password_text = username.get()

password.grid(column = 1, row = 4,sticky="w")

#calls action() when pressed
button = Button(text="Generate Password", command=pass_gen,width=15,bg="white",highlightthickness=0,highlightbackground="white")
button.config(padx=10,pady=10)
button.grid(column = 1, row = 4,sticky="e")

add_button = Button(text="Add", command=save_info, width=35, bg="white", highlightthickness=0, highlightbackground="white")
add_button.config(padx=10,pady=10)
add_button.grid(column = 1, row = 5)

screen.mainloop()