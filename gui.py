import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
import tkintermapview

selected_option_1 = None
selected_option_2 = None
hotel_number = None
longtitude = []
latitude = []
distance = []
def clear_scrollable_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()
def show_map(hotel_num):
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

    print(latitude[hotel_num-1]), longtitude[hotel_num-1],  # get position and text

    # set a position marker
    marker_2 = map_widget.set_marker(latitude[hotel_num-1], longtitude[hotel_num-1], text=f"Hotel {hotel_num}")
    #marker_2 = map_widget.set_marker(53.516268, 19.377695, text="Hotel nr")
    #marker_3 = map_widget.set_marker(52.55, 22.4, text="52.55, 13.4")

    # set a path
    path_1 = map_widget.set_path([marker_1.position, marker_2.position, (52.2297, 21.0122), (latitude[hotel_num-1],
                                                                                             longtitude[hotel_num-1]
                                                                                             )])


def hotel_list(): #printing results
    clear_scrollable_frame(scrollable_frame)
    global selected_option_1, selected_option_2

    selected_index_1 = combo1.current()
    selected_index_2 = combo2.current()

    if selected_index_1 >= 0:
        selected_option_1 = options[selected_index_1]
    else:
        selected_option_1 = None
    if selected_index_2 >= 0:
        selected_option_2 = options2[selected_index_2]
    else:
        selected_option_2 = None
    if selected_option_1 == None or selected_option_2 == None:
        title_label = ctk.CTkLabel(scrollable_frame, text="Choose necessary parameters!", font=ctk.CTkFont(size=15,
                                                                                                          weight="bold"))
        title_label.pack(padx=10, pady=(20, 20))
        return

    print(selected_option_1, selected_option_2)
    for i in range(10):
        text1 = f"Check {i+1} Hotel: "
        add_button = ctk.CTkButton(scrollable_frame, text=text1, width=300, command=lambda num=i+1: show_map(num))
    #te dane beda wczytane z backendu
        latitude.append(0.4 * i + 50.5)
        longtitude.append(0.2 * i + 19)
        distance.append(10*i)
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

combo1 = ttk.Combobox(root, values=options, state="readonly")
combo1.pack(padx=10, pady=(5, 10))

label = ctk.CTkLabel(root, text="Select place, which has to be in max 10km apart from the list", font=ctk.CTkFont(
    size=15))
label.pack()

combo2 = ttk.Combobox(root, values=options2, state="readonly")
combo2.pack(padx=10, pady=(5, 10))

#accepting set parameters and print results
add_button = ctk.CTkButton(root, text="Search", width=80, command=hotel_list)
add_button.pack(pady=10)

scrollable_frame = ctk.CTkScrollableFrame(root, width=450, height=300)
scrollable_frame.pack()

root.mainloop()
