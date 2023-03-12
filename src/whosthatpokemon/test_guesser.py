import unittest

from pokemon_guesser import PokemonGuesser
from questions import *
from src.knowledgebase.logical_classes import Statement, Term


class KBTest(unittest.TestCase):

    def setUp(self):
        self.pg = PokemonGuesser(kb_file='data/pokemon_test_kb.txt')

    def test1(self):
        # A random statement should be generated
        question_statement = self.pg.get_best_statement_for_next_question()
        print(question_statement)

    def test2(self):
        # A random question should be asked
        question_statement = self.pg.get_best_statement_for_next_question()
        question = get_question_from_statement(question_statement)
        print(question)

    def test3(self):
        # No Pokemon should be found for incomplete specification
        self.pg.add_user_answer_to_kb(Statement(['isColor', 'Yellow']), True)
        self.assertFalse(self.pg.return_pokemon_if_found())

    def test4(self):
        # Pokemon should be found for complete specification
        self.pg.add_user_answer_to_kb(Statement(['isColor', 'Yellow']), True)
        self.pg.add_user_answer_to_kb(Statement(['canEvolve']), True)
        self.pg.add_user_answer_to_kb(Statement(['isType', 'Electric']), True)
        self.assertEqual('Pikachu', self.pg.return_pokemon_if_found())

    def test5(self):
        # Pokemon should be found for partial specification which reduces solution space to just 1 Pokemon
        self.pg.add_user_answer_to_kb(Statement(['isColor', 'Yellow']), True)
        self.pg.add_user_answer_to_kb(Statement(['canEvolve']), True)
        self.assertEqual('Pikachu', self.pg.return_pokemon_if_found())

    def test6(self):
        # Pokemon should be found for partial specification which reduces solution space to just 1 Pokemon
        self.pg.add_user_answer_to_kb(Statement(['isColor', 'Green']), True)
        self.assertEqual('Bulbasaur', self.pg.return_pokemon_if_found())

    def test7(self):
        # Pokemon should be found if user answers some questions with no
        self.pg.add_user_answer_to_kb(Statement(['isColor', 'Yellow']), True)
        self.pg.add_user_answer_to_kb(Statement(['canEvolve']), False)
        self.assertEqual('Zapdos', self.pg.return_pokemon_if_found())

    def test8(self):
        # Pokemon should be found if user answers some questions with no
        self.pg.add_user_answer_to_kb(Statement(['isColor', 'Yellow']), False)
        self.pg.add_user_answer_to_kb(Statement(['canEvolve']), True)
        self.pg.add_user_answer_to_kb(Statement(['isPrimaryColor']), False)
        self.assertEqual('Bulbasaur', self.pg.return_pokemon_if_found())


if __name__ == '__main__':
    unittest.main()
