import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
import tkintermapview
def clear_scrollable_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()
def show_map():
    global previous_window
    if previous_window:
        previous_window.destroy()  # Usuń poprzednie okno
    map_window = tk.Toplevel(root)
    map_window.geometry("500x500")
    map_window.title("Map")
    previous_window = map_window

    map_widget = tkintermapview.TkinterMapView(map_window, width=500, height=500, corner_radius=0)
    map_widget.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    map_widget.set_position(52.2297, 21.0122)  # Warsaw/center
    map_widget.set_zoom(6)

    marker_1 = map_widget.set_position(52.2297, 21.0122, marker=True)
    marker_1.set_text("Warsaw centre")  # set new text

    print(marker_1.position, marker_1.text)  # get position and text

    # set a position marker
    marker_2 = map_widget.set_marker(53.516268, 19.377695, text="Hotel nr")
    marker_3 = map_widget.set_marker(52.55, 22.4, text="52.55, 13.4")

    # set a path
    path_1 = map_widget.set_path([marker_1.position, marker_2.position, (52.2297, 21.0122),(53.516268, 19.377695)])


def hotel_list(): #printing results
    clear_scrollable_frame(scrollable_frame)
    for i in range(10):
        text1 = f"Check {i+1} Hotel: "
        add_button = ctk.CTkButton(scrollable_frame, text=text1, width=300, command=show_map)
        add_button.pack(pady=1)

#make global window
root = ctk.CTk()
root.geometry("540x630")
root.title("Search application")

previous_window = None

#setting parameters
title_label = ctk.CTkLabel(root, text="Find route",font=ctk.CTkFont(size=30, weight="bold"))
title_label.pack(padx=10, pady=(40, 20))

label = ctk.CTkLabel(root, text="Select distance range from the list", font=ctk.CTkFont(size=15))
label.pack()

options = ["1-50", "50-100", "100-200", ">200"]
options2 = ["Lake", "Church", "Grocery", "Monument", "Castle"]

combo = ttk.Combobox(root, values=options)
combo.pack(padx=10, pady=(5, 10))

label = ctk.CTkLabel(root, text="Select place, which has to be in max 10km apart from the list", font=ctk.CTkFont(
    size=15))
label.pack()

combo = ttk.Combobox(root, values=options2)
combo.pack(padx=10, pady=(5, 10))

#accepting set parameters and print results
add_button = ctk.CTkButton(root, text="Search", width=80, command=hotel_list)
add_button.pack(pady=10)

scrollable_frame = ctk.CTkScrollableFrame(root, width=450, height=300)
scrollable_frame.pack()

root.mainloop()
