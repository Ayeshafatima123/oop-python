import tkinter as tk
from tkinter import messagebox

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Login GUI")

        tk.Label(root, text="Username").grid(row=0)
        tk.Label(root, text="Password").grid(row=1)

        self.username = tk.Entry(root)
        self.password = tk.Entry(root, show='*')

        self.username.grid(row=0, column=1)
        self.password.grid(row=1, column=1)

        tk.Button(root, text="Login", command=self.login).grid(row=2, column=1)

    def login(self):
        user = self.username.get()
        pwd = self.password.get()
        if user == "admin" and pwd == "123":
            messagebox.showinfo("Login", "Success")
        else:
            messagebox.showerror("Login", "Invalid credentials")

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()
