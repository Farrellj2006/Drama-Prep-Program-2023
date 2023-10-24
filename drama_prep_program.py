"""Drama Prep Program 2023 - Jack Farrell"""


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

# pylint: disable = E1111, E0601, W0601, W0602, W0603, W0621, C0103, C0209

# constants, these are not to be modified, the code manipulates these viariables

# Tkinter base
program = Tk()
program.attributes('-fullscreen', True)
program.configure(bg="#E8C5D8")

window = "opening window"

activity_duration = ["please select a length of time",
                     "please select a difficulty"]

# base variable setting
cut_line = ""
letter_list = []
word_list = []
used_sentences = []
file_line_input = []
line_cycle = 0
difficulty = 0
prep_time = 0
EMR_text_num = 0
EMR_round = 0
actnum = 0
what_act_tips_text_num = 0
what_act = ""

# variables that can be modified

# max_num_of_act =
# <how many activities are in the program (in the 'activity_options' list)>
max_num_of_act = 3

activity_options = [
    "cut lines", "emotion memory recall", "info/tips"]

# 'what_act_tips_text' are the provided tips at the end of the program
what_act_tips_text = ["These are some final useful tips that will help you "
                      "in drama performances",
                      "ARRIVE TO THE VENUE ON TIME, this is majorly important",
                      "Make sure to drink plenty of water before a performance",
                      "Always do a vocal warmup for a musical "
                      "5-10 minutes before the show",
                      "Physically be prepared for your performance. Stretch!",
                      "make sure to use other warmup methods, which can be\n"
                      "found online, alongside this program for the\n"
                      "maximum benefits :D"]

# Emotion Memory Recall text
EMR_text = ["This is a drama technique: emotion memory recall.",
            "This technique is used to make your facial expressions more "
            "realistic and believable. ",
            "This is an exercise which is reliant on you following these "
            "instructions to the best of your abilities.",
            "Press the 'ready' button when you are ready to start the exercise",
            "Lets start with something simple",
            "what you need to do is imagine an emotion",
            "example: anger",
            "then try to remember a memory where you have felt this emotion.",
            "Now you must make your: face, body, and mind look and think like "
            "they did in that memory.",
            "Allow those emotions to be your full focus",
            "this is what you must do before going on-stage in character",
            "you must visualise your characters emotions and relate them to a "
            "personal experience.",
            "Lets do this a couple more times, but with a different "
            "emotion or feeling",
            "When you are ready to leave this activity, press the NEXT button."]

# button names and colours for difficulty and length of time selection
activity_duration_options = [
    ["short", "mid-length", "long", "easy", "medium", "hard"],
    ["#7CDF64", "#E8C04A", "#FF7F51", "#7CDF64", "#E8C04A", "#FF7F50"],
    [[140, 140], [100, 260], [140, 380], [340, 140], [320, 260], [340, 380]]]

# exit the-whole-program button code


def closeprogram():
    """This function confirms to close the program when run"""

    quit_conformation = messagebox.askquestion(
        "Exit Confirmation", "are you sure you want to exit the program?")
    if quit_conformation == "yes":
        with open("report.txt", "a", encoding="utf-8") as file:
            file.write("\n----End of Session----\n\n")
        program.destroy()


exit_button = Button(program, command=closeprogram, text="exit",
                     padx=10, pady=2, bg="#F45866", fg="#131117",
                     font=("Arial", 25))
exit_button.place(x=1775, y=40)

# exit activity button


def close_activity(currentwindow):
    """This function confirms wether the user wants to exit the drama prep"""

    quit_conformation = messagebox.askquestion(
        "Exit Confirmation",
        "are you sure you want to go back? You will not be able to continue")
    if quit_conformation == "yes":
        open_window("start screen", currentwindow)


def clean_file():
    """resets the contents of the 'report.txt' file"""

    erase_conformation = messagebox.askquestion(
        "Erase Confirmation", "are you sure you want to erase your "
        "records contents? You will lose all rcords permanently")
    if erase_conformation == "yes":
        with open("report.txt", "w", encoding="utf-8") as emptf:
            emptf.write("")

            # put 'Session Start' text back, as it gets cleared
        with open("report.txt", "a", encoding="utf-8") as file:
            file.write("\n----Session Start----\n----Start of Prep----\n")


def next_EMR_prompt():
    """Go to the next Emotion Memory Recall text prompt"""
    global EMR_text_num, EMR_round, prep_time

    if EMR_text_num == len(EMR_text)-3 and EMR_round > prep_time - 1:
        EMR_text_num = len(EMR_text)-1

    # reset the text and do another round
    if EMR_text_num == len(EMR_text)-2:
        EMR_text_num = 5
        EMR_round += 1
    else:
        EMR_text_num += 1

    # when enough rounds are completed, go to next activity
    if EMR_round > prep_time:
        next_activity()

    open_window("activity window", "activity window")


def next_tips_prompt():
    """Go to the next tips/info prompt"""
    global what_act_tips_text_num

    what_act_tips_text_num += 1
    open_window("activity window", "activity window")


def next_activity():
    """takes the user to the next activity"""
    global actnum
    actnum += 1
    if actnum > max_num_of_act:
        program.destroy()
    else:
        open_window("activity window", "activity window")


def open_window(new_window, old_window):
    """This fuction is called when a new window needs to be opened or when a
    current window needs to be updated"""

    global opening_frame, info_frame, start_frame, activity_frame, cut_line_gui
    global line_cycle, difficulty, prep_time, what_act, str_cut_line
    global file_line_input, word_list, used_sentences, word_to_use
    global EMR_text_num, EMR_round, max_num_of_act
    global actnum, what_act_tips_text_num
    # remove the old window
    if old_window == "opening window":
        opening_frame.destroy()
    elif old_window == "info screen":
        info_frame.destroy()
    elif old_window == "start screen":
        start_frame.destroy()
    elif old_window == "activity window":
        activity_frame.destroy()

    # open the desired window
    if new_window == "opening window":
        window = new_window

        opening_frame = LabelFrame(
            program, width=1720, height=900, bg="#E2B6CE")
        opening_frame.pack(anchor="nw")

        # button to start drama prep
        start_button = Button(opening_frame,
                              command=lambda: open_window("start screen",
                                                          window),
                              text="start", padx=16, pady=12,
                              bg="#7CDF64", fg="#131117", font=("Arial", 35))
        start_button.place(x=550, y=680)

        # button to get info on the program
        info_button = Button(opening_frame,
                             command=lambda: open_window(
                                 "info screen", window),
                             text="info", padx=16, pady=12,
                             bg="#E8C04A", fg="#131117", font=("Arial", 35))
        info_button.place(x=1000, y=680)

        # name of the program
        intro_text = Label(opening_frame, text="Drama Preparation Program",
                           font=("Arial", 50), bg="#E2B6CE", fg="#131117")
        intro_text.place(x=400, y=225)

        # allows user to clear the contents of the 'report.txt' file
        clear_records = Button(opening_frame, command=clean_file,
                               text="clear warmup memory",
                               padx=16, pady=12, bg="white",
                               fg="black", font=("Arial", 15))
        clear_records.place(x=1440, y=800)

        # reset all constants for the end of the prep
        letter_list = []
        word_list = []
        used_sentences = []
        file_line_input = []
        line_cycle = 0
        difficulty = 0
        prep_time = 0
        EMR_text_num = 0
        EMR_round = 0
        actnum = 0
        what_act = ""
        what_act_tips_text_num = 0

        # declare in the txt file that a new prep has started
        with open("report.txt", "a", encoding="utf-8") as file:
            file.write("----Start of Prep----\n")

    elif new_window == "info screen":
        window = new_window

        info_frame = LabelFrame(
            program, width=1720, height=900, bg="#E2B6CE")
        info_frame.pack(anchor="nw")

        info_text = Label(info_frame, text="Information", font=(
            "Arial", 40), bg="#E2B6CE", fg="#131117")
        info_text.place(x=50, y=50)

        info_back_button = Button(program, command=lambda: open_window(
            "opening window", window),
            text="back", padx=10, pady=2, bg="#F45866", fg="#131117",
            font=("Arial", 25))
        info_back_button.place(x=1500, y=40)

        info_information1 = Label(info_frame, text="Created by: Jack Farrell\n",
                                  font=("Arial", 20), bg="#E2B6CE",
                                  fg="#131117")

        info_information1.place(x=1250, y=800)

        info_information2 = Label(info_frame,
                                  text="This program is designed to help users "
                                  "to prepare for drama performances\n"
                                  "where they need to be in "
                                  "character. To start the program, "
                                  "return to the prevoius "
                                  "window.\n"
                                  "and press START. \n\n"
                                  "This program is designed "
                                  "to be ased alongside other "
                                  "warmup methods",
                                  font=("Arial", 30), bg="#E2B6CE",
                                  fg="#131117")
        info_information2.place(x=60, y=300)

    elif new_window == "start screen":
        window = "start screen"

        # reset all possible constant varibales
        letter_list = []
        word_list = []
        used_sentences = []
        file_line_input = []
        EMR_round = 0
        EMR_text_num = 0
        actnum = 0
        what_act_tips_text_num = 0

        start_frame = LabelFrame(
            program, width=1720, height=900, bg="#E2B6CE")
        start_frame.pack(anchor="nw")

        # create the difficulty and duration buttons
        for i in range(len(activity_duration_options[0])):
            activitybutton = Button(
                start_frame, text=activity_duration_options[0][i], padx=16,
                pady=12, bg=activity_duration_options[1][i],
                fg="#131117", font=("Arial", 25),
                command=lambda i=i: select_activity(i, window,
                                                    activity_duration))
            activitybutton.place(
                x=activity_duration_options[2][i][0],
                y=activity_duration_options[2][i][1])

        time_duration_info_lable = Label(start_frame, text=str(
            "Length of time for prep: " + activity_duration[0] +
            "\nDifficulty of prep: " + activity_duration[1]),
            bg="#E2B6CE", font=('Arial', 14))
        time_duration_info_lable.place(x=60, y=60)

        # back button that only closes the activity
        activitystart_back_button = Button(start_frame,
                                           command=lambda:
                                           open_window("opening window",
                                                       window),
                                           text="back", padx=10, pady=2,
                                           bg="#F45866", fg="#131117",
                                           font=("Arial", 25))

        activitystart_back_button.place(x=1500, y=40)

        # continue button
        continue_to_prep_button = Button(
            start_frame, text="start prep",
            command=lambda: check_activity(activity_duration, window),
            font=('Arial', 16), bg="#7CDF64")
        continue_to_prep_button.place(x=600, y=426)

        # give user direction
        if not old_window == "start screen":
            messagebox.showinfo(title=None, message="Select an excersise"
                                " duration and difficulty, then press\n"
                                "'Start Prep'")

    elif new_window == "activity window":
        letter_list = []
        window = "activity window"
        # to check for the end of the program
        try:
            # select the next activity from 'activity_options'
            what_act = activity_options[actnum]

            activity_frame = LabelFrame(
                program, width=1720, height=900, bg="#E2B6CE")
            activity_frame.pack(anchor="nw")

            # back button that only closes the activity
            activity_back_button = Button(activity_frame,
                                          command=lambda:
                                          close_activity(window),
                                          text="back", padx=10, pady=2,
                                          bg="#F45866", fg="#131117",
                                          font=("Arial", 25))
            activity_back_button.place(x=1500, y=40)

            # create the activity's screen based on what activity is next
            if what_act == "cut lines":

                cut_line_gui = LabelFrame(
                    activity_frame, width=1200, height=800, bg="#DCA7C4")
                cut_line_gui.place(x=50, y=50)

                # label to tell user to input a line from a script
                # into the entry field
                line_input_label = Label(cut_line_gui,
                                         text="enter line to learn here: ",
                                         font=('Arial', 20),
                                         bg="#DCA7C4")
                line_input_label.place(x=50, y=50)
                # the entry field
                line_input = Entry(cut_line_gui, width=60, font='Arial 15')
                line_input.place(x=80, y=100)

                # button to enter the contents of the entry field
                recieve_line = Button(cut_line_gui, text="enter",
                                      command=lambda:
                                      write_to_lines(line_input, window,
                                                     letter_list),
                                      font=('Arial', 14),
                                      bg="#7CDF64")
                recieve_line.place(x=120, y=200)

                # give user direction
                if not old_window == "activity window":
                    messagebox.showinfo(title=None, message="enter a"
                                        " line from your script.\n"
                                        "make sure it has over 3 words")

                if line_cycle > difficulty+1:
                    # 2nd part of the 'cut lines' activity

                    # reload the page
                    cut_line_gui.destroy()

                    cut_line_gui = LabelFrame(
                        activity_frame, width=1200, height=800, bg="#DCA7C4")
                    cut_line_gui.place(x=50, y=50)

                    # pick a piece of one of the lines the user entered
                    word_to_use = r.randint(0, len(word_list)-1)
                    # if all of the user's entered lines are completed
                    if len(word_list) == len(used_sentences):
                        messagebox.showinfo(
                            title=None, message="Activity complete. "
                            "Moving to the next one... ")
                        next_activity()
                        # give user direction
                        messagebox.showinfo(title=None, message="Read"
                                            " the instructions and"
                                            " then press the\n"
                                            "'Next Prompt' button")
                    else:
                        # if selected line has already been used, pick a new one
                        while word_to_use in used_sentences:
                            word_to_use = r.randint(0, (len(word_list)-1))

                        # save that this new line is used
                        used_sentences.append(word_to_use)

                        # back button that only closes the activity
                        cut_lines_2_back_button = Button(cut_line_gui,
                                                         command=lambda:
                                                         close_activity(
                                                             window),
                                                         text="back", padx=10,
                                                         pady=2,
                                                         bg="#F45866",
                                                         fg="#131117",
                                                         font=("Arial", 25))
                        cut_lines_2_back_button.place(x=1500, y=40)

                        # tells user what to do
                        line_piece = Label(cut_line_gui,
                                           text="Please fill in the rest of "
                                           "this line: "
                                           f"{word_list[word_to_use]}",
                                           font=("Arial", 20),
                                           bg="#DCA7C4")
                        line_piece.place(x=50, y=80)
                        # the entry field for the user
                        # to type the rest of the line into
                        line_piece_input = Entry(
                            cut_line_gui, width=60, bg="white",
                            font='Arial 15')
                        line_piece_input.place(x=170, y=150)
                        # confirmation button for what the user has typed
                        whole_line_input = Button(cut_line_gui, text="enter",
                                                  command=lambda:
                                                  check_correct_line(
                                                      line_piece_input.get(),
                                                      window),
                                                      font=('Arial', 14),
                                                      bg="#7CDF64")
                        whole_line_input.place(x=100, y=200)
            elif what_act == "emotion memory recall":
                window = "emotion memory recall"
                # to check for the end of the EMR script in 'EMR_text'
                try:
                    EMR_instructions = Label(activity_frame,
                                             text=EMR_text[EMR_text_num],
                                             padx=10, pady=2, bg="#E2B6CE",
                                             fg="#131117",
                                             font=("Arial", 25))
                    EMR_instructions.place(x=80, y=100)

                    # show the next prompt/text
                    EMR_next_button = Button(activity_frame,
                                             command=next_EMR_prompt,
                                             padx=10, pady=2,
                                             bg="#E2B6CE", fg="#131117",
                                             text="Next Prompt",
                                             font=("Arial", 25))
                    EMR_next_button.place(x=600, y=250)

                # if user has reached the end
                except IndexError:
                    next_activity()

            elif what_act == "info/tips":
                # check for end of tips list
                try:
                    what_act_tips = Label(activity_frame,
                                          text=what_act_tips_text[
                                              what_act_tips_text_num],
                                          padx=10, pady=2, bg="#E2B6CE",
                                          fg="#131117",
                                          font=("Arial", 25))
                    what_act_tips.place(x=100, y=160)

                    # button to show the next prompt/text
                    what_act_tips_next_button = Button(activity_frame,
                                                       command=next_tips_prompt,
                                                       padx=10, pady=2,
                                                       bg="#E2B6CE",
                                                       fg="#131117",
                                                       text="Next Tip",
                                                       font=("Arial", 25))
                    what_act_tips_next_button.place(x=650, y=360)
                # if user reached the end of the tips list
                except IndexError:
                    next_activity()

        # if program has been completed

        except IndexError:
            # write to file to signify the end of a end of a prep
            with open("report.txt", "a", encoding="utf-8") as file:
                file.write("\n----End of Prep----\n\n")
                messagebox.showinfo(title=None, message="You have finished "
                                    "the program's warmup."
                                    " Thank you for using "
                                    "' Drama Prep Program '")
                messagebox.showinfo(
                    title=None, message="Redirecting you back to the "
                    "main window")

            # take user back to home screen
            open_window("opening window", window)

# select activity difficulty and length of time


def select_activity(i, window, activity_duration):
    """These butons allow the user to choose how difficult
    and long they want their prep to be"""
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

    # reload the window
    open_window("start screen", window)


def write_to_lines(line_from_input_line, window, letter_list):
    """Function to send user's line to the .txt file and
    make a var to compare user responce later"""
    global line_cycle, str_cut_line, file_line_input, word_list
    cut_line = []
    str_cut_line = ""

# code to filter out incorrect inputs and provide user
# feedback based on what they did wrong
    if not line_from_input_line.get().count('  ') >= 1:
        if not line_from_input_line.get().count('') == 1:
            if not line_from_input_line.get().count(' ') == 1:
                if not line_from_input_line.get()[-1] == ' ':
                    if line_from_input_line.get().count(' ') >= 3:
                        if not line_from_input_line.get()[0] == ' ':
                            if not line_from_input_line.get(
                            ) in file_line_input:

                                # user's entered lines
                                file_line_input.append(
                                    line_from_input_line.get())
                                with open("report.txt", "a",
                                          encoding="utf-8")as file:
                                    file.write("\nUsers line to learn:  " +
                                               file_line_input[-1] + "\n")
                                # sepparate all characters in the user's
                                # entered line
                                for letter in file_line_input[-1]:
                                    letter_list.append(letter)

                                # check for any entry
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

                                    # the string that gets shown to the user
                                    # for them to fill in the blanks
                                    str_cut_line = "".join(cut_line)
                                    line_cycle += 1
                                    word_list.append(str_cut_line)

                                    # if more linse need to be inputted still
                                    if line_cycle < difficulty+2:
                                        messagebox.showinfo(title=None,
                                                            message="your line "
                                                            "has been "
                                                            "inputted, please "
                                                            "input "
                                                            "{} more".format(
                                                                difficulty -
                                                                line_cycle+2))

                                    # if last line was just inputted
                                    else:
                                        messagebox.showinfo(title=None,
                                                            message="your line "
                                                            "has been inputted,"
                                                            " continuing to the"
                                                            " second part "
                                                            "of the "
                                                            "activity...")
                                    # reload page
                                    open_window("activity window", window)

                                except ValueError:
                                    messagebox.showerror(
                                        title=None, message="please add "
                                        "more words to practice")
                            else:
                                messagebox.showerror(
                                    title=None, message="please input a "
                                    "line different to a "
                                    "previous one")
                        else:
                            messagebox.showerror(
                                title=None, message="please remove spaces "
                                "from infront of the line")
                    else:
                        messagebox.showerror(
                            title=None, message="please add more "
                            "words to practice")
                else:
                    messagebox.showerror(
                        title=None, message="please do not end your "
                        "input with a space")
            else:
                messagebox.showerror(
                    title=None, message="please enter more words "
                    "into the entry field")
        else:
            messagebox.showerror(
                title=None, message="please enter multiple words "
                "into the entry field")
    else:
        messagebox.showerror(
            title=None, message="please do not type consecutive spaces")
    return letter_list


def check_correct_line(whole_line, currentwindow):
    """checks if the user has inputted the correct line into the entry field"""
    global file_line_input, word_to_use

    # check for valid input
    if not whole_line.count('  ') >= 1:
        if not whole_line.count('') == 1:
            if not whole_line[-1] == ' ':
                if not whole_line[0] == ' ':

                    # if answer is correct
                    if str(word_list[word_to_use] +
                           whole_line) == file_line_input[word_to_use]:
                        messagebox.showinfo(
                            title=None,
                            message="you inputted the line in correctly!")
                    # if answer is wrong
                    else:
                        messagebox.showwarning(
                            title=None,
                            message="you inputted the line in wrong, "
                            "the whole line was:   "
                            f"{file_line_input[word_to_use]}")

                    # add to the 'report.txt' file
                    with open("report.txt", "a", encoding="utf-8") as file:
                        file.write("\n" + "answer recieved for the prompt:  ' "
                                   + word_list[word_to_use] + "' was: ' " +
                                   whole_line + " '\n" +
                                   "this resulted in the line: ' " +
                                   word_list[word_to_use] + whole_line +
                                   " '\nthe expected line was      ' " +
                                   file_line_input[word_to_use] + " '\n")
                    open_window("activity window", currentwindow)
                # helping the user to correct their input

                else:
                    messagebox.showerror(
                        title=None, message="please remove spaces from "
                        "infront of the line")
            else:
                messagebox.showerror(
                    title=None, message="please do not end your "
                    "input with a space")
        else:
            messagebox.showerror(
                title=None, message="please enter multiple "
                "words into the entry field")
    else:
        messagebox.showerror(
            title=None, message="please do not type consecutive spaces")


def check_activity(selected_activities, window):
    """checks for both activity settings to have a selection and
    gives error message to user if not"""
    # if user has missed an input
    if selected_activities[0] == "please select a length of time" or \
            selected_activities[1] == "please select a difficulty":
        messagebox.showerror(
            title=None, message="please select a prep duration and difficulty")

    # both choices have been inputted
    else:
        confirm_prep = messagebox.askquestion(
            title=None, message="are you sure you want to "
            "start the activity(s)?")
        if confirm_prep == "yes":
            open_window("activity window", window)


# start the program

open_window("opening window", "")

with open("report.txt", "a", encoding="utf-8") as initfile:
    initfile.write("\n----Session Start----\n")


program.mainloop()
