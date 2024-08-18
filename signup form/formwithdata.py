from tkinter import *
import tkinter as tk
from tkinter import messagebox
import mysql.connector
import re

class Form:
    def __init__(self):
        self.window = tk.Tk()
       
        self.window.title("Simple Form")
        self.host = 'localhost'
        self.database = 'signup_db'
        self.user = 'root'
        self.password = 'mysql@123'

        self.cnx = mysql.connector.connect(
            user=self.user,
            password=self.password,
            host=self.host,
            database=self.database
        )
        self.cursor = self.cnx.cursor()
      
        
        self.name_label = tk.Label(self.window, text="Name:")
        self.name_label.grid(row=0, column=0)
        self.name_entry = tk.Entry(self.window)
        self.name_entry.grid(row=0, column=1)

        self.email_label = tk.Label(self.window, text="Email:")
        self.email_label.grid(row=1, column=0)
        self.email_entry = tk.Entry(self.window)
        self.email_entry.grid(row=1, column=1)

        self.submit_button = tk.Button(self.window, text="Submit", command=self.submit_form)
        self.submit_button.grid(row=2, column=0, columnspan=2)

    def validate_name(self, name):
        if len(name) < 2:
            return False
        return True

    def validate_email(self, email):
        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        if re.match(pattern, email):
            return True
        return False

    def submit_form(self):
        name = self.name_entry.get()
        email = self.email_entry.get()

        if not self.validate_name(name):
            messagebox.showerror("Error", "Name should be at least 2 characters long")
            return

        if not self.validate_email(email):
            messagebox.showerror("Error", "Invalid email address")
            return

        messagebox.showinfo("Form Submission", f"Name: {name}\nEmail: {email}")
        
        query = ("INSERT INTO users "
                 "(username, email) "
                 "VALUES (%s, %s)")
        
        try:
            self.cursor.execute(query, (name, email))
            self.cnx.commit()
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error: {err}")
        finally:
            self.cursor.close() 
            self.cnx.close() 

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    form = Form()
    form.run()