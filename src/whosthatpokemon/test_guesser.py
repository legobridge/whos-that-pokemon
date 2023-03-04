import unittest

from pokemon_guesser import PokemonGuesser
from questions import *
from src.knowledgebase.logical_classes import Statement, Term


class KBTest(unittest.TestCase):

    def setUp(self):
        self.pg = PokemonGuesser()

    def test1(self):
        question_statement = self.pg.get_best_statement_for_next_question()
        print(question_statement)

    def test2(self):
        question_statement = self.pg.get_best_statement_for_next_question()
        question = get_question_from_statement(question_statement)
        print(question)

    def test3(self):
        self.assertFalse(self.pg.return_pokemon_if_found())

    def test4(self):
        self.pg.add_user_answer_to_kb(Statement(['isColor', 'Yellow']), True)
        self.pg.add_user_answer_to_kb(Statement(['canEvolve']), True)
        self.pg.add_user_answer_to_kb(Statement(['isType', 'Electric']), True)
        self.assertEqual('Pikachu', self.pg.return_pokemon_if_found())


if __name__ == '__main__':
    unittest.main()
