from src.whosthatpokemon.pokemon_guesser import *
from tkinter import *
from src.whosthatpokemon.questions import *
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
            img2 = Image.open('data/pokemon_images/'+pokemon_name.lower()+'.png')
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
    #style = Style()
    #style.configure('TButton', font=('helvetica', 14, 'bold'), foreground='#ffcb05', background='#2a75bb', relief='raised')
    #style.configure('red.TButton', foreground='red')
    img1 = PhotoImage(file='data/pokemon_desaturated.gif')
    bg = Label(window, image=img1)
    bg.place(x=0, y=0, relwidth=1, relheight=1)
    window.title("WHO'S THAT POKEMON?")
    window.geometry('700x500+550+200')

    # text to display questions
    display = StringVar()
    refresh_question()  # begin
    question_textbox = Label(window, textvariable=display, fg='#ffcb05', bg='#2a75bb', font=('Comic Sans MS', 20, 'bold'), relief='raised')
    question_textbox.pack(side=TOP, padx=5, pady=50)

    # buttons
    button_font = ('Arial', 15, 'bold')
    button_text_color = '#125fdb'
    yes_button = Button(window, text="Yes", command=yes, foreground=button_text_color,
                        font=button_font, relief='raised')
    yes_button.pack(side=TOP, padx=5, pady=(50, 10))
    no_button = Button(window, text="No", command=no, foreground=button_text_color,
                       font=button_font, relief='raised')
    no_button.pack(side=TOP, padx=5, pady=10)
    idk_button = Button(window, text="I don't know", command=idk, foreground=button_text_color,
                        font=button_font, relief='raised')
    idk_button.pack(side=TOP, padx=5, pady=10)
    quit_button = Button(window, text='Quit', command=window.destroy, foreground=button_text_color,
                         activebackground='red', font=button_font, relief='raised')
    quit_button.pack(side=BOTTOM, padx=5, pady=15)

    # stop execution
    window.mainloop()


if __name__ == '__main__':
    main()
