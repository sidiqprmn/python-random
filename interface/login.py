import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage

def login():
    username = entry_username.get()
    password = entry_password.get()
    print("Username:", username)
    print("Password:", password)

root = tk.Tk()
root.title("Form Login")
root.geometry("300x200")  # Ukuran jendela

# CSS style untuk tampilan login
style = ttk.Style()
style.configure("TFrame", background="#f2f2f2")
style.configure("TLabel", background="#f2f2f2", font=("Helvetica", 12, "bold"), foreground="black")
style.configure("TEntry", background="white", font=("Helvetica", 12))
style.configure("TButton", background="#0085fe", font=("Helvetica", 12, "bold"), foreground="white")

# Frame utama
main_frame = ttk.Frame(root, style="TFrame")
main_frame.pack(padx=20, pady=20)

# Logo di atas form
logo_img = PhotoImage(file="logo.png")  # Ganti "logo.png" dengan nama file logo/gambar Anda
logo_label = ttk.Label(main_frame, image=logo_img)
logo_label.pack(pady=10)

label_username = ttk.Label(main_frame, text="Username:")
label_username.pack()
entry_username = ttk.Entry(main_frame)
entry_username.pack()

label_password = ttk.Label(main_frame, text="Password:")
label_password.pack()
entry_password = ttk.Entry(main_frame, show="*")
entry_password.pack()

button_login = ttk.Button(main_frame, text="Login", command=login)
button_login.pack(pady=15)

root.mainloop()
