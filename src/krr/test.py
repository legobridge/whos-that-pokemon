import unittest
import read
from logical_classes import *
from kb import KnowledgeBase


class KBTest(unittest.TestCase):

    def setUp(self):
        self.KB = KnowledgeBase([], [], [])

        # Assert starter rules
        kb_file = '../../data/pokemon_kb.txt'
        data = read.read_tokenize(kb_file)
        for item in data:
            if isinstance(item, Fact) or isinstance(item, Rule):
                self.KB.kb_assert(item)

        perm_rules_file = '../../data/pokemon_perm_rules_kb.txt'
        perm_rule_data = read.read_tokenize(perm_rules_file)
        for perm_rule in perm_rule_data:
            if isinstance(perm_rule, Rule):
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
