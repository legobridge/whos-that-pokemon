from pokemon_guesser import *
from questions import *

# todo - Aparna use the functions in pokemon_guesser.py and questions.py


def console_main():
    pg = PokemonGuesser()
    while True:
        state = pg.get_best_statement_for_next_question()
        question = get_question_from_statement(state)
        ans = input(question)
        if ans == 'y':
            pg.add_user_answer_to_kb(state, True)
        elif ans == 'n':
            pg.add_user_answer_to_kb(state, False)
        found_pokemon = pg.return_pokemon_if_found()
        if found_pokemon:
            print(found_pokemon)
            break


if __name__ == '__main__':
    console_main()
