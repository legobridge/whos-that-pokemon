from pokemon_guesser import *
from tkinter import *
from tkinter.ttk import Button, Style
from questions import *
from PIL import Image, ImageTk


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
        print("CURR_STMT ", CURR_STMT)
        print("USER_CHOICE ", USER_CHOICE)
        try:
            pg.add_user_answer_to_kb(CURR_STMT, USER_CHOICE)
        finally:
            refresh_question()

    def no():
        global USER_CHOICE
        global CURR_STMT
        USER_CHOICE = False
        print("CURR_STMT ", CURR_STMT)
        print("USER_CHOICE ", USER_CHOICE)
        try:
            pg.add_user_answer_to_kb(CURR_STMT, USER_CHOICE)
        finally:
            refresh_question()

    def idk():
        global CURR_STMT
        print("CURR_STMT ", CURR_STMT)
        print("USER_CHOICE IDK")
        try:
            pg.remove_ambiguous_predicate(CURR_STMT)
        finally:
            refresh_question()

    def end(text):
        display.set(text)
        yes_button.destroy()
        no_button.destroy()
        idk_button.destroy()


    # get the next question from KB
    def refresh_question():
        global Q
        global CURR_STMT
        pokemon_name = pg.return_pokemon_if_found()

        if pokemon_name is None:
            end('Sorry! No Pokemon matches those features.')
        elif pokemon_name:
            end(f'Maybe you were thinking of... {pokemon_name}?')
            img2 = Image.open('../../data/pokemon_images/'+pokemon_name.lower()+'.png')
            resized_img2 = img2.resize((350, 350), Image.LANCZOS)
            img2 = ImageTk.PhotoImage(resized_img2)
            bg.configure(image=img2)
            bg.image = img2
        else:
            CURR_STMT = pg.get_best_statement_for_next_question()
            if CURR_STMT is not None:
                Q = get_question_from_statement(CURR_STMT)
                display.set(Q)
            else:
                end(" Sorry! \n I'm not sure what else I can ask you about.")

    # create a window and background image
    window = Tk()
    style = Style()
    style.configure('TButton', font=('helvetica', 14, 'bold'), foreground='#ffffff', highlightbackground='#ffcb05', relief='raised')
    style.configure('red.TButton', foreground='red')
    img1 = PhotoImage(file='../../data/pokemon.gif')
    bg = Label(window, image=img1)
    bg.place(x=0, y=0, relwidth=1, relheight=1)
    window.title("WHO'S THAT POKEMON?")
    window.geometry('500x500+400+400')

    # text to display questions
    display = StringVar()
    refresh_question()  # begin
    question_textbox = Label(window, textvariable=display, fg='#ffcb05', bg='#2a75bb', font=('Comic Sans MS', 20, 'bold'), relief='raised')
    question_textbox.pack(side=TOP, padx=5, pady=50)

    # buttons
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
