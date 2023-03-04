from pokemon_guesser import *
from questions import *
from tkinter import *
from tkinter.ttk import Button, Style
from questions import *


def main():
    USER_CHOICE = False
    CURR_STMT = ""  # statement from KB
    Q = ""  # current question
    pg = PokemonGuesser()

    # process user input
    def yes():
        global USER_CHOICE
        global CURR_STMT
        USER_CHOICE = True
        try:
            print("CURR_STMT ", CURR_STMT)
            print("USER_CHOICE ", USER_CHOICE)
            pg.add_user_answer_to_kb(CURR_STMT, USER_CHOICE)
        finally:
            refresh_question()

    def no():
        global USER_CHOICE
        global CURR_STMT
        USER_CHOICE = False
        try:
            pg.add_user_answer_to_kb(CURR_STMT, USER_CHOICE)
        finally:
            refresh_question()

    def idk():
        refresh_question()


    # get the next question from KB
    def refresh_question():
        global Q
        global CURR_STMT
        pokemon_name = pg.return_pokemon_if_found()
        if pokemon_name:
            # TODO
            print("Pokemon found: ", pokemon_name)
        else:
            CURR_STMT = pg.get_best_statement_for_next_question()
            Q = get_question_from_statement(CURR_STMT)
            Text.set(Q)


    # create a window
    window = Tk()
    style = Style()
    style.configure('TButton', font=('helvetica', 14, 'bold'), foreground='blue', relief='RAISED')
    style.configure('red.TButton', foreground='red')
    bgimg = PhotoImage(file='../../data/pokemon.gif')
    bg = Label(window, image=bgimg)
    bg.place(x=0, y=0, relwidth=1, relheight=1)
    window.title("WHO'S THAT POKEMON?")
    window.geometry('500x500+400+400')

    Text = StringVar()
    refresh_question()  # begin
    LabelResult = Label(window, textvariable=Text, fg='blue', bg='light blue', font=('helvetica', 20, 'bold'))
    LabelResult.pack(side=TOP, padx=5, pady=50)

    quit_button = Button(window, text='Quit', style='red.TButton', command=window.destroy)
    quit_button.pack(side=BOTTOM, padx=5, pady=5)
    yes_button = Button(window, text="Yes", command=yes)
    yes_button.place(x=205, y=165)
    no_button = Button(window, text="No", command=no)
    no_button.place(x=205, y=205)
    idk_button = Button(window, text="I don't know", command=idk)
    idk_button.place(x=185, y=245)

    # stop execution
    window.mainloop()


if __name__ == '__main__':
    main()
