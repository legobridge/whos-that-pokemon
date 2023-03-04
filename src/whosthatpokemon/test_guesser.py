import unittest

from pokemon_guesser import PokemonGuesser


class KBTest(unittest.TestCase):

    def setUp(self):
        self.pg = PokemonGuesser()

    def test1(self):
        question_statement = self.pg.get_best_statement_for_next_question()
        print(question_statement)

    def test1(self):
        question_statement = self.pg.get_best_statement_for_next_question()
        print(question_statement)


if __name__ == '__main__':
    unittest.main()
