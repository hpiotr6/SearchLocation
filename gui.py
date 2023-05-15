import customtkinter as ctk
import tkinter as tk
from tkinter import ttk

def search_todo():
    label = ctk.CTkLabel(scrollable_frame, text="Done", font=ctk.CTkFont(size=45))
    label.pack(fill="x")

root = ctk.CTk()
root.geometry("800x800")
root.title("Search application")

title_label = ctk.CTkLabel(root, text="Find route",font=ctk.CTkFont(size=30, weight="bold"))
title_label.pack(padx=10, pady=(40, 20))

label = ctk.CTkLabel(root, text="Select distance range in kilometers", font=ctk.CTkFont(size=15))
label.pack()

options = ["1-50", "50-100", "100-200", ">200"]
options2 = ["Lake", "Church", "Grocery", "Monument", "Castle"]

combo = ttk.Combobox(root, values=options)
combo.pack(padx=10, pady=(5, 10))

label = ctk.CTkLabel(root, text="Select place, which has to be in max 10km apart", font=ctk.CTkFont(size=15))
label.pack()

combo = ttk.Combobox(root, values=options2)
combo.pack(padx=10, pady=(5, 10))

add_button = ctk.CTkButton(root, text="Search", width=80, command=search_todo)
add_button.pack(pady=10)

scrollable_frame = ctk.CTkScrollableFrame(root, width=500, height=200)
scrollable_frame.pack()

label = ctk.CTkLabel(scrollable_frame, text="Results:", font=ctk.CTkFont(size=15))
label.pack(fill="x")

root.mainloop()



# def main():
#     print("Hello, world!")
#
#
# if __name__ == '__main__':
#     main()
