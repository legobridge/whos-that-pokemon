from src.knowledgebase import read
from src.knowledgebase.kb import KnowledgeBase
from src.knowledgebase.logical_classes import *


class PokemonGuesser:

    def __init__(self):
        self.KB = KnowledgeBase([], [], [])

        # Assert starter rules
        kb_file = '../../data/pokemon_kb.txt'
        data = read.read_tokenize(kb_file)
        for item in data:
            if isinstance(item, Fact) or isinstance(item, Rule):
                self.KB.kb_assert(item)

        # Assert permanent rules
        perm_rules_file = '../../data/pokemon_perm_rules_kb.txt'
        perm_rule_data = read.read_tokenize(perm_rules_file)
        for perm_rule in perm_rule_data:
            if isinstance(perm_rule, Rule):
                self.KB.kb_assert(perm_rule)
                self.KB.permanent_rules.append(perm_rule)

    def get_best_statement_for_next_question(self):
        """
        Based on the current pool of Pokemon in the KB,
        return the best statement to ask a question about.

        :return: a Statement, comprising a predicate (isLegendary)
                 and 0 or 1 terms (Red, for the predicate isColor)
        """
        smallest_rule = None
        smallest_rule_length = 100000
        for rule in self.KB.rules:
            if rule in self.KB.permanent_rules:
                continue
            if len(rule.lhs) < smallest_rule_length:
                smallest_rule = rule
                smallest_rule_length = len(rule.lhs)

        # todo - choose statements better
        best_statement = smallest_rule.lhs[0]
        return best_statement

    def return_pokemon_if_found(self):
        """
        Returns the guessed Pokemon, if we have narrowed it down to 1.

        :return: False if it is still not narrowed down to 1 Pokemon.
                 Name of the guessed Pokemon otherwise.
        """
        # todo - Kushal
        return False

    def add_user_answer_to_kb(self, question_statement: Statement, answer: bool):
        """
        Adds the users answer to the question asked to the KB.

        :param question_statement: the Statement that was used to ask the question.
        :param answer: True if the user said yes, False otherwise
        """
        # todo - Kushal
        pass
