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


# pylint: disable = E1111, E0601, W0601, W0602, W0603, W0621, C0103


# ctrl + f  "what_act"


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


activity_options = [
    "cut lines", "cut lines 2", "emotion memory recall", "info/tips"]


EMR_text = ["This is a drama technique: emotion memory recall.",
            "This technique is used to make your facial expressions more realistic and believable. ",
            """This is an exercise which is reliant
on you following these instructions to the best of your abilities.""",
            "Press the 'ready' button when you are ready to start the exercise",
            "Lets start with something simple",
            "what you need to do is imagine an emotion",
            "example: anger",
            "then try to remember a memory where you have felt this emotion.",
            "Now you must make your: face, body, and mind look and think like they did in "
            "that memory.",
            "Allow those emotions to be your full focus",
            "this is what you must do before going on-stage in character",
            "you must visualise your characters emotions and relate them to a personal experience.",
            "Lets do this a couple more times, but with a different emotion or feeling",
            "When you are ready to leave this activity, press the NEXT button."]

what_act_tips_text = ["These are some final useful tips that will help you in drama performances",
                      "ARRIVE TO THE VENUE ON TIME, this is majorly important",
                      "Make sure to drink plenty of water before a performance",
                      "Always do a vocal warmup for a musical 5-10 minutes before the show",
                      "Physically be prepared for your performance. Stretch!",
                      "make sure to use other warmup methods, which can be found online, alongside this program for the maximum benefits :D"]


# constants, these are not to be modified, the code manipulates these viariables
cut_line = ""
letter_list = []
word_list = []
used_sentences = []
file_line_input = []
completed_activities = []
line_cycle = 0
difficulty = 0
prep_time = 0
EMR_text_num = 0
EMR_round = 0
actnum = 0
what_act_tips_text_num = 0
what_act = ""

# variables

# how many activities are in the program
max_num_of_act = 3


def closeprogram():
    """This function confirms to close the program when run"""
    quit_conformation = messagebox.askquestion(
        "Exit Confirmation", "are you sure you want to exit the program?")
    if quit_conformation == "yes":
        program.destroy()


exit_button = Button(program, command=closeprogram, text="exit",
                     padx=10, pady=2, bg="#F45866", fg="#131117", font=("Arial", 25))
exit_button.place(x=1775, y=40)


def close_activity(currentwindow):
    """This function confirms wether the user wants to exit the drama prep"""
    quit_conformation = messagebox.askquestion(
        "Exit Confirmation", "are you sure you want to go back? You will not be able to continue")
    if quit_conformation == "yes":
        open_window("start screen", currentwindow)


def clean_file():
    """Erases text record of drama prep"""
    erase_conformation = messagebox.askquestion(
        "Erase Confirmation", "are you sure you want to erase your "
        "records contents? You will lose all rcords permanently")
    if erase_conformation == "yes":
        with open("lines.txt", "w", encoding="utf-8") as f:
            f.write("")


def next_EMR_prompt():
    """Go to the next EMR prompt"""
    global EMR_text_num, EMR_round, prep_time

    print(prep_time, " : prep time", EMR_round, " : EMR_round")
    if EMR_text_num == len(EMR_text)-3 and EMR_round > prep_time - 1:
        EMR_text_num = len(EMR_text)-1

    if EMR_text_num == len(EMR_text)-2:
        EMR_text_num = 5
        EMR_round += 1
    else:
        EMR_text_num += 1

    if EMR_round > prep_time:
        next_activity()

    open_window("activity window", "activity window")


def next_tips_prompt():
    """Go to the next tips prompt"""
    global what_act_tips_text_num
    if what_act_tips_text_num == len(what_act_tips_text)-1:
        if actnum == max_num_of_act:
            program.destroy()  # end program nicely

        else:
            what_act_tips_text_num += 1
            open_window("activity window", "activity window")

    else:
        what_act_tips_text_num += 1
        open_window("activity window", "activity window")


def next_activity():
    """takes the user to the next activity"""
    global actnum
    actnum += 1
    if actnum > max_num_of_act:
        program.destroy()
    else:
        pass  # do code to go to next activity


def open_window(new_window, old_window):
    """This fuction is called when a new window needs to be opened, and also closes the old one"""
    global opening_frame, info_frame, start_frame, activity_frame, line_cycle, cut_line_gui, difficulty, prep_time, what_act, str_cut_line, file_line_input, word_list, used_sentences, word_to_use, completed_activities, EMR_text_num, EMR_round, max_num_of_act, actnum

    if old_window == "opening window":
        opening_frame.destroy()
    elif old_window == "info screen":
        info_frame.destroy()
    elif old_window == "start screen":
        start_frame.destroy()
    elif old_window == "activity window":
        activity_frame.destroy()

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
                                  text="This program is designed to help users "
                                  "to prepare for drama performances",
                                  font=("Arial", 30), bg="#E2B6CE", fg="#131117")
        info_information2.place(x=60, y=300)

        info_information3 = Label(info_frame, text="where they need to be in "
                                  "character. To start the program, return to the prevoius "
                                  "window", font=(
                                      "Arial", 30), bg="#E2B6CE", fg="#131117")
        info_information3.place(x=60, y=350)

        info_information4 = Label(info_frame, text="and press START.", font=(
            "Arial", 30), bg="#E2B6CE", fg="#131117")
        info_information4.place(x=60, y=400)

    elif new_window == "start screen":
        window = "start screen"

        letter_list = []
        word_list = []
        used_sentences = []
        file_line_input = []
        EMR_round = 0
        EMR_text_num = 0
        actnum = 0

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

        continue_to_prep_button = Button(
            start_frame, text="start prep",
            command=lambda: check_activity(activity_duration, window))
        continue_to_prep_button.place(x=600, y=400)

    elif new_window == "activity window":
        window = "activity window"

        activity_frame = LabelFrame(
            program, width=1720, height=900, bg="#E2B6CE")
        activity_frame.pack(anchor="nw")

        activity_back_button = Button(activity_frame, command=lambda: close_activity(window),
                                      text="back", padx=10, pady=2,
                                      bg="#F45866", fg="#131117", font=("Arial", 25))
        activity_back_button.place(x=1500, y=40)

        what_act = activity_options[actnum]

        if what_act == "cut lines":
            used_sentences = []
            letter_list = []

            cut_line_gui = LabelFrame(
                activity_frame, width=1200, height=800, bg="#DCA7C4")
            cut_line_gui.place(x=50, y=50)

            line_input_label = Label(
                cut_line_gui, text="enter line to learn here: ")
            line_input_label.place(x=50, y=50)
            line_input = Entry(cut_line_gui, width=120)
            line_input.place(x=200, y=50)

            recieve_line = Button(cut_line_gui, text="enter",
                                  command=lambda: write_to_lines(line_input, window, letter_list))
            recieve_line.place(x=60, y=80)

            if line_cycle > difficulty+1:
                what_act = "cut lines 2"
                open_window("activity window", window)

        elif what_act == "cut lines 2":

            cut_line_gui = LabelFrame(
                activity_frame, width=1200, height=800, bg="#DCA7C4")
            cut_line_gui.place(x=50, y=50)

            word_to_use = r.randint(0, len(word_list)-1)
            if len(word_list) == len(used_sentences):
                messagebox.showinfo(
                    title=None, message="Activity complete. Moving to the next one... ")
                next_activity()
            else:
                while word_to_use in used_sentences:
                    word_to_use = r.randint(0, (len(word_list)-1))

                print(word_list, "   word list")
                print(used_sentences, "   used sentences")
                print(word_to_use, "    word to use")
                used_sentences.append(word_to_use)

                cut_lines_2_back_button = Button(cut_line_gui,
                                                 command=lambda: close_activity(
                                                     window),
                                                 text="back", padx=10, pady=2,
                                                 bg="#F45866", fg="#131117",
                                                 font=("Arial", 25))
                cut_lines_2_back_button.place(x=1500, y=40)
                line_piece = Label(cut_line_gui,
                                   text=f"Please enter the rest of this line: "
                                   f"{word_list[word_to_use]}")
                line_piece.place(x=50, y=300)
                line_piece_input = Entry(cut_line_gui, width=100, bg="white")
                line_piece_input.place(x=400, y=300)
                whole_line_input = Button(cut_line_gui, text="enter",
                                          command=lambda:
                                          check_correct_line(line_piece_input.get(), window))
                whole_line_input.place(x=60, y=80)

        elif what_act == "emotion memory recall":
            window = "emotion memory recall"

            try:
                EMR_instructions = Label(activity_frame, text=EMR_text[EMR_text_num],
                                         padx=10, pady=2, bg="#E2B6CE", fg="#131117",
                                         font=("Arial", 25))
                EMR_instructions.place(x=50, y=50)

                EMR_next_button = Button(activity_frame, command=next_EMR_prompt, padx=10, pady=2,
                                         bg="#E2B6CE", fg="#131117", text="Next",
                                         font=("Arial", 25))
                EMR_next_button.place(x=600, y=200)

            except IndexError:
                next_activity()

        elif what_act == "info/tips":
            what_act_tips = Label(activity_frame, text=what_act_tips_text[what_act_tips_text_num],
                                  padx=10, pady=2, bg="#E2B6CE", fg="#131117",
                                  font=("Arial", 25))
            what_act_tips.place(x=50, y=50)

            what_act_tips_next_button = Button(activity_frame, command=next_tips_prompt, padx=10, pady=2,
                                               bg="#E2B6CE", fg="#131117", text="Next",
                                               font=("Arial", 25))
            what_act_tips_next_button.place(x=600, y=200)


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


def write_to_lines(line_from_input_line, window, letter_list):
    """Function to send lines to new line in file and make a var to compare with later"""
    global line_cycle, str_cut_line, file_line_input, word_list
    cut_line = []
    str_cut_line = ""


# code to filter out incorrect inputs and provide user feedback based on what they did wrong
    if not line_from_input_line.get().count('  ') >= 1:
        if not line_from_input_line.get().count('') == 1:
            if not line_from_input_line.get().count(' ') == 1:
                if not line_from_input_line.get()[-1] == ' ':
                    if line_from_input_line.get().count(' ') >= 3:
                        if not line_from_input_line.get()[0] == ' ':
                            if not line_from_input_line.get() in file_line_input:

                                file_line_input.append(
                                    line_from_input_line.get())
                                print(file_line_input, "    file line input")
                                with open("lines.txt", "a", encoding="utf-8") as file:
                                    file.write("Users line to learn:  " +
                                               file_line_input[-1] + "\n")
                                for letter in file_line_input[-1]:
                                    letter_list.append(letter)
                                try:
                                    no_of_words = r.randint(
                                        1, letter_list.count(" ")-1)

                                    # cut the line into 2 sections
                                    for char in letter_list:
                                        if not no_of_words == 0:
                                            if not char == ' ':
                                                cut_line.append(char)
                                            else:
                                                no_of_words += -1
                                                cut_line.append(char)
                                    str_cut_line = "".join(cut_line)
                                    line_cycle += 1
                                    word_list.append(str_cut_line)
                                    if line_cycle < difficulty+2:
                                        messagebox.showinfo(title=None,
                                                            message="your line has been inputted, "
                                                            "please input "
                                                            f"{difficulty-line_cycle+2} "
                                                            "more")
                                    else:
                                        messagebox.showinfo(title=None,
                                                            message="your line has been inputted, "
                                                            "continuing to the second part of the "
                                                            "activity...")
                                    print(word_list)
                                    open_window("activity window", window)

                                except ValueError:
                                    messagebox.showerror(
                                        title=None, message="please add more words to practice")
                            else:
                                messagebox.showerror(
                                    title=None, message="please input a line different to a "
                                                        "previous one")
                        else:
                            messagebox.showerror(
                                title=None, message="please remove spaces from infront of the line")
                    else:
                        messagebox.showerror(
                            title=None, message="please add more words to practice")
                else:
                    messagebox.showerror(
                        title=None, message="please do not end your input with a space")
            else:
                messagebox.showerror(
                    title=None, message="please enter more words into the entry field")
        else:
            messagebox.showerror(
                title=None, message="please enter multiple words into the entry field")
    else:
        messagebox.showerror(
            title=None, message="please do not type consecutive spaces")
    return letter_list


def check_correct_line(whole_line, currentwindow):
    """checks if the user has inputted the correct line into the entry field"""
    global file_line_input, word_to_use

    if not whole_line.count('  ') >= 1:
        if not whole_line.count('') == 1:
            if not whole_line[-1] == ' ':
                if not whole_line[0] == ' ':

                    if str(word_list[word_to_use] + whole_line) == file_line_input[word_to_use]:
                        messagebox.showinfo(
                            title=None, message="you inputted the line in correctly!")
                    else:
                        messagebox.showwarning(
                            title=None,
                            message="you inputted the line in wrong, "
                            f"the whole line was:   {file_line_input[word_to_use]}")

                    open_window("activity window", currentwindow)

                else:
                    messagebox.showerror(
                        title=None, message="please remove spaces from infront of the line")
            else:
                messagebox.showerror(
                    title=None, message="please do not end your input with a space")
        else:
            messagebox.showerror(
                title=None, message="please enter multiple words into the entry field")
    else:
        messagebox.showerror(
            title=None, message="please do not type consecutive spaces")


def check_activity(selected_activities, window):
    """checks for both activity settings to have a selection and gives error message to user"""
    if selected_activities[0] == "please select a length of time" or \
            selected_activities[1] == "please select a difficulty":
        messagebox.showerror(
            title=None, message="please select a prep duration and difficulty")
    else:
        confirm_prep = messagebox.askquestion(
            title=None, message="are you sure you want to start the activity(s)?")
        if confirm_prep == "yes":
            open_window("activity window", window)


open_window("opening window", "")


program.mainloop()
