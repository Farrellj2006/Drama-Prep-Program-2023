"""Drama_P_P 2023 - Jack Farrell"""

from tkinter import Label, LabelFrame, Button, Tk, messagebox, Entry
import random as r

# L2 DISC Program 2023: Drama Prep

# green #7CDF64
# red #F45866
# off-white #FDF3EC
# off-black #131117

# pink #E8C5D8
# purple #724E91
# yellow #E8C04A

# pylint: disable = E1111, E0601, W0601, W0621, C0103

program = Tk()
program.attributes('-fullscreen', True)
program.configure(bg="#E8C5D8")


window = "opening window"
activity_duration = ["please select a length of time",
                     "please select a difficulty"]
activity_duration_options = [
    ["short", "mid-length", "long", "easy", "medium", "hard"],
    ["#7CDF64", "#E8C04A", "#FF7F51", "green", "orange", "red"],
    [[140, 140], [100, 260], [140, 380], [340, 140], [320, 260], [340, 380]]]

activity_options = ["cut lines", "who is your character",
                    "emotion memory recall", "calming circle", "info/tips"]
calming_circle_options = ["colour breathing", "who is watching", ""]
cut_line = ""
letter_list = []
line_cycle = 0
difficulty = 0
prep_time = 0


def closeprogram():
    """This function confirms to close the program when run"""
    quit_conformation = messagebox.askquestion(
        "Exit Confirmation", "are you sure you want to exit?")
    if quit_conformation == "yes":
        program.destroy()


exit_button = Button(program, command=closeprogram, text="exit",
                     padx=10, pady=2, bg="#F45866", fg="#131117", font=("Arial", 25))
exit_button.place(x=1775, y=40)


def close_activity(currentwindow):
    """This function confirms wether the user wants to exit the drama prep"""
    quit_conformation = messagebox.askquestion(
        "Exit Confirmation", "are you sure you want to exit? You will not be able to continue")
    if quit_conformation == "yes":
        open_window("start screen", currentwindow)


def clean_file():
    """Erases text record of drama prep"""
    erase_conformation = messagebox.askquestion(
        "Erase Confirmation", "are you sure you want to erase your \
records contents? You will lose all rcords permanently")
    if erase_conformation == "yes":
        with open("lines.txt", "w", encoding="utf-8") as f:
            f.write("")


def open_window(new_window, old_window):
    """This fuction is called when a new window needs to be opened, and also closes the old one"""
    global opening_frame, info_frame, \
        start_frame, activity_frame, letter_list, line_cycle, activity2_frame, difficulty

    if old_window == "opening window":
        opening_frame.destroy()
    elif old_window == "info screen":
        info_frame.destroy()
    elif old_window == "start screen":
        start_frame.destroy()
    elif old_window == "activity window":
        activity_frame.destroy()
    elif old_window == "activity window":
        activity2_frame.destroy()

    if new_window == "opening window":
        window = new_window

        opening_frame = LabelFrame(
            program, width=1720, height=900, bg="#E2B6CE")
        opening_frame.pack(anchor="nw")

        start_button = Button(opening_frame, command=lambda: open_window("start screen", window),
                              text="start", padx=16, pady=12,
                              bg="#7CDF64", fg="#131117", font=("Arial", 35))
        start_button.place(x=550, y=680)

        info_button = Button(opening_frame, command=lambda: open_window("info screen", window),
                             text="info", padx=16, pady=12,
                             bg="#E8C04A", fg="#131117", font=("Arial", 35))
        info_button.place(x=1000, y=680)

        intro_text = Label(opening_frame, text="Drama Preperation Program", font=(
            "Arial", 50), bg="#E2B6CE", fg="#131117")
        intro_text.place(x=400, y=225)

        clear_records = Button(opening_frame, command=clean_file, text="clear warmup memory",
                               padx=16, pady=12, bg="white", fg="black", font=("Arial", 15))
        clear_records.place(x=1440, y=800)

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
            "opening window", window),
            text="back", padx=10, pady=2, bg="#F45866", fg="#131117", font=("Arial", 25))
        info_back_button.place(x=1500, y=40)

        info_information1 = Label(info_frame, text="""Created by:
                                    Jack Farrell""", font=(
            "Arial", 20), bg="#E2B6CE", fg="#131117")
        info_information1.place(x=1250, y=800)

        info_information2 = Label(info_frame,
                                  text="This program is designed to help users \
to prepare for drama performances",
                                  font=("Arial", 30), bg="#E2B6CE", fg="#131117")
        info_information2.place(x=60, y=300)

        info_information3 = Label(info_frame, text="where they need to be in \
character. To start the program, return to the prevoius window", font=(
            "Arial", 30), bg="#E2B6CE", fg="#131117")
        info_information3.place(x=60, y=350)

        info_information4 = Label(info_frame, text="and press START.", font=(
            "Arial", 30), bg="#E2B6CE", fg="#131117")
        info_information4.place(x=60, y=400)

    elif new_window == "start screen":
        window = "start screen"
        letter_list = []
        start_frame = LabelFrame(
            program, width=1720, height=900, bg="#E2B6CE")
        start_frame.pack(anchor="nw")
        for i in range(len(activity_duration_options[0])):
            activitybutton = Button(
                start_frame, text=activity_duration_options[0][i], padx=16,
                pady=12, bg=activity_duration_options[1][i],
                fg="#131117", font=("Arial", 25),
                command=lambda i=i: select_activity(i, window, activity_duration))
            activitybutton.place(
                x=activity_duration_options[2][i][0], y=activity_duration_options[2][i][1])

        testlabel_text = "length of time for prep: " + \
            activity_duration[0] + \
            "\nDifficulty of prep: " + activity_duration[1]
        testlabel = Label(start_frame, text=testlabel_text)
        testlabel.place(x=60, y=60)

        activitystart_back_button = Button(start_frame, command=lambda: open_window(
            "opening window", window), text="back",
            padx=10, pady=2, bg="#F45866", fg="#131117", font=("Arial", 25))
        activitystart_back_button.place(x=1500, y=40)

        continue_to_rep_button = Button(
            start_frame, text="start prep",
            command=lambda: check_activity(activity_duration, window))
        continue_to_rep_button.place(x=600, y=400)

    elif new_window == "activity window":
        window = "activity window"
        letter_list = []
        activity_frame = LabelFrame(
            program, width=1720, height=900, bg="#E2B6CE")
        activity_frame.pack(anchor="nw")

        activity_back_button = Button(activity_frame, command=lambda: close_activity(window),
                                      text="back", padx=10, pady=2,
                                      bg="#F45866", fg="#131117", font=("Arial", 25))
        activity_back_button.place(x=1500, y=40)

        # for if the activity is "cut lines"
        cut_line_gui = LabelFrame(
            activity_frame, width=1200, height=800, bg="orange")
        cut_line_gui.place(x=50, y=50)

        line_input_label = Label(
            cut_line_gui, text="enter line to learn here: ")
        line_input_label.place(x=50, y=50)
        line_input = Entry(cut_line_gui, width=120)
        line_input.place(x=200, y=50)

        recieve_line = Button(cut_line_gui, text="enter",
                              command=lambda: write_to_lines(line_input, window))
        recieve_line.place(x=60, y=80)

        if line_cycle > difficulty+1:
            open_window("activity window 2", window)

    elif new_window == "activity window 2":
        window = "activity window 2"

        activity2_frame = LabelFrame(
            program, width=1720, height=900, bg="#E2B6CE")
        activity2_frame.pack(anchor="nw")

        activity2_back_button = Button(activity2_frame, command=lambda: close_activity(window),
                                       text="back", padx=10, pady=2,
                                       bg="#F45866", fg="#131117", font=("Arial", 25))
        activity2_back_button.place(x=1500, y=40)

        # elif randactivity == "who is your character":
        # pass
        # elif randactivity == "emotion memory recall":
        # pass
        # elif randactivity == "calming circle":
        # circle_act =  randomizing code here
        # pass
        # elif randactivity == "info/tips":
        # pass


def select_activity(i, window, activity_duration):
    """These butons allow the user to choose how difficult and long they want their prep to be"""
    global difficulty, prep_time
    if i == 0:
        activity_duration[0] = "short"
        prep_time = 2
    elif i == 1:
        activity_duration[0] = "mid-length"
        prep_time = 3
    elif i == 2:
        activity_duration[0] = "long"
        prep_time = 4
    elif i == 3:
        activity_duration[1] = "easy"
        difficulty = 1
    elif i == 4:
        activity_duration[1] = "medium"
        difficulty = 2
    elif i == 5:
        activity_duration[1] = "hard"
        difficulty = 3

    open_window("start screen", window)


def write_to_lines(line_from_input, window):
    """Function to send lines to new line in file"""
    global line_cycle
    cut_line = []
    file_line_input = line_from_input.get()
    print(file_line_input)
    with open("lines.txt", "a", encoding="utf-8") as file:
        file.write("Users line to learn:  " + file_line_input + "\n")
    for letter in file_line_input:
        letter_list.append(letter)
    print(letter_list)
    try:
        no_of_words = r.randint(1, letter_list.count(" ")-1)
    except ValueError:
        messagebox.showerror(
            title=None, message="please add more words to practice")
    # partial line
    for char in letter_list:
        if not no_of_words == 0:
            if not char == ' ':
                cut_line.append(char)
            else:
                no_of_words += -1
                cut_line.append(char)
    cut_line.pop(len(cut_line)-1)
    cut_line = "".join(cut_line)
    print(cut_line)
    line_cycle += 1
    if line_cycle < difficulty+2:
        messagebox.showinfo(
            title=None, message=f"your, line has been inputted, please input {difficulty-line_cycle+2} more")
    else:
        messagebox.showinfo(
            title=None, message=f"your line has been inputted, continuing to the second part of activity...")

    open_window("activity window", window)


def check_activity(selected_activities, window):
    """checks for both activity settings to have a selection and gives error message to user"""
    if selected_activities[0] == "please select a \
length of time" or selected_activities[1] == "please \
select a difficulty":
        messagebox.showerror(
            title=None, message="please select a prep duration and difficulty")
    else:
        confirm_prep = messagebox.askquestion(
            title=None, message="are you sure you want to start the activity(s)?")
        if confirm_prep == "yes":
            open_window("activity window", window)


open_window("opening window", "")


program.mainloop()
