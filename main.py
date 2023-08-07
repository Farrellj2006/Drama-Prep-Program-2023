"""Digital Science Program 2023 - Jack Farrell"""

from tkinter import Label, LabelFrame, Button, Tk, messagebox

# L2 DISC Program 2023: Drama Prep

# green #7CDF64
# red #F45866
# off-white #FDF3EC
# off-black #131117

# pink #E8C5D8
# purple #724E91
# yellow #E8C04A

# pylint: disable = E1111


program = Tk()
program.attributes('-fullscreen', True)
program.configure(bg="#E8C5D8")


window = "opening window"
activity_duration = ["please select a length of time",
                     "please select a difficulty"]
activity_duration_options = [
    ["short", "mid-length", "long", "easy", "medium", "hard"], ["#7CDF64", "#E8C04A", "#FF7F51", "green", "orange", "red"], [[140, 140], [100, 260], [140, 380], [340, 140], [320, 260], [340, 380]]]


def closeprogram():
    """This function closes the program when run"""
    quit_conformation = messagebox.askquestion(
        "Exit Confirmation", "are you sure you want to exit?")
    if quit_conformation == "yes":
        program.destroy()


exit_button = Button(program, command=closeprogram, text="exit",
                     padx=10, pady=2, bg="#F45866", fg="#131117", font=("Arial", 25))
exit_button.place(x=1775, y=40)


def open_window(new_window, old_window):
    global opening_frame, info_frame, start_frame

    if old_window == "opening window":
        opening_frame.destroy()
    elif old_window == "info screen":
        info_frame.destroy()
    elif old_window == "start screen":
        start_frame.destroy()
        # old frame not deleting for activity duration buttons
    if new_window == "opening window":
        window = new_window

        opening_frame = LabelFrame(
            program, width=1720, height=900, bg="#E2B6CE")
        opening_frame.pack(anchor="nw")

        start_button = Button(opening_frame, command=lambda: open_window("start screen", window), text="start", padx=16,
                              pady=12, bg="#7CDF64", fg="#131117", font=("Arial", 35))
        start_button.place(x=550, y=680)

        info_button = Button(opening_frame, command=lambda: open_window("info screen", window), text="info",
                             padx=16, pady=12, bg="#E8C04A", fg="#131117", font=("Arial", 35))
        info_button.place(x=1000, y=680)

        intro_text = Label(opening_frame, text="Drama Preperation Program", font=(
            "Arial", 50), bg="#E2B6CE", fg="#131117")
        intro_text.place(x=400, y=225)

    elif new_window == "info screen":
        window = new_window

        info_frame = LabelFrame(
            program, width=1720, height=900, bg="#E2B6CE")
        info_frame.pack(anchor="nw")
        info_text = Label(info_frame, text="Information", font=(
            "Arial", 40), bg="#E2B6CE", fg="#131117")
        info_text.place(x=0, y=0)
        info_text.place(x=50, y=50)

        info_back_button = Button(program, command=lambda: open_window(
            "opening window", window), text="back", padx=10, pady=2, bg="#F45866", fg="#131117", font=("Arial", 25))
        info_back_button.place(x=1500, y=40)

        info_information1 = Label(info_frame, text="""Created by:
                                    Jack Farrell""", font=(
            "Arial", 20), bg="#E2B6CE", fg="#131117")
        info_information1.place(x=1250, y=800)

        info_information2 = Label(info_frame, text="This program is designed to help users to prepare for drama performances", font=(
            "Arial", 30), bg="#E2B6CE", fg="#131117")
        info_information2.place(x=60, y=300)

        info_information3 = Label(info_frame, text="where they need to be in character. To start the program, return to the prevoius window", font=(
            "Arial", 30), bg="#E2B6CE", fg="#131117")
        info_information3.place(x=60, y=350)

        info_information4 = Label(info_frame, text="and press START.", font=(
            "Arial", 30), bg="#E2B6CE", fg="#131117")
        info_information4.place(x=60, y=400)

    elif new_window == "start screen":
        window = "start screen"
        start_frame = LabelFrame(
            program, width=1720, height=900, bg="#E2B6CE")
        start_frame.pack(anchor="nw")
        for i in range(len(activity_duration_options[0])):
            activitybutton = Button(
                start_frame, text=activity_duration_options[0][i], padx=16,
                pady=12, bg=activity_duration_options[1][i], fg="#131117", font=("Arial", 25), command=lambda i=i: select_activity(i))
            activitybutton.place(
                x=activity_duration_options[2][i][0], y=activity_duration_options[2][i][1])

        testlabel_text = ", ".join(activity_duration)
        testlabel = Label(start_frame, text=testlabel_text)
        testlabel.place(x=60, y=60)


def select_activity(i):
    global activity_duration

    if i == 0:
        activity_duration[0] = "short"
    elif i == 1:
        activity_duration[0] = "mid-length"
    elif i == 2:
        activity_duration[0] = "long"
    elif i == 3:
        activity_duration[1] = "easy"
    elif i == 4:
        activity_duration[1] = "medium"
    elif i == 5:
        activity_duration[1] = "hard"

    open_window("start screen", window)


open_window("opening window", "")

program.mainloop()
