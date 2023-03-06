import unittest
import read
from kb import KnowledgeBase


class KBTest(unittest.TestCase):

    def setUp(self):
        self.KB = KnowledgeBase([], [], [])

        kb_file = '../../data/pokemon_test_kb.txt'
        perm_rules_file = '../../data/pokemon_perm_rules_kb.txt'

        # Assert starter rules
        data = read.read_tokenize(kb_file)
        for item in data:
            self.KB.kb_assert(item)

        # Assert permanent rules
        perm_rule_data = read.read_tokenize(perm_rules_file)
        for perm_rule in perm_rule_data:
            self.KB.kb_assert(perm_rule)
            self.KB.permanent_rules.append(perm_rule)

    def test1(self):

        fact1 = read.parse_input("fact: (isColor Yellow)")
        fact2 = read.parse_input("fact: (canEvolve)")
        fact3 = read.parse_input("fact: (isType Electric)")
        self.KB.kb_assert(fact3)
        self.KB.kb_assert(fact2)
        self.KB.kb_assert(fact1)

        ask1 = read.parse_input("fact: (isPokemon ?X)")
        answer = self.KB.kb_ask(ask1)
        self.assertEqual(str(answer[0]), "?X : Pikachu")

    def test2(self):

        fact1 = read.parse_input("fact: (isColor Blue)")
        fact2 = read.parse_input("fact: (canEvolve)")
        fact3 = read.parse_input("fact: (isType Water)")
        self.KB.kb_assert(fact3)
        self.KB.kb_assert(fact2)
        self.KB.kb_assert(fact1)

        ask1 = read.parse_input("fact: (isPokemon ?X)")
        answer = self.KB.kb_ask(ask1)
        self.assertEqual(str(answer[0]), "?X : Squirtle")

    def test3(self):

        fact1 = read.parse_input("fact: (~canEvolve)")
        fact2 = read.parse_input("fact: (isColor Yellow)")
        fact3 = read.parse_input("fact: (isType Electric)")
        fact4 = read.parse_input("fact: (isLegendary)")
        self.KB.kb_assert(fact1)
        self.KB.kb_assert(fact2)
        self.KB.kb_assert(fact3)
        self.KB.kb_assert(fact4)

        ask1 = read.parse_input("fact: (isPokemon ?X)")
        answer = self.KB.kb_ask(ask1)
        self.assertEqual(str(answer[0]), "?X : Zapdos")

    def test4(self):

        fact1 = read.parse_input("fact: (~isLegendary)")
        fact2 = read.parse_input("fact: (canEvolve)")
        fact3 = read.parse_input("fact: (isType Water)")
        fact4 = read.parse_input("fact: (isColor Blue)")
        self.KB.kb_assert(fact1)
        self.KB.kb_assert(fact2)
        self.KB.kb_assert(fact3)
        self.KB.kb_assert(fact4)

        ask1 = read.parse_input("fact: (isPokemon ?X)")
        answer = self.KB.kb_ask(ask1)
        self.assertEqual(str(answer[0]), "?X : Squirtle")

    def test10(self):
        KB = KnowledgeBase([], [], [])

        rule1 = read.parse_input("rule: ((isColor Yellow) (isLegendary) (isType Electric)) -> (isPokemon Zapdos)")
        rule2 = read.parse_input("rule: ((isColor Yellow) (canEvolve) (isType Electric)) -> (isPokemon Pikachu)")
        rule3 = read.parse_input("rule: ((isColor Blue) (canEvolve) (isType Water)) -> (isPokemon Squirtle)")

        KB.kb_assert(rule1)
        KB.kb_assert(rule2)
        KB.kb_assert(rule3)

        fact1 = read.parse_input("fact: (isColor Yellow)")
        fact2 = read.parse_input("fact: (canEvolve)")
        fact3 = read.parse_input("fact: (isType Electric)")
        KB.kb_assert(fact1)
        KB.kb_assert(fact2)
        KB.kb_assert(fact3)

        ask1 = read.parse_input("fact: (isPokemon ?X)")
        answer = KB.kb_ask(ask1)
        self.assertEqual(str(answer[0]), "?X : Pikachu")


if __name__ == '__main__':
    unittest.main()
