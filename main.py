# L2 DISC Program 2023: Drama Prep

# green #7CDF64
# red #F45866
# off-white #FDF3EC
# off-black #131117

# pink #E8C5D8
# purple #724E91
# yellow #E8C04A


import tkinter as tk

program = tk.Tk()
program.attributes('-fullscreen', True)
program.configure(bg="#E8C5D8")



window = "opening window"



def closeprogram():
    program.destroy()

exit_button = tk.Button(program, command=lambda:closeprogram(), text="exit", padx=10, pady=2, bg="#F45866", fg="#131117", font=("Arial", 25)).place(x=1775, y=40)


def open_window(new_window, old_window):
    global opening_frame
    global info_frame

    if old_window == "opening window":
        opening_frame.destroy()
    elif old_window == "info screen":
        info_frame.destroy()


    if new_window == "opening window":
        window = new_window
        opening_frame = tk.LabelFrame(program, width=1720, height=900, bg="#E2B6CE")
        opening_frame.pack(anchor="nw")
        start_button = tk.Button(opening_frame, command=lambda:closeprogram(), text="start", padx=16, pady=12, bg="#7CDF64", fg="#131117", font=("Arial", 35)).place(x=550, y=680)
        info_button = tk.Button(opening_frame, command=lambda:open_window("info screen", window), text="info", padx=16, pady=12, bg="#E8C04A", fg="#131117", font=("Arial", 35)).place(x=900, y=680)
        intro_text = tk.Label(opening_frame, text="Drama Preperation Program", font=("Arial", 50), bg="#E2B6CE", fg="#131117").place(x=400, y=225)
    elif new_window == "info screen":
        window = new_window
        info_frame = tk.LabelFrame(program, width=1720, height=900, bg="#E2B6CE")
        info_frame.pack(anchor="nw")
        info_text = tk.Label(info_frame, text="Information", font=("Arial", 40), bg="#E2B6CE", fg="#131117").place(x=50, y=50)
        info_back_button = tk.Button(program, command=lambda:open_window("opening window", window), text="back", padx=10, pady=2, bg="#F45866", fg="#131117", font=("Arial", 25)).place(x=100, y=100)


open_window("opening window", "")

program.mainloop()